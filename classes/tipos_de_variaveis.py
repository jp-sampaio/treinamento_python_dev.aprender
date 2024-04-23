# Tipos de variaveis em uma classe
class Computador:
    sistema_operacional = 'Windows 10'

    def __init__(self, marca, memoria_ram, placa_de_video):
        self.marca = marca
        self.memoria_ram = memoria_ram
        self.placa_de_video = placa_de_video

    def ligar(self):
        print('Ligar o computador!!')

# Modificar a variavél sem precisar criar uma nova instancia, todas as novas instancias vão receber essa nova informação
Computador.sistema_operacional = 'Linux'

computador1 = Computador('Asus', '16gb', 'Nvidia')
print(computador1.marca)
print(computador1.memoria_ram)
print(computador1.placa_de_video)

print(computador1.sistema_operacional)