import os
import fnmatch
import sys

comando_ffmpeg = r'C:\cursopython\aula136\ffmpeg\bin\ffmpeg.exe'

codec_video = '-c:v libx264'
crf = '-crf 23'
preset = '-preset ultrafast'
codec_audio = '-c:a aac'
bitrate = '-b:a 320k'
debug = '-ss 00:00:00 -to 00:00:25'

caminho_origem = r'C:\Users\andre\Videos'
caminho_destino = r'C:\Users\andre\Desktop'

for raiz, pastas, arquivos in os.walk(caminho_origem):
    for arquivo in arquivos:
        if not fnmatch.fnmatch(arquivo, '*.mp4'):
            continue
        
        caminho_completo = os.path.join(raiz, arquivo)
        nome_arquivo, extensao_arquivo = os.path.splitext(caminho_completo)
        
        nome_arquivo, extensao_arquivo = os.path.splitext(arquivo)
        
        arquivo_saida = f'{caminho_destino}\{nome_arquivo}_NOVO{extensao_arquivo}'
        
        comando = f'{comando_ffmpeg} -i "{caminho_completo}" {codec_video} {crf} {preset} {codec_audio} {bitrate} {debug} "{arquivo_saida}"'
        
        os.system(comando)
