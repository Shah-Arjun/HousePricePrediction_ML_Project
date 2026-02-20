# Generic libraries - commonly used
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# data set
from sklearn.datasets import fetch_california_housing

# get the data set
data = fetch_california_housing()

# print(data.DESCR)

# creating data frame
df = pd.DataFrame()

# data.data
print(data.data.shape)  #(20640, 8)