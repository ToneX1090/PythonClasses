class Carro(object):
    def __init__(self, nome, estado):
        self.nome = nome
        self.estado = estado

    def printar(self):
        print(f"O carro {self.nome} tem o estado de {self.estado}")

bmw = Carro("BMW", "Novo")
ferrari = Carro("Ferrari", "Semi-novo")
fusca = Carro("Fusca", "Usado")

bmw.printar()
ferrari.printar()
fusca.printar()