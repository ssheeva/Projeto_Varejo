import pandas as pd

df = pd.read_csv("varejo.csv", sep=";")
print(df.shape)
print(df.dtypes)
print(df.head())

#print(df.isna().sum())
#print(df.duplicated().sum())
#print(df["PR_CAT"].value_counts(dropna=False))

#df = df.dropna(axis=1, how="all")

#df["PR_CAT"] = df["PR_CAT"].fillna("Sem Categoria")
#df["PR_CAT"] = df["PR_CAT"].str.strip().replace("#N/D", "Sem Categoria")

df = df.drop_duplicates().copy()

df["DATA"] = pd.to_datetime(
    df["DATA"], format="%d/%m/%Y", errors="coerce"
)