#evaluate Covid data from Python data cleaning cookbook
#CH 3 p 109
import pandas as pd 
import numpy as np 
import matplotlib.pyplot as plt

covidtotals= pd.read_csv('covidtotals.csv', parse_dates= ['lastdate'])
covidtotals.set_index("iso_code", inplace=True)

#print(covidtotals.shape)
#print(covidtotals.describe())

#closer look at distribution of values for the cases and death columns
totvar= ['location', 'total_cases','total_deaths','total_cases_pm', 'total_deaths_pm']
covidtotals[totvar].quantile(np.arange(0.0,1.1,0.1))
#print(covidtotals[totvar])

#create histogram describe to distribution of key variables.
#check the relationship between the mean and medium of covid cases by country
#results will show that the data is not normally distributed.
plt.hist(covidtotals['total_cases']/1000, bins=12)
plt.title("Total Covid Cases")
plt.xlabel('Cases')
plt.ylabel('Number of Countries')
plt.show()