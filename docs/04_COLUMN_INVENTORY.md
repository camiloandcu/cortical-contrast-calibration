# Inventario de columnas observado

Los diez campos originales FreeSurfer se describen en [la revisión](01_DATASET_REVIEW.md) y en el inventario específico (`data/derived/freesurfer_stats_column_inventory.csv`, generado localmente).
La tabla regional derivada conserva el grosor medio, identificadores y campos de auditoría.

Generado por `scripts/profile_datasets.py`.

Faltantes: vacíos, NA/NaN y -9999. Los tipos se infieren de los valores; no sustituyen el diccionario del repositorio.

## abide1/phenotypic

| Columna literal | Tipo observado | Faltantes (%) | Valores únicos | Rango numérico |
|---|---|---:|---:|---|
| `<empty_header>` | integer | 0.0 | 1112 | 0 a 1111 |
| `Unnamed: 0` | integer | 0.0 | 1112 | 1 a 1112 |
| `SUB_ID` | integer | 0.0 | 1112 | 50002 a 51607 |
| `X` | integer | 0.0 | 1112 | 1 a 1112 |
| `subject` | integer | 0.0 | 1112 | 50002 a 51607 |
| `SITE_ID` | text | 0.0 | 20 | — |
| `FILE_ID` | text | 0.0 | 1036 | — |
| `DX_GROUP` | integer | 0.0 | 2 | 1 a 2 |
| `DSM_IV_TR` | integer | 6.47 | 5 | 0 a 4 |
| `AGE_AT_SCAN` | numeric | 0.0 | 709 | 6.47 a 64 |
| `SEX` | integer | 0.0 | 2 | 1 a 2 |
| `HANDEDNESS_CATEGORY` | text | 29.32 | 5 | — |
| `HANDEDNESS_SCORES` | numeric | 67.27 | 105 | -100 a 100 |
| `FIQ` | numeric | 6.47 | 123 | 41 a 148 |
| `VIQ` | integer | 17.54 | 87 | 42 a 180 |
| `PIQ` | integer | 16.28 | 83 | 37 a 157 |
| `FIQ_TEST_TYPE` | text | 15.2 | 12 | — |
| `VIQ_TEST_TYPE` | text | 25.0 | 12 | — |
| `PIQ_TEST_TYPE` | text | 23.29 | 13 | — |
| `ADI_R_SOCIAL_TOTAL_A` | integer | 66.01 | 26 | 2 a 30 |
| `ADI_R_VERBAL_TOTAL_BV` | integer | 65.92 | 23 | 0 a 26 |
| `ADI_RRB_TOTAL_C` | integer | 66.01 | 14 | 0 a 13 |
| `ADI_R_ONSET_TOTAL_D` | integer | 73.29 | 6 | 0 a 5 |
| `ADI_R_RSRCH_RELIABLE` | integer | 64.84 | 2 | 0 a 1 |
| `ADOS_MODULE` | integer | 54.41 | 3 | 2 a 4 |
| `ADOS_TOTAL` | integer | 62.68 | 23 | 0 a 22 |
| `ADOS_COMM` | integer | 64.93 | 9 | 0 a 8 |
| `ADOS_SOCIAL` | integer | 64.84 | 15 | 0 a 14 |
| `ADOS_STEREO_BEHAV` | integer | 70.23 | 9 | 0 a 8 |
| `ADOS_RSRCH_RELIABLE` | integer | 66.19 | 2 | 0 a 1 |
| `ADOS_GOTHAM_SOCAFFECT` | integer | 76.17 | 21 | 0 a 20 |
| `ADOS_GOTHAM_RRB` | integer | 75.72 | 9 | 0 a 8 |
| `ADOS_GOTHAM_TOTAL` | integer | 75.45 | 29 | 0 a 28 |
| `ADOS_GOTHAM_SEVERITY` | integer | 75.45 | 10 | 1 a 10 |
| `SRS_VERSION` | integer | 79.23 | 2 | 1 a 2 |
| `SRS_RAW_TOTAL` | integer | 67.18 | 129 | 0 a 164 |
| `SRS_AWARENESS` | integer | 94.24 | 15 | 1 a 18 |
| `SRS_COGNITION` | integer | 94.24 | 27 | 0 a 29 |
| `SRS_COMMUNICATION` | integer | 94.24 | 34 | 0 a 51 |
| `SRS_MOTIVATION` | integer | 94.24 | 27 | 0 a 29 |
| `SRS_MANNERISMS` | integer | 94.24 | 22 | 0 a 25 |
| `SCQ_TOTAL` | integer | 88.85 | 33 | 0 a 37 |
| `AQ_TOTAL` | integer | 94.96 | 25 | 7 a 42 |
| `COMORBIDITY` | text | 93.62 | 39 | — |
| `CURRENT_MED_STATUS` | text | 27.16 | 3 | — |
| `MEDICATION_NAME` | text | 85.88 | 101 | — |
| `OFF_STIMULANTS_AT_SCAN` | integer | 93.53 | 2 | 0 a 1 |
| `VINELAND_RECEPTIVE_V_SCALED` | integer | 89.93 | 13 | 7 a 19 |
| `VINELAND_EXPRESSIVE_V_SCALED` | integer | 89.93 | 18 | 6 a 23 |
| `VINELAND_WRITTEN_V_SCALED` | integer | 89.93 | 13 | 9 a 21 |
| `VINELAND_COMMUNICATION_STANDARD` | integer | 89.93 | 52 | 40 a 138 |
| `VINELAND_PERSONAL_V_SCALED` | integer | 89.93 | 15 | 7 a 23 |
| `VINELAND_DOMESTIC_V_SCALED` | integer | 89.93 | 17 | 2 a 20 |
| `VINELAND_COMMUNITY_V_SCALED` | integer | 89.93 | 15 | 4 a 21 |
| `VINELAND_DAILYLVNG_STANDARD` | integer | 89.93 | 50 | 42 a 127 |
| `VINELAND_INTERPERSONAL_V_SCALED` | integer | 89.93 | 17 | 1 a 20 |
| `VINELAND_PLAY_V_SCALED` | integer | 89.93 | 17 | 1 a 19 |
| `VINELAND_COPING_V_SCALED` | integer | 89.93 | 17 | 6 a 22 |
| `VINELAND_SOCIAL_STANDARD` | integer | 89.93 | 61 | 20 a 138 |
| `VINELAND_SUM_SCORES` | integer | 89.93 | 85 | 128 a 469 |
| `VINELAND_ABC_STANDARD` | integer | 89.93 | 56 | 41 a 131 |
| `VINELAND_INFORMANT` | integer | 89.93 | 2 | 1 a 2 |
| `WISC_IV_VCI` | integer | 95.05 | 24 | 63 a 144 |
| `WISC_IV_PRI` | integer | 95.05 | 22 | 79 a 137 |
| `WISC_IV_WMI` | integer | 95.05 | 20 | 56 a 126 |
| `WISC_IV_PSI` | integer | 95.05 | 21 | 68 a 131 |
| `WISC_IV_SIM_SCALED` | integer | 95.05 | 12 | 1 a 17 |
| `WISC_IV_VOCAB_SCALED` | integer | 95.05 | 15 | 1 a 18 |
| `WISC_IV_INFO_SCALED` | integer | 95.05 | 13 | 5 a 17 |
| `WISC_IV_BLK_DSN_SCALED` | integer | 95.05 | 14 | 4 a 19 |
| `WISC_IV_PIC_CON_SCALED` | integer | 95.05 | 13 | 3 a 15 |
| `WISC_IV_MATRIX_SCALED` | integer | 95.05 | 11 | 7 a 19 |
| `WISC_IV_DIGIT_SPAN_SCALED` | integer | 95.05 | 13 | 2 a 17 |
| `WISC_IV_LET_NUM_SCALED` | integer | 95.05 | 13 | 2 a 14 |
| `WISC_IV_CODING_SCALED` | integer | 95.05 | 11 | 4 a 15 |
| `WISC_IV_SYM_SCALED` | integer | 95.05 | 12 | 1 a 16 |
| `EYE_STATUS_AT_SCAN` | integer | 0.0 | 2 | 1 a 2 |
| `AGE_AT_MPRAGE` | numeric | 91.01 | 97 | 8.29 a 17.94 |
| `BMI` | numeric | 91.55 | 89 | 6.53 a 35.43 |
| `anat_cnr` | numeric | 1.17 | 1098 | 1.5127e-05 a 51.6918 |
| `anat_efc` | numeric | 1.17 | 1098 | -217.56 a 33.3184 |
| `anat_fber` | numeric | 1.17 | 1098 | -3.12374 a 1734.15 |
| `anat_fwhm` | numeric | 1.17 | 1098 | 2.53393 a 5.93832 |
| `anat_qi1` | numeric | 1.17 | 1098 | 0.000451496 a 0.259048 |
| `anat_snr` | numeric | 1.17 | 1098 | 0.00140007 a 5957.2 |
| `func_efc` | numeric | 1.17 | 1097 | 0.352391 a 0.668279 |
| `func_fber` | numeric | 1.17 | 1097 | 33.8365 a 326.544 |
| `func_fwhm` | numeric | 1.17 | 1096 | 1.58111 a 3.75348 |
| `func_dvars` | numeric | 1.17 | 1097 | 0.709671 a 1.5711 |
| `func_outlier` | numeric | 1.17 | 1097 | 0.000182083 a 0.0801582 |
| `func_quality` | numeric | 1.17 | 1097 | 0.0016933 a 0.0986142 |
| `func_mean_fd` | numeric | 1.17 | 1097 | 0.0161171 a 1.43491 |
| `func_num_fd` | integer | 1.17 | 153 | 0 a 288 |
| `func_perc_fd` | numeric | 1.17 | 451 | 0 a 91.7355 |
| `func_gsr` | numeric | 1.17 | 1097 | -0.0158119 a 0.104225 |
| `qc_rater_1` | text | 0.0 | 3 | — |
| `qc_notes_rater_1` | text | 96.49 | 18 | — |
| `qc_anat_rater_2` | text | 1.08 | 3 | — |
| `qc_anat_notes_rater_2` | text | 75.27 | 16 | — |
| `qc_func_rater_2` | text | 1.08 | 3 | — |
| `qc_func_notes_rater_2` | text | 76.71 | 25 | — |
| `qc_anat_rater_3` | text | 0.09 | 2 | — |
| `qc_anat_notes_rater_3` | text | 90.29 | 7 | — |
| `qc_func_rater_3` | text | 0.09 | 2 | — |
| `qc_func_notes_rater_3` | text | 93.17 | 47 | — |
| `SUB_IN_SMP` | integer | 0.0 | 2 | 0 a 1 |

