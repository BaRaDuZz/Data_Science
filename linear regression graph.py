import seaborn as sns
import pandas as pd  # Data manipulation
import matplotlib.pyplot as plt  # Visualization

plt.rcParams['figure.figsize'] = [16, 10]
plt.rcParams['font.size'] = 14
plt.rcParams['font.weight'] = 'bold'
plt.style.use('seaborn-whitegrid')

df = pd.read_csv('Affairs.csv')

sns.lmplot(x='affairs', y='age', data=df, aspect=2, height=6)
plt.xlabel('Affairs: as Independent variable')
plt.ylabel('Age: as Dependent variable')
plt.title('Affairs Vs Age')
plt.savefig(r'figures\linear regression graph.png', transparent=True)

plt.show()