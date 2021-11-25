#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from scipy.stats import chi2_contingency
import scipy.stats as stats



def distplot(data):
    for column in data.select_dtypes(np.number).columns:
        sns.distplot(data[column])
        plt.show()

def boxplot(data):
    for column in data.select_dtypes(np.number).columns:
        sns.boxplot(data[column])
        plt.show()


# In[9]:


def boxcox_transform(data):
    numeric_cols = data.select_dtypes(np.number).columns
    _ci = {column: None for column in numeric_cols}
    for column in numeric_cols:
        # since i know any columns should take negative numbers, to avoid -inf in df
        data[column] = np.where(data[column]<=0, np.NAN, data[column]) 
        data[column] = data[column].fillna(data[column].mean())
        #print(column)
        transformed_data, ci = stats.boxcox(data[column])
        data[column] = transformed_data
        _ci[column] = [ci] 
    return data, _ci


# In[10]:
def replace_outliers(data, in_columns):
    
    for column in in_columns:
        iqr = np.percentile(data[column],75) - np.percentile(data[column],25)
        upper_limit = np.percentile(data[column],75) + 1.5*iqr
        lower_limit = np.percentile(data[column],25) - 1.5*iqr
        #data = data[(data[column]>lower_limit) & (data[column]<upper_limit)]
        data.loc[(data[column]>upper_limit), column] =  upper_limit
        data.loc[(data[column]>lower_limit), column] =  lower_limit
    
    return data

def remove_outliers(data, threshold=1.5, in_columns=[], skip_columns=[]):
    for column in in_columns:
        if column not in skip_columns:
            upper = np.percentile(data[column],75)
            lower = np.percentile(data[column],25)
            iqr = upper - lower
            upper_limit = upper + (threshold * iqr)
            lower_limit = lower - (threshold * iqr)
            data = data[(data[column]>lower_limit) & (data[column]<upper_limit)]
    return data

