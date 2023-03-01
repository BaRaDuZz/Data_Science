import pandas as pd

df = pd.read_csv('Affairs_Original_to_add_some_data.csv')
df1 = pd.read_csv('add_some_data1.csv')
df2 = pd.read_csv('add_some_data2.csv')
df3 = pd.read_csv('add_some_data3.csv')
df4 = pd.read_csv('add_some_data4.csv')

df = df.append(df, ignore_index=True)
df = df.append(df, ignore_index=True)

df = df.append(df1, ignore_index=True)
df = df.append(df2, ignore_index=True)
df = df.append(df3, ignore_index=True)
df = df.append(df4, ignore_index=True)

df = df.append(df1, ignore_index=True)
df = df.append(df1, ignore_index=True)
df = df.append(df3, ignore_index=True)



df.to_csv('Big_One.csv', index=False)