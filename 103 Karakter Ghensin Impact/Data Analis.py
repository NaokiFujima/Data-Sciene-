import pandas as pd

df = pd.read_csv("103 Karakter Ghensin Impact/Genshin.csv")

print(df.shape)
df.head()
df.info()
df.isna().sum()
df.duplicated().sum()
print (df.shape)

for col in ['rarity', 'weapon', 'element', 'region', 'is_standard_banner', 'is_archon']:
    print (df[col].value_counts(), "\n")