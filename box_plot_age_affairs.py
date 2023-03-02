import seaborn as sns
import pandas as pd  # Data manipulation
import matplotlib.pyplot as plt  # Visualization
from group_by_age import cat_order

plt.rcParams['figure.figsize'] = [16, 10]
plt.rcParams['font.size'] = 14
plt.rcParams['font.weight'] = 'bold'
plt.style.use('seaborn-whitegrid')

df = pd.read_csv('Affairs.csv')

df['children'] = df['children'].apply(lambda x: 'yes' if x == 1 else 'no')

f = plt.figure(figsize=(14, 6))
ax = f.add_subplot(121)
sns.boxplot(x='religiousness', y='affairs', data=df, palette='RdPu', ax=ax, showfliers=False)
ax.set_title('Box plot of affairs vs religiousness')
plt.xlabel('Religiousness')
plt.savefig(r'figures\box plot affairs vs religiousness.png', transparent=True)

plt.show()