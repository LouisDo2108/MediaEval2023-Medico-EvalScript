from pycocotools.coco import COCO
from pycocotools.cocoeval import COCOeval
import numpy as np
from argparse import ArgumentParser
  

def main(args):
    annType = 'bbox'

    #initialize COCO ground truth api
    annFile = args.annFile
    cocoGt=COCO(annFile)

    resFile = args.resFile
    cocoDt=cocoGt.loadRes(resFile)

    if args.all:
        for catId in cocoGt.getCatIds():
            print('Evaluating category: {}'.format(catId))
            cocoEval = COCOeval(cocoGt,cocoDt,annType)
            cocoEval.params.catIds = [catId]
            cocoEval.evaluate()
            cocoEval.accumulate()
            cocoEval.summarize()
    else:
        cocoEval = COCOeval(cocoGt,cocoDt,annType)
        cocoEval.params.catIds = [0] # Sperm class only
        cocoEval.evaluate()
        cocoEval.accumulate()
        cocoEval.summarize()


if __name__ == '__main__':
    
    parser = ArgumentParser()
    parser.add_argument('--annFile', type=str, help="Ground truth JSON file path")
    parser.add_argument('--resFile', type=str, help="Results JSON file path")
    parser.add_argument('--all', action='store_true', help="Evaluate all categories")
    args = parser.parse_args()
    
    main(args)
