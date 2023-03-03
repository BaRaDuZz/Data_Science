import seaborn as sns
import pandas as pd  # Data manipulation
import matplotlib.pyplot as plt  # Visualization

plt.rcParams['figure.figsize'] = [20, 12]
plt.rcParams['font.size'] = 12
plt.rcParams['font.weight'] = 'bold'
plt.tight_layout()

df = pd.read_csv('Affairs.csv')

sns.lmplot(x='yearsmarried', y='affairs', data=df, aspect=2, height=8, line_kws={'color': '#FFAEB8'}, scatter_kws={'color': '#FF6275'})
plt.xlabel('Yearsmarried: as Independent variable')
plt.ylabel('Affairs: as Dependent variable')
plt.title('Affairs Vs Yearsmarried')
plt.savefig(r'figures\linear regression graph.png', transparent=True)

plt.show()