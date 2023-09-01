#!/bin/bash

eval "$(conda shell.bash hook)"
conda activate medico
cd MediaEval2023-Medico-EvalScript

: '
### Description ###
gt : The provided ground truth CSV file path.
res : The provided result CSV file path. 
      Make sure gt and res columns are the same.
      The sum of three columns should be 100.
'

python medico_eval_scripts/motility.py \
--gt VISEM_Tracking_Train_v4/csv_files/semen_analysis_data_Train.csv \
--res VISEM_Tracking_Train_v4/motility_example_prediction.csv