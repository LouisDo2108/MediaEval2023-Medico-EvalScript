#!/bin/bash

eval "$(conda shell.bash hook)"
conda activate medico
cd MediaEval2023-Medico-EvalScript

: '
### Description ###
annFile: The provided COCO format annotation file path.
resFile: The provided COCO format result file path. (image_id must match with the image_id in annFile)
'

python medico_eval_scripts/cocoeval.py \
--annFile VISEM_Tracking_Train_v4/annotations/val.json \
--resFile VISEM_Tracking_Train_v4/tracking_example_prediction.json \
--all