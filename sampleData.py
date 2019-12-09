import thoth.thoth as thoth
import numpy as np
import scipy as sp
import pandas as pd
import os
from thothSupplemental import *

#These experiments are to show that the bootstrap works in small archaeological 
## datasets to establish whether we need more categories in a given typology

#The assumption here is that arch. data are a small sized n multinomial draw from
## an m-category (or m-dimensional) categorical distribution

#Thus, we need to sample a cross sample of distributions, as well as within each
# distribution, to establish whether the method works

# This is done for categories m = 2 through 10, n = 2 through 30, 100 different 
# probability distributions, 100 different draws at each level

# The results are stored as a pandas dataframe that is saved at each level of m
## for each category


# First, let's establish the parameters and storage

results = create_structure(['m','distribution','draw','trueEnt','naive'])

mrange = np.arange(2,11)
nrange = np.arange(2,31)
distributioncount = 10
drawcount = 10
bootRep = 1000


# Now, run the loop
os.chdir('/home/cabaniss/results')

for m in mrange:
    # Make a new distribution
    distribution = sp.random.dirichlet(m*[1.],distributioncount)
    trueEnt = np.array([sum(-d*np.log(d)/np.log(2)) for d in distribution])
    for i in range(distributioncount):
        for n in nrange:
            #Make a new draw with n entities
            draw = np.random.multinomial(n,distribution[i],drawcount)
            for j in range(drawcount):
                results = add_row([m,i,j,trueEnt[i],get_entropy(draw[j],counted=True,bootstrap=False)] + get_entropy(draw[j],bootRep,counted=True),results)
    results.to_csv('Results10x10x100.csv')
    




