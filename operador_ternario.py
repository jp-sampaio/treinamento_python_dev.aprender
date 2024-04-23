# Se uma pessoa tiver 18 anos eu mais de idade, então ela é maior de idade, senão ela é menor de idade

idade = 17
print('Maior de idade.') if idade >= 18 else print('Menor de idade')

# Uma pessoa só pode embacar caso ela tenha um passaporte, caso contrário ela não pode viajar

possui_passaporte = True
print('Pode embarcar') if possui_passaporte else print('Não pode embarcar')

# DESAFIO 🥇
# uso expressão condicional(operador ternário) para criar a seguinte condição
# se velocidade estiver acima de 100 exibir, você foi multado, caso contrário exiba siga em frente

speed = 101

print('Siga em frente') if speed <= 100 else print('Você foi multado')