import os
import shutil

caminho = r'C:\Users\andre\Documents\UTFPR\02-segundoPeriodo\EletricidadeMagnetismo'
new_caminho = r'C:\Users\andre\Documents\UTFPR\02-segundoPeriodo\EletricidadeMagnetismo2'

try:
    # cria o diretório caso ele não exista
    os.mkdir(new_caminho)
except FileExistsError as e:
    print(f'Pasta {new_caminho} já existe.')

for root, dirs, files in os.walk(caminho):
    for file in files:
        old_file_path = os.path.join(root, file)
        new_file_path = os.path.join(new_caminho, file)
        
        # move o arquivo. O primeiro parâmetro é a pasta de origem e o segundo
        # parâmetro é a pasta de destino
        # o move também pode ser usado para renomear os arquivos
        #shutil.move(old_file_path, new_file_path)
        #print(f'Arquivo {file} movido com sucesso.')
        
        if '.pdf' in file:
            # copia arquivo do caminho de origem para o caminho de destino
            shutil.copy(old_file_path, new_file_path)
            print(f'Arquivo {file} copiado com sucesso.')
        
        # apaga arquivos
        #if '.pdf' in file:
            #os.remove(new_file_path)
