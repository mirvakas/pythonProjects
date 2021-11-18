import pandas as pd
df= pd.read_csv('pokemon_data.csv')
df.head(5)
# df.tail()
# df.columns
df2 = pd.read_csv('User list.csv')
df2.head()

# df2.loc[df2['FULL_NAME'] == 'Jim Broker'] # Read specific cells

# Reading Data in Pandas¶
df[['Name', 'HP']][0:3] #Use double brackets to enclose column names and then enter row sequence you want to see
print(df.iloc[3,0]) ##Check exact cell by mentioning the co-ordinates
print(df.iloc[0]) ##Check called row
for index, row in df.iterrows():
    print(row) # This for loop helped iterate iloc[i] multiple times i.e. shows every row one by one.
df.loc[df['Legendary'] == True] #Used to find all rows with specific search key from the mentioned column
df.loc[(df['Legendary'] == False) & (df['Type 2'] == 'Fairy')]  #Used to find all rows with specific search key from the mentioned column
print(df2.iloc[3,2])

# Use of describe to get Count, Mean, Std. Dev etc on all numeric Columns¶
df.describe()

# Sort Data in Columns¶
df2 = df2.sort_values(['FULL_NAME'])
df2.sort_values(['FULL_NAME', 'POSITION_ID'], ascending = [1,0])
df['Total'] = df['HP'] + df['Attack'] + df['Defense'] + df['Speed']
df.head(5)

# Drop Column/s¶
df.drop(columns = ['Total'])

# Create New Column based on a Formula (Sum)¶
df['Total'] = df.iloc[:,4:10].sum(axis=1)
df

# Way to show sequence of columns in the desired sequence¶
cols = list(df.columns)
df = df[cols[0:4] + [cols[-1]] + cols[4:12]] # Way to show sequence of columns in the desired sequence
df

# Save output to a file¶
df.to_csv('modified.csv', index = False)
df.to_excel('modifiedexcel.xlsx', index = False)
df.to_csv('modified.csv', index = False)
df2.describe()

# Conditional Filtering and use of Str.Contains function to filter keywords.¶
new_df = df.loc[(df['Type 1'] == 'Grass') & (df['Type 2'] == 'Poison') & (df['HP'] > 70)]
new_df.reset_index(drop=True, inplace=True) #Inplace is used to make changes to DF only the fly rather than storing it in a new container.
import re
df.loc[df['Name'].str.contains('^d[a-z]*', flags=re.I,  regex = True)]
#flags=re.I is meant to ignore Case Sensitive. One can use python upper() inbuilt function as well

# Conditional Changes¶
df.loc[df['Type 1'] == 'Buggy' , 'Type 1'] = 'Bug'
df.loc[df['Name'].str.contains('^d[a-z]*'.upper(), flags=re.I,  regex = True)]
df.loc[df['Total'] > 500, ['Generation','Legendary']] = ['1',False]
df.loc[df['Total'] > 500]

Group By Function to Group Rows¶
df.groupby(['Type 1']).mean().sort_values('Attack', ascending = 0)
print(df.groupby(['Type 1']).sum().sort_values('Attack', ascending = 0))
print(df.groupby(['Type 1']).count().sort_values('Attack', ascending = 0))
df['Count'] = 1
df.groupby(['Type 1']).count()['Count']

# Handling Data from Large Files in Smaller Chunks¶
# for df in pd.read_csv('modified.csv', chunksize = 5):
#     print("DATA FRAME: ")
#     print(df)
new_df = pd.DataFrame(columns=df.columns)
for df in pd.read_csv('pokemon_data.csv', chunksize=50):
    results = df.groupby(['Type 1']).count()
    new_df = pd.concat([new_df, results])
new_df.drop(columns = ['Type 1'])


