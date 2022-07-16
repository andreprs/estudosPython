from bank import Banco
from cliente import Cliente
from accounts import ContaPoupanca, ContaCorrente

banco = Banco()
cliente1 = Cliente('Andre Prasel', 20)
cliente2 = Cliente('João da Silva', 45)
cliente3 = Cliente('Maria Santos', 34)

conta1 = ContaCorrente(1000, 696969, 0)
conta2 = ContaPoupanca(3000, 454647, 0)
conta3 = ContaPoupanca(2000, 122334, 0)

banco.inserir_conta(conta2)
banco.inserir_clientes(cliente2)
banco.inserir_conta(conta3)
banco.inserir_clientes(cliente3)

cliente1.inserir_conta(conta1)
cliente2.inserir_conta(conta2)
cliente3.inserir_conta(conta3)

if banco.verificar(cliente3):
    cliente3.conta.depositar(30)
    cliente3.conta.sacar(20)
else:
    print('Cliente não autenticado!')

if banco.verificar(cliente2):
    cliente2.conta.depositar(30)
    cliente2.conta.sacar(20)
else:
    print('Cliente não autenticado!')
