#Create the figure for the publication

import scipy as sp
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


# Make figure 2, showing the resutls of the simulation
## Load the simulation data
res = pd.read_csv('data\\Results10x10x100.csv')

#Distinguish between results with greater and less than 10% accuracy
close = [i for i in res.index if abs(res.iloc[i]['mean']-res.iloc[i]['trueEnt'])/res.iloc[i]['trueEnt'] <= .10]
far = [i for i in res.index if abs(res.iloc[i]['mean']-res.iloc[i]['trueEnt'])/res.iloc[i]['trueEnt'] > .10]

plt.figure(1,figsize=(6.41,3.36))
plt.plot(res.iloc[far]['N'],res.iloc[far]['mean']-log(res.iloc[far]['m'])/log(2),'rx',alpha=.02)
plt.plot(res.iloc[close]['N'],res.iloc[close]['mean']-log(res.iloc[close]['m'])/log(2),'b+',alpha=.02)
plt.axis([1,31,-3.5,.95])
plt.ylabel('EESB estimate (minus log(k)/log(2))')
plt.xlabel('Sample size (n)')
plt.title('Entropy estimates that exceed the maximum are almost always erroneous')
plt.subplots_adjust(left=.12,right=.90,top=.88,bottom=.15)
plt.show()
