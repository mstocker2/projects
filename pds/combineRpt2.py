import pandas as pd
import glob

#create path to get csv files in directory
path = "/home/michael/Documents/GitHub/projects/pds"
pattern = (path + "/*.csv")
files = glob.glob(pattern)

#create df
df = pd.read_csv(files[0], encoding= "utf-8", delimiter= ',')

for file in files[1:len(files)]:
    df_csv= pd.read_csv(file, encoding= "utf-8", delimiter=',')
    df = df.merge(df_csv, on=['Material'], how= 'outer')
#print(df)
df.to_csv('combined.csv')