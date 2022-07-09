#selecting and organizing columns in the NLS and COVID data sets
import pandas as pd
import numpy as np
nls97= pd.read_csv('nls_raw.csv')
covidtotals= pd.read_csv('covidtotals.csv')

#set index
nls97.set_index('personid', inplace=True)

#convert object data types to catagory data
nls97.loc[:, nls97.dtypes == 'object'] = nls97.select_dtypes(['object']).apply(lambda x: x.astype('category'))
#print(nls97.head(5))

#how to select columns using brackets
analysisdemo = nls97['gender']
#print(analysisdemo.head(2))

#select multiple columns
analysisdemo = nls97[['gender', 'maritalstatus', 'highestgradecompleted']]
#print(analysisdemo.head(3))

#filtering columns
analysiswork = nls97.filter(like='weeksworked')
print(analysiswork.info())