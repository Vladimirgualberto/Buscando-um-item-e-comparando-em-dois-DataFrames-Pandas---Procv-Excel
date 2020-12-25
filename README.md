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

![alt tag](https://github.com/Vladimirgualberto/Buscando-um-item-e-comparando-em-dois-DataFrames-Pandas---Procv-Excel/blob/main/img/compara%C3%A7%C3%A3o.png?raw=true)

As colunas devem ter o mesmo nome!

Como seria essa busca sem utilizar a biblioteca do Pandas ou outra biblioteca do Python? utilizando um for encadeado, por exemplo.


Abrindo o Arquivo A:
df = pd.read_csv(r"Caminho do arquivo.csv")

Abrindo o Arquivo B:
df1 = pd.read_excel(r"Caminho do arquivo.xlsx")

Neste exemplo criei uma coluna 'Existe' dentro do primeiro dataframe


# Markdown
```
for i in df['Coluna que quero buscar']:

    for j in df1['Coluna que quero buscar ou comparar']:
    
       if i == j:
       
        df.loc[i,'Existe'] = 'Existe'
        
        break
        
       else:
       
           df.loc[i,'Existe'] = 'Não Existe'
```
