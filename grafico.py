import matplotlib as plt
import pandas as pd

df = pd.read_csv("varejo_limpo.csv")


compras_por_genero.plot(kind="bar")
plt.title("Compras únicas por gênero")
plt.tight_layout()
plt.savefig("resultados/compras_por_genero.png")

