from ingresso import Ingresso


class IngressoVip(Ingresso):
    def __init__(self, valor, adicional) -> None:
        Ingresso.__init__(self, valor + adicional)