## abide1/freesurfer_thickness_derived

| Columna literal | Tipo observado | Faltantes (%) | Valores únicos | Rango numérico |
|---|---|---:|---:|---|
| `SUB_ID` | integer | 0.0 | 1035 | 50003 a 51607 |
| `FILE_ID` | text | 0.0 | 1035 | — |
| `SITE_ID` | text | 0.0 | 20 | — |
| `DX_GROUP` | integer | 0.0 | 2 | 1 a 2 |
| `SEX` | integer | 0.0 | 2 | 1 a 2 |
| `AGE_AT_SCAN` | numeric | 0.0 | 657 | 6.47 a 64 |
| `both_hemispheres` | integer | 0.0 | 1 | 1 a 1 |
| `n_regions_available` | integer | 0.0 | 4 | 64 a 68 |
| `complete_68_regions` | integer | 0.0 | 2 | 0 a 1 |
| `invalid_thickness_values` | integer | 0.0 | 1 | 0 a 0 |
| `qc_anat_rater_2` | text | 0.0 | 3 | — |
| `qc_anat_rater_3` | text | 0.0 | 2 | — |
| `lh_bankssts_thickness_mm` | numeric | 0.0 | 719 | 1.458 a 3.547 |
| `lh_caudalanteriorcingulate_thickness_mm` | numeric | 0.1 | 712 | 1.578 a 4.149 |
| `lh_caudalmiddlefrontal_thickness_mm` | numeric | 0.0 | 661 | 1.764 a 3.562 |
| `lh_cuneus_thickness_mm` | numeric | 0.0 | 640 | 1.388 a 3.407 |
| `lh_entorhinal_thickness_mm` | numeric | 0.0 | 804 | 1.071 a 4.74 |
| `lh_frontalpole_thickness_mm` | numeric | 0.0 | 764 | 0.865 a 4.397 |
| `lh_fusiform_thickness_mm` | numeric | 0.0 | 665 | 1.878 a 3.564 |
| `lh_inferiorparietal_thickness_mm` | numeric | 0.0 | 655 | 1.946 a 3.398 |
| `lh_inferiortemporal_thickness_mm` | numeric | 0.0 | 716 | 1.865 a 3.682 |
| `lh_insula_thickness_mm` | numeric | 0.0 | 659 | 2.087 a 3.974 |
| `lh_isthmuscingulate_thickness_mm` | numeric | 0.1 | 671 | 1.502 a 3.796 |
| `lh_lateraloccipital_thickness_mm` | numeric | 0.0 | 615 | 1.514 a 3.03 |
| `lh_lateralorbitofrontal_thickness_mm` | numeric | 0.0 | 697 | 1.909 a 3.827 |
| `lh_lingual_thickness_mm` | numeric | 0.0 | 638 | 1.472 a 3.054 |
| `lh_medialorbitofrontal_thickness_mm` | numeric | 0.1 | 650 | 1.818 a 3.516 |
| `lh_middletemporal_thickness_mm` | numeric | 0.0 | 699 | 1.728 a 3.858 |
| `lh_paracentral_thickness_mm` | numeric | 0.0 | 666 | 1.455 a 3.498 |
| `lh_parahippocampal_thickness_mm` | numeric | 0.0 | 733 | 1.292 a 3.989 |
| `lh_parsopercularis_thickness_mm` | numeric | 0.0 | 645 | 1.664 a 3.724 |
| `lh_parsorbitalis_thickness_mm` | numeric | 0.0 | 739 | 1.773 a 4.185 |
| `lh_parstriangularis_thickness_mm` | numeric | 0.0 | 688 | 1.785 a 3.71 |
| `lh_pericalcarine_thickness_mm` | numeric | 0.0 | 630 | 1.204 a 3.83 |
| `lh_postcentral_thickness_mm` | numeric | 0.0 | 569 | 1.709 a 3.02 |
| `lh_posteriorcingulate_thickness_mm` | numeric | 0.0 | 632 | 1.387 a 4.122 |
| `lh_precentral_thickness_mm` | numeric | 0.0 | 603 | 1.978 a 3.3 |
| `lh_precuneus_thickness_mm` | numeric | 0.0 | 654 | 2.016 a 3.358 |
| `lh_rostralanteriorcingulate_thickness_mm` | numeric | 0.1 | 724 | 1.334 a 4.117 |
| `lh_rostralmiddlefrontal_thickness_mm` | numeric | 0.0 | 685 | 1.823 a 3.483 |
| `lh_superiorfrontal_thickness_mm` | numeric | 0.0 | 676 | 1.969 a 3.732 |
| `lh_superiorparietal_thickness_mm` | numeric | 0.0 | 613 | 1.839 a 3.024 |
| `lh_superiortemporal_thickness_mm` | numeric | 0.0 | 677 | 1.506 a 3.85 |
| `lh_supramarginal_thickness_mm` | numeric | 0.0 | 655 | 1.667 a 3.454 |
| `lh_temporalpole_thickness_mm` | numeric | 0.0 | 790 | 1.778 a 4.727 |
| `lh_transversetemporal_thickness_mm` | numeric | 0.1 | 714 | 1.637 a 3.686 |
| `rh_bankssts_thickness_mm` | numeric | 0.0 | 691 | 1.415 a 3.74 |
| `rh_caudalanteriorcingulate_thickness_mm` | numeric | 0.1 | 680 | 1.75 a 4.052 |
| `rh_caudalmiddlefrontal_thickness_mm` | numeric | 0.0 | 635 | 1.662 a 3.581 |
| `rh_cuneus_thickness_mm` | numeric | 0.1 | 641 | 1.398 a 3.282 |
| `rh_entorhinal_thickness_mm` | numeric | 0.1 | 814 | 1.692 a 4.883 |
| `rh_frontalpole_thickness_mm` | numeric | 0.0 | 785 | 1.546 a 4.382 |
| `rh_fusiform_thickness_mm` | numeric | 0.1 | 679 | 1.978 a 3.655 |
| `rh_inferiorparietal_thickness_mm` | numeric | 0.0 | 656 | 2.002 a 3.436 |
| `rh_inferiortemporal_thickness_mm` | numeric | 0.0 | 719 | 1.59 a 3.776 |
| `rh_insula_thickness_mm` | numeric | 0.0 | 650 | 1.956 a 4.025 |
| `rh_isthmuscingulate_thickness_mm` | numeric | 0.0 | 665 | 1.404 a 3.657 |
| `rh_lateraloccipital_thickness_mm` | numeric | 0.0 | 610 | 1.594 a 3.351 |
| `rh_lateralorbitofrontal_thickness_mm` | numeric | 0.0 | 703 | 1.885 a 3.836 |
| `rh_lingual_thickness_mm` | numeric | 0.0 | 636 | 1.605 a 3.871 |
| `rh_medialorbitofrontal_thickness_mm` | numeric | 0.0 | 665 | 1.886 a 3.737 |
| `rh_middletemporal_thickness_mm` | numeric | 0.0 | 696 | 1.838 a 3.781 |
| `rh_paracentral_thickness_mm` | numeric | 0.0 | 656 | 1.833 a 3.48 |
| `rh_parahippocampal_thickness_mm` | numeric | 0.1 | 701 | 1.551 a 4.236 |
| `rh_parsopercularis_thickness_mm` | numeric | 0.0 | 648 | 1.664 a 3.566 |
| `rh_parsorbitalis_thickness_mm` | numeric | 0.0 | 741 | 1.903 a 4.073 |
| `rh_parstriangularis_thickness_mm` | numeric | 0.0 | 699 | 1.869 a 3.648 |
| `rh_pericalcarine_thickness_mm` | numeric | 0.1 | 604 | 1.179 a 3.042 |
| `rh_postcentral_thickness_mm` | numeric | 0.0 | 562 | 1.608 a 2.922 |
| `rh_posteriorcingulate_thickness_mm` | numeric | 0.19 | 632 | 1.455 a 3.932 |
| `rh_precentral_thickness_mm` | numeric | 0.0 | 579 | 1.869 a 3.265 |
| `rh_precuneus_thickness_mm` | numeric | 0.0 | 650 | 1.971 a 3.442 |
| `rh_rostralanteriorcingulate_thickness_mm` | numeric | 0.1 | 700 | 1.517 a 4.117 |
| `rh_rostralmiddlefrontal_thickness_mm` | numeric | 0.0 | 656 | 1.805 a 3.396 |
| `rh_superiorfrontal_thickness_mm` | numeric | 0.0 | 681 | 2.075 a 3.776 |
| `rh_superiorparietal_thickness_mm` | numeric | 0.0 | 592 | 1.772 a 3.31 |
| `rh_superiortemporal_thickness_mm` | numeric | 0.0 | 695 | 1.843 a 3.929 |
| `rh_supramarginal_thickness_mm` | numeric | 0.0 | 626 | 1.997 a 3.501 |
| `rh_temporalpole_thickness_mm` | numeric | 0.1 | 783 | 1.877 a 4.786 |
| `rh_transversetemporal_thickness_mm` | numeric | 0.1 | 715 | 1.505 a 3.656 |
