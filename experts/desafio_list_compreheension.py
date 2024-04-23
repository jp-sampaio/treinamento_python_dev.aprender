# Desafio 1
# Usando a lista compreheension, crie a seguinte lista:
# [2, 4, 6, 8, 10]

first_list = [number for number in range(1, 11) if number % 2 == 0]
# print(first_list)

# =============================================================================================


# Desafio 2
# Use a seguinte lista como base:
colors = ['vermelho','azul','verde','amarelo','rosa','preto']
# Para criar a lista a seguir:
# ['1 - vermelho','2 - azul','3 - verde','4 - amarelo','5 - rose','6 - preto']

color_numbering = [f'{index} - {color}' for index, color in enumerate(colors, start=1)]
# print(color_numbering)

# Outra forma de fazer esse mesmo processo 
color_numbering_2 = [str(colors.index(color) + 1) + ' - ' + color for color in colors]
print(color_numbering_2)

# ==============================================================================================

# Desafio 3 
# Usando a lista a seguir como base:
participantes = ['joel','jessica','maria','cris','Larissa','rafael','marcus','john']
pagamento_realizado = ['joel','jessica','maria','cris']
'''
    Concatene(adicione) a palavra 'PAGO' aos nomes da lista 'participantes' usando condicionais somente nos casos onde seu nome esteja na lista 'pagamento_realizado'. O resultado final deve ser como a lista a seguir:
'''
# ['joel PAGO','jessica PAGO','maria PAGO','cris PAGO','Larissa','rafael','marcus','john']

pagantes = [nome + ' PAGO' if nome in pagamento_realizado else nome + '' for nome in participantes]
print(pagantes)