import pandas as pd

import numpy as np
import openpyxl
##Local lib


df = pd.read_csv(r"Caminho do arquivo.csv")
df1 = pd.read_excel(r"Caminho do arquivo.xlsx")
df = df.rename(columns={'dst': 'TELEFONE'})
df =df.drop(columns=['realsrc'])

df=df.merge(df1, on=['TELEFONE'], how='outer', suffixes=['', '_'], indicator=True)

df = df.rename(columns={'_merge': 'Existe em Qual Local?'})
df["Existe em Qual Local?"] = df["Existe em Qual Local?"].replace(['left_only'], 'Encontrado apenas na Nextip')
df["Existe em Qual Local?"] = df["Existe em Qual Local?"].replace(['both'], 'Existe nos dois')
df["Existe em Qual Local?"] = df["Existe em Qual Local?"].replace(['right_only'], 'Encontrado apenas no Syonet')


df.to_excel("comparativo.xlsx")



