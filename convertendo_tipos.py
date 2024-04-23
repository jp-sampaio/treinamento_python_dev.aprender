# Convertendo tipos de dados 
idade = input('Digite a sua idade ')
print(int(idade) > 17)

ano_publicação = 2020
print('Este livro foi criado em ' + str(ano_publicação))

altura = input('Altura da parede: ')
print(float(altura) > 2.50)

# Convertendo entre coleções
saudacao = 'Hello!'
print(list(saudacao))
print(set(saudacao))
print(tuple(saudacao))
print(list(range(10)))

numeros = [10, 20, 20, 30]
print(tuple(numeros))
print(set(numeros))
print(type(numeros))