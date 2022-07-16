from conta_poupanca import ContaPoupanca
from conta_corrente import ContaCorrente

cp = ContaPoupanca(2222, 9999, 0)
cp.depositar(10)
cp.sacar(5)
cp.sacar(5)
cp.sacar(1)
print('++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++')
cc = ContaCorrente(1111, 3333, 0, 500)
cc.depositar(100)
cc.sacar(250)
cc.sacar(500)
cc.depositar(1000)

