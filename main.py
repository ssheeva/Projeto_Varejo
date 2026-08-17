import pandas as pd

df = pd.read_csv("varejo.csv", sep=";")
#print(df.shape)
#print(df.dtypes)
#print(df.head())

#print(df.isna().sum())
#print(df.duplicated().sum())
#print(df["PR_CAT"].value_counts(dropna=False))

df = df.dropna(axis=1, how="all")

df["PR_CAT"] = df["PR_CAT"].fillna("Sem Categoria")
df["PR_CAT"] = df["PR_CAT"].str.strip().replace("#N/D", "Sem Categoria")

df = df.drop_duplicates(

).copy()

df["DATA"] = pd.to_datetime(
    df["DATA"], format="%d/%m/%Y", errors="coerce"
)

df.to_csv("varejo_limpo.csv", index=False, encoding="utf-8-sig")

#filhos

filhos = df["CL_FHL"]
print(filhos.mean())
print(filhos.median())
print(filhos.mode().iloc[0])
print(filhos.quantile([0.25, 0.50, 0.75]))