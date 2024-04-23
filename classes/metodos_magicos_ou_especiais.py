# Métodos Mágicos (Magic Methods, dunder methods(double underscore))

class Pessoa:
    # Inicializa a classe
    def __init__(self):
        self.nome = 'Sou uma pessoa'
        self.habilidades = ['Habilidade 1', 'Habiliade 2', 'Habilidade 3']

    # Representação para programadores(chamado com método repr(pessoa))
    def __repr__(self):
        return 'Classe Pessoa com propriedades nome e habilidades'
    
    # O que deve ser mensurado para determinar a quantidade daquela classe(chamada com o método(len(pessoa)))
    def __len__(self):
        return len(self.habilidades)
    
    # Retorna a classe como uma string 
    def __str__(self):
        return f'{self.nome} com as habilidades {self.habilidades}'
    
pessoa = Pessoa()
print(pessoa.nome) # __init__
print(repr(pessoa)) # __repr__
print(len(pessoa)) # __len__
print(pessoa) # __str__
print(dir(pessoa)) # Retorna todas os métodos especiais 