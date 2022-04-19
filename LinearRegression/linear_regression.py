import numpy as np
from util.features import prepare_for_training

class LinearRegression:
    def __init__(self,data,labels,polynomial_degree = 0,sinusoid_degree = 0,normalize_data = True):
        prepare_for_training()