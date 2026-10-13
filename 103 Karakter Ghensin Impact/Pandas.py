import pandas as pd

df = pd.read_csv("Genshin.csv")

df.head()
df.info()
df.isna().sum()
df.duplicated().sum()
print (df.shape)
print (df.head(3))
for col in ['rarity', 'weapon', 'element', 'region', 'is_standard_banner', 'is_archon']:
    print (df[col].value_counts(), "\n")

import ast

df = df.drop(columns=["Unnamed: 0"])


df["release_date"] = pd.to_datetime(df["release_date"])
df["release_year"] = df["release_date"].dt.year


df["banner_versions"] = df["banner_versions"].apply(ast.literal_eval)
df["n_banner_versions"] = df["banner_versions"].apply(len)


roles = df["roles"].str.get_dummies(sep=",")
df = pd.concat([df, roles], axis=1)

print(df.shape)
