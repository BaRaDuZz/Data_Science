import seaborn as sns
import pandas as pd  # Data manipulation
import matplotlib.pyplot as plt  # Visualization

df = pd.read_csv('Affairs.csv')

df['age_group'] = pd.cut(df['age'], bins=[18, 25, 30, 35, 40, 45, 50, 55, 60], labels=['18-25', '26-30', '31-35', '36-40', '41-45', '46-50', '51-55', '56-60'])

df['age_group'] = df['age_group'].astype('category')

cat_order = ['18-25', '26-30', '31-35', '36-40', '41-45', '46-50', '51-55', '56-60']
df['age_group'] = df['age_group'].cat.reorder_categories(cat_order)

df.to_csv('Affairs.csv', index=False)