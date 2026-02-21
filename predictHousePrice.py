# Generic libraries - commonly used
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# data set -- independent data
from sklearn.datasets import fetch_california_housing

# get the data set
data = fetch_california_housing()

# print(data.DESCR)

# creating data frame
df = pd.DataFrame(data = data.data, columns=data.feature_names)

# print(df.head())   #first five rows

print('\n')

# data.data
print(data.data.shape)  #(20640, 8)
 

# setting output column in dataset --> dependent variable
df['Target'] = data.target

print(df.head())



# Exploratory Data Analysis(EDA)
