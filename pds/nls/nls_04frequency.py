#generating frequencies for catagorical variances
#Cookbook-P103

import pandas as pd
import numpy as np
nls97 = pd.read_csv('nls_raw.csv')
nls97.set_index('personid', inplace=True)
nls97.loc[:, nls97.dtypes == 'object'] = nls97.select_dtypes(['object']).apply(lambda x: x.astype('category'))

#figure out value counts
catcols = nls97.select_dtypes(include= ['category']).columns
#print(nls97[catcols].isnull().sum())

#show the frequency of marital status
#print(nls97.maritalstatus.value_counts())

#turn of the default sorting
#print(nls97.maritalstatus.value_counts(sort=False))

#change the values to percentages
print(nls97.maritalstatus.value_counts(sort=False, normalize=True))
	


