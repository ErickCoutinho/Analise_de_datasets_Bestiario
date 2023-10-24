import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

data = 'd20pfsrd-Bestiary - Updated 23Feb2014.csv'
df_path = pd.read_csv(data)


'CORRELAÇÃO ENTRE ATRIBUTOS'
###########################################################################
columns_to_replace = ['Str', 'Dex', 'Con', 'Int', 'Wis', 'Cha']
for col in columns_to_replace:
    df_path[col] = df_path[col].replace('-', np.nan)
############################################################################

import seaborn as sns
atributos_principais = ['Str', 'Dex', 'Con', 'Int', 'Wis', 'Cha']
correlacao_atributos = df_path[atributos_principais].corr()
# Plotar um mapa de calor da matriz de correlação
plt.figure(figsize=(8, 6))
sns.heatmap(correlacao_atributos, annot=True, cmap='coolwarm', linewidths=1)
plt.title('Matriz de Correlação entre Atributos Principais')
plt.show()
print(correlacao_atributos)




"XP obtido por nivel de CR"
###################################################################
df_path['XP'] = df_path['XP'].str.replace(',', '').astype(float)
###################################################################
# Filtrar o DataFrame para incluir apenas CR de 1 a 12
df_filtrado = df_path[df_path['CR'].between(1, 12)]

media_xp_por_cr = df_filtrado.groupby('CR')['XP'].mean()
plt.figure(figsize=(12, 6))
media_xp_por_cr.plot(kind='bar', color='red', alpha=0.7)
plt.xlabel('CR')
plt.ylabel('Média de XP')
plt.title('Média de XP por CR (CR de 1 a 12)')
plt.xticks(rotation=0)
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.tight_layout()
plt.show()




