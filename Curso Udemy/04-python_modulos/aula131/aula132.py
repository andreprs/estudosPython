# datetime parte 2
from datetime import datetime
from locale import setlocale, LC_ALL
from calendar import mdays

setlocale(LC_ALL, 'pt_BR.utf-8')  # set da localida para o Brasil
                                  # de forma explícita

data = datetime.now()
mes_atual = int(data.strftime('%m'))
formatacao = data.strftime('%A, %d de %B de %Y')
print(formatacao)
print(mdays[mes_atual])  # retorna o ultimo dia do mês indicado
