import seaborn as sns
import pandas as pd  # Data manipulation
import matplotlib.pyplot as plt  # Visualization

plt.rcParams['figure.figsize'] = [16, 10]
plt.rcParams['font.size'] = 14
plt.rcParams['font.weight'] = 'bold'
plt.style.use('seaborn-whitegrid')

df = pd.read_csv('Affairs.csv')

f = plt.figure(figsize=(14, 6))
ax = f.add_subplot(121)
sns.violinplot(x='rating', y='affairs', data=df, palette='RdPu', ax=ax, left=0.053, bottom=0.244, right=1, top=0.825)
ax.set_title('Violin plot of affairs vs rating')
plt.savefig(r'figures\violin plot affairs vs rating.png', transparent=True)

plt.show()