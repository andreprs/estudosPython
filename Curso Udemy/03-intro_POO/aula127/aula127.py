from dataclasses import dataclass


# Parâmetro frozen pode ser usado para criar uma classe imutável (perfeito para isso)
@dataclass(eq=False, repr=False, order=False)  # Esses parâmetros por padrão são setados como True
class Pessoa:                                  # Setá-los como False garante que eles não vão ser usados caso queira criar método próprio
    nome: str
    sobrenome: str

    @property
    def nome_completo(self):
        return f'{self.nome} {self.sobrenome}'


p1 = Pessoa('Andre', 'Prasel')
print(p1)
