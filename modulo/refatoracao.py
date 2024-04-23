# Refatoração
# Renomear todas as ocorrências com o F2
class Calculadora():
    pass

calc1 = Calculadora()
calc2 = Calculadora()
calc3 = Calculadora()

# Extrair uma função (Ctrl + Shift + R => Extract Method ou o atalho em)
def adicao():
    resultado = 10 + 49
    return resultado

print(adicao())


# Extrair Variavel (Ctrl + Shift + R => Extract Variable ou o atalho ev)

comprimento = 60
idade = 2
tamanho = (comprimento / idade) + 50
