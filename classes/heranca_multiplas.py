# Herança Multiplas
class Pessoa:
    nome = 'Sou uma pessoa'

    def convidar(self):
        print('Olá sou uma pessoa, vamos ao evento?')

class Profissional:
    nome = 'Sou um profissional'

    def convidar(self):
        print('Olá sou um profissinal, vamos ao evento?')

class AtorProfissional(Pessoa, Profissional):
    pass

ator_profissonal = AtorProfissional()
# Mostra a primeira class
print(ator_profissonal.nome)
ator_profissonal.convidar()

print(AtorProfissional.mro())
# [<class '__main__.AtorProfissional'>, <class '__main__.Pessoa'>, <class '__main__.Profissional'>, <class 'object'>]