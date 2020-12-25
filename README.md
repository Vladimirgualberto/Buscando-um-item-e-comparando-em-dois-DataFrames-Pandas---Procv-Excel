# Buscando-um-item-e-comparando-em-dois-DataFrames-Pandas---Procv-Excel
Comparando-dois-DataFrames-Pandas - Procv Excel

Como encontra um item em uma coluna de um dataframe e buscar esse item em outra coluna de um dataframe diferente?
É algo similar ao procv do excel, dessa forma iremos pegar um item ou mais de uma coluna no dataframe A e busca-los em uma coluna do dataframe B. Iremos marcar em uma outra coluna chamada _merge onde aquele item foi encontrado.

Abrindo o Arquivo A:
df = pd.read_csv(r"Caminho do arquivo.csv")

Abrindo o Arquivo B:
df1 = pd.read_excel(r"Caminho do arquivo.xlsx")

Executando a busca utilizando um merge dos arquivos:
df=df.merge(df1, on=['Coluna que quero buscar'], how='outer', suffixes=['', '_'], indicator=True)

As colunas devem ter o mesmo nome!
