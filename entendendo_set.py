# Set
# O set é uma coleção que não aceita duplicatas 

numeros = [2, 2, 5, 8]
frutas = {'maça', 'banana', 'uva', 'maça', 'morango'}
# Convertendo para set
set_numeros = set(numeros)
set_frutas = set(frutas)

# Ele exclui os valores repetidos na coleção
print(set_numeros)
print(set_frutas)

# Adicionando valores no set
set_numeros.add(10)
print(set_numeros)

# Conjuntos 
numeros_1 = [2, 2, 5, 8]
numero_2 = [2, 2, 3, 9]

a = set(numeros_1)
b = set(numero_2)

# Mostra os numeros que não se encontra nas duas coleções
print(a.symmetric_difference(b))

# Mostra somente os números que estam presente em ambos
print(a.intersection(b))

# Unir as duas coleções sem duplicatas
print(a.union(b))