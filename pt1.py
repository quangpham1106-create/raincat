import pandas as pd
df = pd.read_csv('Student_Data_With_NULLs.csv')
colAge = df['Age']
print(colAge)