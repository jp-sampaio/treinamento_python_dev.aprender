from carro import ligar_carro
from moto import ligar_moto

ligar_carro()
ligar_carro()

# Só vai executar caso seja chamado diretamente e por isso o arquivo recebe o nome de main
if __name__ == '__main__':
    print('Ligando veiculos')
    print(f'Estamos no arquivo {__name__}')