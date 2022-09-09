import pandas as pd
import random
import numpy as np
from sklearn.model_selection import StratifiedShuffleSplit

def random_sampling(dataset, samples):
    return dataset.sample(n=samples,random_state=1)

def sistematic_sampling(dataset, samples):
    interval = len(dataset)//samples
    random.seed(1)
    begin = random.randint(0, interval)
    indexes = np.arange(begin, len(dataset), step=interval)
    sistematic_sample = dataset.iloc[indexes]
    return sistematic_sample

def grouping_sampling(dataset, group_quiantity):
    interval = len(dataset)//group_quiantity
    groups = []
    group_id = 0
    count = 0
    for _ in dataset.iterrows():
        groups.append(group_id)
        count += 1
        if count > interval:
            count = 0
            group_id += 1
            
    dataset['groups'] = groups #you can change the label name
    random.seed(1)
    selected_group = random.randint(0, group_quiantity)
    return dataset[dataset['groups']==selected_group]

