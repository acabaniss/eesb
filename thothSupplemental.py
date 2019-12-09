#THOTH supplemental toolkit
###This provides some data-cleaning functions for working with THOTH

import thoth.thoth as thoth
import numpy as np
import pandas as pd


def count_unique_na(x):
    """
    For a one-dimensional series or array, remove NAs and NANs, then
    count the number of each uniquely observed value.
    x -  a one dimensional series or array."""
    
    x = [i for i in x if pd.isnull(i) == False] 
    u = np.unique(x)
    y = []
    for i in u:
        y.append(sum([1 for j in x if j == i]))
    return y
    
def remove_zeros(x):
    """
    Equivalent cleaning to count_unique_na, but for already counted data.
    """
    y = x[x!= 0]
    return y
    
def create_structure(additional):
    """
    Create a blank pandas dataframe structure for storing entropy bootstrap results.
    additional - additional list of column names
    """
    r = pd.DataFrame(columns=additional + ['mean','1smin','1smax','2smin','2smax','samp','N'])
    return r

def add_row(x,r):
    """
    Add a row to the results data frame to eventually be exported.
    """
    add = pd.DataFrame(data = [x],columns=r.columns)
    return r.append(add,ignore_index = True)

def get_entropy(x, rep=10000, counted = False, bootstrap = True):
    """
    This is a helper script that takes a dataset and runs the THOTH bootstrap
    entropy on a dataset.
    x - a dataset, either counted (counter = True) or still raw (counted = False)
    rep - number of repetitions, a parameter of the THOTH bootstrap
    counted - whether x is already counted or is a raw array
    bootstrap - whether to return the THOTH result (True, default) or the naive result (False)
    
    Returns either the standard THOTH bootstrap output:
    (mean, 1-std below, 1-std above, 2-std below, 2-std above, repetitions, sample size)
    Or returns just the naive entropy.
    """
    if counted == False:
        cv = count_unique_na(x)
    else:
        cv = remove_zeros(x)
    N = sum(cv)
    if bootstrap == True:
        output = thoth.calc_entropy(cv,rep)
        return list(output) + [rep,N]
    else:
        array = thoth.prob_from_array(cv)
        return thoth.entropy(array)
