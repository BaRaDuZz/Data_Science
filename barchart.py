import pandas as pd  # Data manipulation
import numpy as np  # Data manipulation
import matplotlib.pyplot as plt  # Visualization
import seaborn as sns  # Visualization

plt.rcParams['figure.figsize'] = [16, 10]
plt.rcParams['font.size'] = 14
plt.rcParams['font.weight'] = 'bold'
plt.style.use('seaborn-whitegrid')

df = pd.read_csv('Affairs.csv')

colors = ['pink', 'red']

male_count = 0
female_count = 0

for x in df.index:

    if (df['gender'][x] == 0):
        if (df['affairs'][x]) > 0:
            male_count += 1

    if (df['gender'][x] == 1):
        if (df['affairs'][x]) > 0:
            female_count += 1

print(male_count, female_count)

male_proz = male_count * 100 / 3146
female_proz = female_count * 100 / 3465

print(male_proz, female_proz)


plt.bar(['Men', 'Women'], [male_proz, female_proz], width=0.5, color=colors)

# Set x-axis limit to start at 0
plt.xlim()
plt.ylim(top=50)

# Add labels and title
plt.xlabel('Gender')
plt.ylabel('Percentage with Affairs')
plt.title('Percentage of married men and women having affairs')

plt.text(0, male_proz, f'{male_proz:.2f}%', ha='center', va='bottom', fontsize=12)
plt.text(1, female_proz, f'{female_proz:.2f}%', ha='center', va='bottom', fontsize=12)
plt.savefig(r'figures\Percentage of married men and women having affairs.png', transparent=True)

# Show chart
plt.show()
