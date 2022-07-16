from aula112.eletronico import Escritor, Caneta, MaquinaDeEscrever

escritor = Escritor('Ronaldo')
caneta = Caneta('Bic')
maquina = MaquinaDeEscrever()

escritor.ferramenta = maquina  # Aqui é como se toda a classe fosse enviada para o atributo __ferramenta
# Esse tipo de associação é o mais fraco, pois se uma classe for excluída, as outras ainda poderão ser usadas depois
escritor.ferramenta.escrever()
