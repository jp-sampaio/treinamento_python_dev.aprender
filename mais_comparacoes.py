# Operações de comparação com mais de uma condição utilizamos os operadores lógicos.
# and
# or
# not

# O operador and retorna True se ambos os valores forem True
# O operador or retorna True se um dos valores for True
# O operador not inverte o valor de um operando, retornando o inverso

# Vamos pensar no seguinte exemplo a seguir:
# age = 21
# # Vamos verificar se a idade é maior que 18 e menor que 30
# print(age > 18 and age < 30)
# # Vamos verificar se a idade é maior que 18 ou menor que 30
# print(age > 18 or age < 30)
# # Vamos verificar se a idade não é maior que 18
# print(not age > 18)

# possui_convite = False
# filho_do_dono = True

# # Só informando a variável possui_convite já mostra que quero saber se é true
# print(age == 21 and possui_convite)
# print(age == 21 or possui_convite)
# # Idade igual a 21 anos e tiver convite ou seja filho do dono
# print(age == 21 and possui_convite or filho_do_dono)
# # Idade igual a 21 anos e tiver convite e não ser filho do dono
# print(age == 21 and possui_convite and not filho_do_dono)

# print(not possui_convite) # Inverte os valores

#  Precedencia de operadores em python
#  1. ()
#  2. **
#  3. *, /, //, %
#  4. +, -
#  5. ==, !=, <, >, <=, >=, is, is not, in, not in
#  6. not
#  7. and
#  8. or

# Outro exemplo
# maior_de_idade = True
# possui_carteira_de_trabalho = True
# esta_trabalhando_atualmente = True
# possui_veiculo_proprio = False

# # Vamos verificar se a pessoa é maior de idade, possui carteira de trabalho,
# print(maior_de_idade and possui_carteira_de_trabalho)

# # Queremos contratar pessoas que não tenha veículo próprio mais já tenha carteira
# # de trabalho
# print(possui_carteira_de_trabalho and not possui_veiculo_proprio)


# ​ Desafio 🥇

# '''

# Quero que você defina as seguintes variáveis, inicialmente todas como False,
# a ideia aqui não é de se importar com os valores dentro dessas variáveis, 
# mas sim como montar condicionais.

# possui_passaporte = False

# passagem_comprada = False

# menor_de_idade = False

# E Crie as seguintes condições usando o que acabou de ver e imprima o resultado na tela
# Tente fazer cada condição e depois veja a solução no final deste aula.

# 1º Uma pessoa só pode viajar se possuir  passaporte e tiver a passagem comprada e não 
# for menor de idade

# 2º Uma pessoa só pode viajar se possuir passaporte ou tiver a passagem comprada e não 
# for menor de idade

# 3º Uma pessoa só pode viajar se não possuir passaporte ou tiver a passagem comprada e 
# não for menor de idade

# 4º Uma pessoa não pode viajar se não possuir passaporte ou não tiver a 
# passagem comprada e for menor de idade

possui_passaporte = False
passagem_comprada = False
menor_de_idade = False

# condição 1
print((possui_passaporte and passagem_comprada) and not menor_de_idade)

# Condição 2
print((possui_passaporte or passagem_comprada) and not menor_de_idade)

# Condição 3 
print((not possui_passaporte or passagem_comprada) and not menor_de_idade)

# Condição 4
print((not possui_passaporte or not passagem_comprada) and menor_de_idade)