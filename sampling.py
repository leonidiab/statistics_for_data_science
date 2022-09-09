import pandas as pd
import random
import numpy as np

def simple_random(dataset, samples):
    return dataset.sample(n=samples,random_state=1)

