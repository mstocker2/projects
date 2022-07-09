#get initial look at the NLS and COVID data

import pandas as pd
import numpy as np
nls97= pd.read_csv('nls_raw.csv')
covidtotals= pd.read_csv('covidtotals.csv')

#show number of rows and columns
print(nls97.shape)
print(covidtotals.shape)

#are the index values unique, replace the default 0-### index
nls97.set_index("personid", inplace=True)
#print(nls97.index)

#show the data types and non-null values
#print(nls97.info())

#how to transpose data to see more details
print(nls97.head(2).T)
