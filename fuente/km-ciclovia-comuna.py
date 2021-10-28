# coding: utf-8
import pandas as pd
import geopandas as gpd
from pathlib import Path

archivo = Path("entrada/visor-territorial/ciclovias.shp")
df = gpd.read_file(archivo)
df.columns = df.columns.str.lower()

# crea un dataframe con ciclovías existentes
dfs = df[df.estado_rec == "Existente"]

# agrupa las ciclovías por comuna y kilómetros de ciclovías
tabla = dfs.groupby("comuna")["km"].sum()

# df.groupby(["comuna", "estado_rec"])["km"].sum()

# guarda la tabla en salida/producto-1
tabla.to_csv("salida/producto-1/km-ciclovia-comuna.csv")

print("fin")
