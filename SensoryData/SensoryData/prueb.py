import pandas as pd

ruta = "SensoryData/Data/Data Energia_Combustible.xlsx"
df = pd.read_excel(ruta, engine="openpyxl")
print(df.head())  # Para ver las primeras filas del archivo
