from abc import ABC, abstractmethod

class Forma(ABC):
    @abstractmethod
    def clone(self):
        pass

class Circulo(Forma):
    def __init__(self, raio):
        self.raio = raio

    def clone(self):
        return Circulo(self.raio)

class Retangulo(Forma):
    def __init__(self, largura, altura):
        self.largura = largura
        self.altura = altura

    def clone(self):
        return Retangulo(self.largura, self.altura)

class Triangulo(Forma):
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura

    def clone(self):
        return Triangulo(self.base, self.altura)

if __name__ == "__main__":
    circulo_definido = Circulo(raio=5)
    circulo2 = circulo_definido.clone()

    print(f"Raio do círculo original: {circulo_definido.raio}")
    print(f"Raio do círculo clonado: {circulo2.raio}")