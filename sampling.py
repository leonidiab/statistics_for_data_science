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

def grouping_sampling(dataset, group_quiantity, label_name): #label_name must be a string value
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
            
    dataset[label_name] = groups
    random.seed(1)
    selected_group = random.randint(0, group_quiantity)
    return dataset[dataset[label_name]==selected_group]

def stratified_sampling(dataset,label_name,testSize=100/len(dataset)): #label_name must be a string
    split = StratifiedShuffleSplit(test_size=testSize, random_state=1)
    for _, y in split.split(dataset,dataset[label_name]):
        df_y = dataset.iloc[y]
    return df_y

def reservoir_sampling(dataset, samples_quantity):
    stream = []
    for i in range(len(dataset)):
        stream.append(i)
        
    df_length = len(dataset)
    reservoir = [0] * samples_quantity
    i = samples_quantity
    while i < df_length:
        j = random.randrange(0, i+1)
        if j < samples_quantity:
            reservoir[j] = stream[i]
        i+=1
    return dataset.iloc[reservoir]