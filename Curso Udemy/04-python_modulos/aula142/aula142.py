from zipfile import ZipFile
import os

caminho = r'C:\Users\andre\Documents\UTFPR\02-segundoPeriodo\EletricidadeMagnetismo'

# criação do arquivo zip + colocar os arquivos dentro
with ZipFile('arquivo.zip', 'w') as zip:
    for arquivo in os.listdir(caminho):
        caminho_completo = os.path.join(caminho, arquivo)
        zip.write(caminho_completo, arquivo)
        # aqui o primeiro parâmetro indidca o caminho onde o arquivo está
        # e o segundo parâmetro o nome desejado para o arquivo (somente o 
        # nome, não a estrutura completa de diretórios)

with ZipFile ('arquivo.zip', 'r') as zip:
    for arquivo in zip.namelist():
        print(arquivo)

# extração do arquivo zip
with ZipFile('arquivo.zip', 'r') as zip:
    zip.extractall('descompactado')