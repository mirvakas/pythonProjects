import pandas as pd

df = pd.read_csv('User list.csv')
# print(df.tail(3))
print(df.columns) # Read All Columns
print(df[['COMPANY_NAME','FULL_NAME', 'EMAIL1']][0:20])
# print(df.COMPANY_NAME)