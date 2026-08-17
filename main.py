import pandas as pd

df = pd.read_csv("varejo.csv", sep=";")
print(df.shape)
print(df.dtypes)
print(df.head())