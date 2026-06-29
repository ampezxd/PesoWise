import json
import pandas as pd

with open('trm_historico.json', 'r') as f:
    data = json.load(f)

df = pd.DataFrame(data)[["vigenciadesde", "vigenciahasta", "valor", "unidad"]]
df["fecha"] = pd.to_datetime(df["vigenciadesde"]).dt.date
df["trm"] = df["valor"].astype(float)
df = df[["fecha", "trm", "unidad"]].sort_values("fecha")

df.to_csv('trm_historico.csv', index=False)