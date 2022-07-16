# Exemplos de uso do módulo
# https://www.blog.pythonlibrary.org/2018/06/07/an-intro-to-pypdf2/

import PyPDF2
import os

caminho_pdf = r'C:\Users\andre\Documents\UTFPR\02-segundoPeriodo\EletricidadeMagnetismo'

"""
pdf_gerado = PyPDF2.PdfFileMerger()

for root, dirs, files in os.walk(caminho_pdf):
    for file in files:
        caminho_completo = os.path.join(root, file)
        
        arquivo_pdf = open(caminho_completo, 'rb')
        pdf_gerado.append(arquivo_pdf)
    
with open(f'{caminho_pdf}\\juncao_listas.pdf', 'wb') as novo_pdf:
    pdf_gerado.write(novo_pdf)
"""

with open(f'{caminho_pdf}\\juncao_listas.pdf', 'rb') as arquivo_pdf:
    leitor = PyPDF2.PdfFileReader(arquivo_pdf)
    num_paginas = leitor.getNumPages()
    
    for num_pagina in range(num_paginas):
        escritor = PyPDF2.PdfFileWriter()
        pagina_atual = leitor.getPage(num_pagina)
        escritor.addPage(pagina_atual)

        with open(f'{caminho_pdf}\\paginas\\{num_pagina}.pdf', 'wb') as novo_pdf:
            escritor.write(novo_pdf)
