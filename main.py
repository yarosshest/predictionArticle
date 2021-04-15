import numpy as np
import pandas as pd
import json
from scholarly import scholarly
import time
from scholarly import ProxyGenerator
import json
import DBnaorm
from catboost import CatBoostRegressor
if __name__ == '__main__':
    bd = DBnaorm.createBd()
    data = bd.get_data(600000)
    xd = data[0]
    yd = data[1]
    # train_data = xd
    # train_labels = yd

    train_data = xd[1:600000]
    eval_data  = xd[:1]
    train_labels = yd[1:600000]
    eval_labels = yd[:1]
    print("Data loaded")
    # Initialize CatBoostRegressor
    model = CatBoostRegressor(iterations=30,
                              learning_rate=1,
                              depth=10,
                              task_type="GPU",
                              cat_features=[0, 4, 5])
    # Fit model
    model.fit(train_data, train_labels, verbose=False, plot=True)
    preds = model.predict(eval_data)
    print("done")
    # tensorboard --logdir=catboost_info