#!/bin/bash

eval "$(conda shell.bash hook)"
conda activate medico
cd MediaEval2023-Medico-EvalScript

: '
### Description ###

GT_FOLDER: The provided MOT format ground truth folder path. 
             It should always start with gt/mot_challenge/
TRACKERS_FOLDER: MOT format tracking result folder path. 
                   It should always start with trackers/mot_challenge/
OUTPUT_FOLDER: the folder path to save the evaluation results.
SPLIT_TO_EVAL: The split to evaluate. It can be 'train', 'test', or 'all'.
DO_PREPROC: should always be False
METRICS: HOTA (by default)
USE_PARALLEL: True to use parallel computing. False to use single core.
NUM_PARALLEL_CORES: The number of cores to use for parallel computing. (2+ for best performance)
'

python scripts/run_mot_challenge.py \
--GT_FOLDER VISEM_Tracking_Train_v4/trackeval_MOT/gt/mot_challenge \
--TRACKERS_FOLDER VISEM_Tracking_Train_v4/trackeval_MOT/trackers/mot_challenge \
--OUTPUT_FOLDER MediaEval2023-Medico-EvalScript/medico_eval_scripts \
--SPLIT_TO_EVAL 'test' \
--DO_PREPROC False \
--METRICS HOTA \
--USE_PARALLEL True \
--NUM_PARALLEL_CORES 4