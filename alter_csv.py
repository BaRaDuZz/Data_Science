import pandas as pd

# Originale Csv von Kaggle --> Female durch 1 ersetzt und male durch 0
# Children "no" durch 0 ersetzt und "yes durch 1
# Erste leer Spalte gelöscht

# Deletes first column of the csv
df = pd.read_csv('Big_One.csv')
# If you know the name of the column skip this
first_column = df.columns[0]
# Delete first
df = df.drop([first_column], axis=1)
df = df.replace("female", 1)
df = df.replace("male", 0)
df = df.replace("no", 0)
df = df.replace("yes", 1)
df.to_csv('Affairs.csv', index=False)


