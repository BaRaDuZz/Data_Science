import seaborn as sns
import pandas as pd  # Data manipulation
import matplotlib.pyplot as plt  # Visualization

plt.rcParams['figure.figsize'] = [16, 10]
plt.rcParams['font.size'] = 14
plt.rcParams['font.weight'] = 'bold'
plt.style.use('seaborn-whitegrid')

df = pd.read_csv('Affairs.csv')
corr = df.corr()
sns.heatmap(corr, cmap='RdPu', annot=True)
plt.savefig(r'figures\correlation matrix.png', transparent=True)

plt.show()

# https://matplotlib.org/stable/tutorials/colors/colormaps.html
