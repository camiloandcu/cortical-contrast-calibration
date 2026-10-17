"""Descriptive ABIDE design audit; no fitted research models.
Run from repository root: python3 literature/audit_design_coverage.py.
"""
import csv
from collections import Counter
from pathlib import Path
from statistics import median
ROOT=Path(__file__).resolve().parents[1]
with (ROOT/'data/derived/abide1_freesurfer_thickness.csv').open(encoding='utf-8-sig') as f:
    rows=list(csv.DictReader(f))
def write(name,records):
    with (ROOT/'literature'/name).open('w',encoding='utf-8',newline='') as f:
        writer=csv.DictWriter(f,fieldnames=list(records[0]));writer.writeheader();writer.writerows(records)
def complete(r):
    return r['complete_68_regions']=='1' and r['invalid_thickness_values']=='0'
stages={
    'bilateral_stats':rows,
    'complete_68': [r for r in rows if complete(r)],
    'illustrative_QC': [r for r in rows if complete(r) and r['qc_anat_rater_2']=='OK' and r['qc_anat_rater_3']=='OK'],
}
groups=[('1','1'),('1','2'),('2','1'),('2','2')]
summary=[];sitegroups=[];support=[];bins=[]
for stage, rs in stages.items():
    sites=sorted({r['SITE_ID'] for r in rs})
    for dx,sex in groups:
        gr=[r for r in rs if (r['DX_GROUP'],r['SEX'])==(dx,sex)]
        ages=sorted(float(r['AGE_AT_SCAN']) for r in gr)
        summary.append(dict(stage=stage,DX_GROUP=dx,SEX=sex,n=len(gr),age_min=min(ages),age_median=median(ages),age_max=max(ages),sites=len({r['SITE_ID'] for r in gr}),n_age_8_to_18=sum(8<=x<=18 for x in ages),n_age_10_to_18=sum(10<=x<=18 for x in ages)))
    for site in sites:
        ranges=[];counts=[]
        for dx,sex in groups:
            gr=[r for r in rs if r['SITE_ID']==site and (r['DX_GROUP'],r['SEX'])==(dx,sex)]
            ages=[float(r['AGE_AT_SCAN']) for r in gr];counts.append(len(gr))
            if ages:ranges.append((min(ages),max(ages)))
            sitegroups.append(dict(stage=stage,SITE_ID=site,DX_GROUP=dx,SEX=sex,n=len(gr),age_min=min(ages) if ages else '',age_max=max(ages) if ages else ''))
            for lo,hi in [(6,8),(8,10),(10,12),(12,14),(14,16),(16,18),(18,25),(25,65)]:
                bins.append(dict(stage=stage,SITE_ID=site,DX_GROUP=dx,SEX=sex,age_lower=lo,age_upper_exclusive=hi,n=sum(lo<=x<hi for x in ages)))
        lo=max((v[0] for v in ranges),default=0);hi=min((v[1] for v in ranges),default=0)
        support.append(dict(stage=stage,SITE_ID=site,n_total=sum(counts),n_ASD_male=counts[0],n_ASD_female=counts[1],n_control_male=counts[2],n_control_female=counts[3],all_four_groups=int(all(counts)),all_four_min_ge_5=int(min(counts)>=5),four_group_range_intersection_min=lo if len(ranges)==4 and lo<=hi else '',four_group_range_intersection_max=hi if len(ranges)==4 and lo<=hi else '',positive_width_intersection=int(len(ranges)==4 and lo<hi),warning='Range intersection alone does not demonstrate local age overlap or model identifiability'))
write('abide_design_group_summary.csv',summary)
write('abide_design_site_groups.csv',sitegroups)
write('abide_design_age_cells.csv',bins)
write('abide_design_support.csv',support)
for stage,rs in stages.items():
    ss=[s for s in support if s['stage']==stage]
    print(stage,'n=',len(rs),'all four groups sites=',sum(s['all_four_groups'] for s in ss),'min5 sites=',[s['SITE_ID'] for s in ss if s['all_four_min_ge_5']],'inclusive intersections=',sum(s['four_group_range_intersection_min']!='' for s in ss),'positive-width intersections=',sum(s['positive_width_intersection'] for s in ss))
print('group summary',summary)
print('QC min5 support',[s for s in support if s['stage']=='illustrative_QC' and s['all_four_min_ge_5']])
