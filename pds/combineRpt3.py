#merge multiple csv files with pandas
import pandas as pd
import numpy as np

#read in csv data
df1 = pd.read_csv('file1.csv')
df2 = pd.read_csv('file2.csv')
df3 = pd.read_csv('file3.csv')

#merge df1 and df2 to see unique list of materials
df4 = pd.merge(df1,df2, on=['Material'], how = 'right')
print(df4.head(2))

df5 = pd.merge(df4, df3, on = ['Material'], how= 'right')
print(df5.head(3))
