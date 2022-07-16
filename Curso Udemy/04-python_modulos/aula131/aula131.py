from datetime import datetime, timedelta

data = datetime(2022, 7, 13, 8, 39, 10)
# ano - mês - dia - hora - minuto - segundo
# os dados de hora são opicionais caso a data seja instanciada
print(data)  # data em formato americano
print(data.strftime('%d/%m/%Y - %H:%M:%S'))  # maneira de fazer a formatação BR
    # Isso são diretivas dos formatos, é possível ver mais sobre na doc
    
data = datetime.strptime('13/07/2022', '%d/%m/%Y')
print(data)

seg = data.timestamp()  # conta os segundos desde 01/01/1970 até a data info.
print(datetime.fromtimestamp(seg))  #  função que converte timestamp em data

data = datetime.strptime('20/04/1987 20:00:00', '%d/%m/%Y %H:%M:%S')
data += timedelta(days=5, seconds=37)  # faz acrescimos nos parâmetros
                                       # aceita cálculos
print(data.strftime('%d/%m/%Y %H:%M:%S'))

d1 = datetime.strptime('19/04/1987 20:00:00', '%d/%m/%Y %H:%M:%S')
d2 = datetime.strptime('23/04/1987 16:56:00', '%d/%m/%Y %H:%M:%S')
dif = d2 - d1
print(dif)  # mostra a diferença entre as datas (qualquer parâmetro)
            # aceita .days, .seconds, .total_seconds, etc.
            # retorno somente em números