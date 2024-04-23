# Polimorfismo
# A principal característica do polimorfismo é a sua adaptabilidade e poder ter diferentes resultados em classes diferentes

class Pessoa():
    # Quando eu adiciono o none a declaração do parâmetro é opcional
    def apresentar(self, nome, idade=None, profissao=None):
        if idade and profissao != None:
            print(f'{nome}, {idade}, {profissao}')
        elif idade != None:
            print(f'{nome}', {idade})
        elif profissao != None:
            print(f'{nome}, {profissao}')
        else:
            print(nome)

# Se adapta nos diferentes cenarios que foram proposto abaixo
pessoa = Pessoa()
pessoa.apresentar(nome='Joana')
pessoa.apresentar(nome='Maria', profissao='Programadora')
pessoa.apresentar(nome='Maria', idade=45, profissao='Programadora')
pessoa.apresentar(nome='Maria', idade=45,)