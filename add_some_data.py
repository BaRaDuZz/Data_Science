import pandas as pd

# Originale Csv von Kaggle --> Female durch 1 ersetzt und male durch 0
# Children "no" durch 0 ersetzt und "yes durch 1
# Erste leer Spalte gelöscht

# Deletes first column of the csv
df = pd.read_csv('add_some_data.csv')
# If you know the name of the column skip this

df['age'] = df['age'].replace({17.5: 21, 22: 26, 27: 31, 32: 36, 37: 41, 42: 46})


df.to_csv('add_some_data4.csv', index=False)