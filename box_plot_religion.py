import seaborn as sns
import pandas as pd  # Data manipulation
import matplotlib.pyplot as plt  # Visualization
from group_by_age import cat_order

plt.rcParams['figure.figsize'] = [16, 10]
plt.rcParams['font.size'] = 14
plt.rcParams['font.weight'] = 'bold'
plt.style.use('seaborn-whitegrid')

df = pd.read_csv('Affairs.csv')


f = plt.figure(figsize=(14, 6))
ax = f.add_subplot(121)
sns.boxplot(x='age_group', y='affairs', data=df, palette='RdPu', ax=ax, order=cat_order, showfliers=False, hue='children')
ax.set_title('Box plot of affairs vs age group distinguished by children')
plt.xlabel('Age groups')
plt.savefig(r'figures\box plot affairs vs age group Distinguished whether children.png', transparent=True)

plt.show()