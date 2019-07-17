
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

#import the dataset 
data =pd.read_csv("Data.csv")
x=data.iloc[:,:-1].values
y=data.iloc[:,:3].values

#missing data
from sklearn.preprocessing import Imputer
imputer=Imputer(missing_values='NaN',strategy='mean',axis = 0)
imputer=imputer.fit(x[:,1:3])

x[:,1:3]=imputer.transform(x[:,1:3])
