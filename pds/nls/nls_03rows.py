#selecting and filtering rows
import pandas as pd
import numpy as np
nls97 = pd.read_csv('nls_raw.csv')
nls97.set_index('personid', inplace=True)

#slice df to start at row 1001 to 1004
#print(nls97[1000:1004].T)

#slice df to start at row 1001 to 1004 and skip every other row
#print(nls97[1000:1004:2].T)

#how to use iloc to get row position, this script returns the first 3 rows
#could use negatives to select the ending rows
#print(nls97.iloc[[0,1,2]].T)

#selecting rows with boolean indexing
print(nls97.nightlyhrssleep.quantile(0.05))
print(nls97.nightlyhrssleep.count())