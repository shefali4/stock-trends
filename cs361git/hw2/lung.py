import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import scipy.stats as stats
do = pd.read_csv("/Users/shefalisharma/Downloads/Nebraska - Sheet1.csv")
dol = pd.read_csv("/Users/shefalisharma/Downloads/NoOutlier - Sheet1.csv")


do = do.filter(['CIG', 'LEUK'])
dol = dol.filter(['CIG', 'LEUK'])



plt.figure(figsize=(8,8))
plt.scatter(do['CIG'], do['LEUK'])

plt.annotate(do['STATE'], # this is the text
                (dol['CIG'], dol['LEUK']) , # this is the point to label
                 textcoords="offset points", # how to position the text
                 xytext=(0,10), # distance from text to points (x,y)
                 ha='center')



plt.show()