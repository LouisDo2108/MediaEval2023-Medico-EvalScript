# MediaEval2023-Medico-EvalScript

**Prerequisites**: 
1. Download this [example data](https://drive.google.com/file/d/1nSsQbAMxCmZoLeEAQwVLYVbQA7zq2WQG/view?usp=sharing).
2. Create a conda enviroment name `medico` with python 3.8 as follows:

```python
conda create -n medico python=3.8 -y
conda activate medico
cd MediaEval2023-Medico-EvalScript
pip install requirements.txt
```

## Subtask 1: Sperm detection and tracking

### Detection

- We use pycocotools to evaluate the detection results. The evaluation script is `MediaEval2023-Medico-EvalScript/medico_eval_scripts/run_detect.sh`.
- To use the script, prepare a resFile in the format of COCO json file:
```
[
    {
        "bbox": [
            404.25,
            260.75,
            19.0,
            18.5
        ],
        "category_id": 0,
        "image_id": 1,
        "score": 0.84277
    },
    ...
]
```
make sure the "image_id" matches the `annotations/Train.json` or `annotations/Val.json` in the provided files. We provide an example `detection_example_prediction.json` in the example data.

---

### Tracking

- We use TrackEval to evaluate the tracking results. The evaluation script is `MediaEval2023-Medico-EvalScript/medico_eval_scripts/run_track.sh`.
- We have provided an example data format for using this script in the trackeval_MOT folder. There are 2 folders:
    - `gt/mot_challenge`: contains the ground truth data in the format of MOTChallenge:
        - `MOT17-*`: contain the ground truth data for different splits.
        - `seqmaps`: contains the name of the sequences in each split.
    - `trackers/mot_challenge`: contains the sample tracking results in the format of MOTChallenge:
        - `MOT17-*/any_name_you_want/data`: the corresponding tracking results for each split. (any_name_you_want is the name of the tracker, in this case, I suppose each team has only one tracker, so use whatever name you want.)
- Please prepare your tracking results in the same format as the sample tracking results. For more information, read `MediaEval2023-Medico-EvalScript/docs/MOTChallenge-Official/Readme.md` and `MediaEval2023-Medico-EvalScript/docs/MOTChallenge-format.txt`.
- The script is class-agnostic, so you don't need to worry about the class id (pedestrian).

## Subtask 2: Efficient detection and tracking
Please use the example python scripts in `MediaEval2023-Medico-EvalScript/medico_eval_scripts/subtask2_example.py` as a reference.

## Subtask 3: Prediction of motility
We use `MediaEval2023-Medico-EvalScript/medico_eval_scripts/subtask3_run_motility.sh` to evaluate the motility prediction results. 

## Subtask 4: Predicting motility using graph data structures
You should use the tracking evaluation script to evaluate the tracking results.

# Acknowledgement
The evaluation scripts are modified from [TrackEval](https://github.com/JonathonLuiten/TrackEval) and [pycocotools](https://github.com/cocodataset/cocoapi/tree/master/PythonAPI/pycocotools).