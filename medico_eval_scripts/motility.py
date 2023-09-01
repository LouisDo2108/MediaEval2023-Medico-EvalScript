import pandas as pd
import numpy as np
from argparse import ArgumentParser
from copy import deepcopy
from sklearn.metrics import mean_squared_error, mean_absolute_percentage_error


def check_result_csv(gt, res):
    assert (gt.columns == res.columns).all(), "Columns of ground truth and results CSV files are not the same"
    res['sum'] = res[[x for x in res.columns if x != 'ID']].sum(axis=1)
    assert np.allclose(res['sum'], 100), "Sum of all columns of results CSV file is not 1"
    

def main(args):
    
    # Read ground truth CSV file
    gt_path = args.gt
    res_path = args.res
    
    gt = pd.read_csv(gt_path)
    gt = gt[['ID', 'Progressive motility (%)', 'Non progressive sperm motility (%)',
        'Immotile sperm (%)']]

    # Read your results CSV file, it should have the same format as the ground truth CSV file
    res = pd.read_csv(res_path)
    
    # Select only the rows that are in the both ground truth and results CSV files
    gt = gt[gt['ID'].isin(res['ID'])]
    
    print("Checking results CSV file...")
    check_result_csv(deepcopy(gt), deepcopy(res))
    
    for column in res.columns:
        if column == 'ID':
            continue
        gt_column = gt[column]
        res_column = res[column]
        mae = mean_squared_error(gt_column, res_column)
        mape = mean_absolute_percentage_error(gt_column, res_column)
        print(f"{column:40s} MAE: {mae:10.2f}, MAPE: {mape:10.2f}")


if __name__ == "__main__":
    
    parser = ArgumentParser()
    parser.add_argument('--gt', type=str, help="Ground truth CSV file path")
    parser.add_argument('--res', type=str, help="Results CSV file path")
    args = parser.parse_args()
    
    main(args)