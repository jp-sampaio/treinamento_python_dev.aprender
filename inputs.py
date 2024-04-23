# Recebendo os dados do usuário
# Posso receber informações do usuário com o input e armazenar em variáveis, 
# lembrando que o input sempre retorna uma string e preciso converter para o 
# tipo de dado que eu quero.

# Exemplo:
# nome = input("Digite seu nome: ")
# Exemplo de conversão de string para inteiro:
# idade = int(input("Digite sua idade: "))
# Exemplo de conversão de string para float:
# altura = float(input("Digite sua altura: "))

name = input('Digite seu nome: ')
print(name)
age = int(input('Digite sua idade: '))
print(age)
height = input('Digite sua altura: ')
# Tratamento do dado caso a pessoa insira uma virgula no lugar do ponto
if ',' in height:
  height = height.replace(',', '.')
# Converte a string para float
height = float(height)
print(height)
print(type(height))