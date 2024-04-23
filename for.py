# Caso queira repetir algo mais de uma vez 

for numero in range(1, 20, 2): # Começa no 0 e não conta o último número
    print('Carregando', numero)

names = ['john', 'Paul', 'Joe', 'Mark', 'Karl']

for name in names:
    print(name)


# Desafio 1  🥇
# Usando um loop, exiba na tela: Estamos em X
# onde x é um valor iniciando em 18 e finalizando em 110
# Desafio 2
# Você precisa de 10 passos para finalizar uma tarefa, exiba na tela, usando loop for a seguinte frase
    
# Desafio 1
for number in range(18, 111):
    print('Estamos em', number)

# Desafio 2
for step in range(1, 11):
    print(f'Realizando o passo {step}')
