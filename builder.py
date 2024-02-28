class Veiculo:
    def __init__(self, modelo, motor, cor):
        self.modelo = modelo
        self.motor = motor
        self.cor = cor

class Carro(Veiculo):
    def __init__(self, motor, cor):
        super().__init__("Carro", motor, cor)

class Motocicleta(Veiculo):
    def __init__(self, motor, cor):
        super().__init__("Moto", motor, cor)

class Caminhao(Veiculo):
    def __init__(self, motor, cor):
        super().__init__("Caminhão", motor, cor)

carro_grife = Carro("1.0", "Vermelha")
moto_grife = Moto("1.0", "Amarela")
caminhao_grife = Caminhao("2.0", "Preta")

print(f"Modelo: {carro_grife.modelo}, Motor: {carro_grife.motor}, Cor: {carro_grife.cor}")
print(f"Modelo: {moto_grife.modelo}, Motor: {moto_grife.motor}, Cor: {moto_grife.cor}")
print(f"Modelo: {caminhao_grife.modelo}, Motor: {caminhao_grife.motor}, Cor: {caminhao_grife.cor}")