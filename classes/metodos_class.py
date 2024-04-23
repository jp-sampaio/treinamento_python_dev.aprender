# Métodos são funcionalidades de uma class 
class Computador:
    def __init__(self, marca, memoria_ram, placa_de_video):
        self.marca = marca 
        self.memoria_ram = memoria_ram
        self.placa_de_video = placa_de_video

    def ligar(self):
        print('Estou ligando o computador')

    def desligar(self):
        print('Estou desligando o computador')

    def exibir_informacoes_do_computador(self):
        print(f'Computador da marca {self.marca}, com {self.memoria_ram} de memória ram e que usa a placa de vídeo {self.placa_de_video}')

marca = input('Informe a marca do seu computador: ')
memoria_ram = input('Informe a memória ram do seu computador: ')
placa_de_video = input('Informe a placa de vídeo do seu computador: ')

computador1 = Computador(marca, memoria_ram, placa_de_video)
computador1.ligar()
computador1.desligar()
computador1.exibir_informacoes_do_computador()