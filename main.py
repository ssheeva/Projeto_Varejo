import pandas as pd

df = pd.read_csv("varejo.csv", sep=";")
print(df.shape)
print(df.dtypes)
print(df.head())

print(df.isna().sum())
print(df.duplicated().sum())
print(df["PR_CAT"].value_counts(dropna=False))

df = df.dropna(axis=1, how="all")
