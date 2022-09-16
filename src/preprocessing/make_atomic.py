# Creates atomic file of transactions_train.csv
import os
from pathlib import Path

os.chdir('/content/drive/MyDrive/hnm')
DATA_PATH = Path.cwd() / 'data'
RAW = DATA_PATH / 'raw'
PROCESSED = DATA_PATH / 'processed'
SUBMISSION = DATA_PATH / 'submission'

import pandas as pd
import numpy as np


if __name__=='__main__':
    train = pd.read_csv(RAW / 'transactions_train.csv')

    train.t_dat = pd.to_datetime(train.t_dat, format="%Y-%m-%d")
    train['timestamp'] = train.t_dat.values.astype(np.int64) // 10 ** 9

    train_inter = train[['customer_id', 'article_id', 'timestamp']].rename(columns={
        'customer_id': 'user_id:token', 'article_id': 'item_id:token', 'timestamp': 'timestamp:float'})

    train_inter.to_csv(PROCESSED / 'recbox_data/recbox_data.inter', index=False, sep='\t')