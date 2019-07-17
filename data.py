#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jul 16 15:34:12 2019

@author: ghost
"""
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

#import the dataset 
data =pd.read_csv("Data.csv")
x=data.iloc[:,:-1].values
y=data.iloc[:,:3].values
