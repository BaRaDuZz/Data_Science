import pandas as pd  # Data manipulation
import numpy as np  # Data manipulation
import matplotlib.pyplot as plt  # Visualization
import seaborn as sns  # Visualization

pd.set_option('display.max_columns', None)

plt.rcParams['figure.figsize'] = [16, 10]
plt.rcParams['font.size'] = 14
plt.rcParams['font.weight'] = 'bold'
plt.style.use('seaborn-whitegrid')

df = pd.read_csv('Affairs.csv')
print('\nNumber of rows and columns in the data set: ', df.shape)
print('')

# print(df.head())
# print(df.describe())

# Correlation Matrix
corr = df.corr()
sns.heatmap(corr, cmap='Wistia', annot=True)

# Standard Korrelations-Graf
sns.lmplot(x='affairs', y='age', data=df, aspect=2, height=6)
plt.xlabel('Affairs: as Independent variable')
plt.ylabel('Age: as Dependent variable')
plt.title('Affairs Vs Age')

# Violin-Plot Gender und Anzahl der Affären
f = plt.figure(figsize=(14, 6))
ax = f.add_subplot(121)
sns.violinplot(x='gender', y='affairs', data=df, palette='Wistia', ax=ax)
ax.set_title('Violin plot of affairs vs gender')

# boxplot
plt.figure(figsize=(14, 6))
sns.boxplot(x='religiousness', y='affairs', hue='gender', data=df, palette='rainbow')
plt.title('Box plot of religiousness vs affairs');

females = df['gender'].value_counts(1)
males = df['gender'].value_counts(0)


print(df.head())




plt.show()
