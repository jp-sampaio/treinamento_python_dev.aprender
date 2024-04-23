valores = [1, 2, 3, 4, 2, 5, 6, 7, 8, 9, 10]
anos = [2020, 2030, 2040, 2050]

# Adicionar um valor no final da lista
valores.append(11)
print(valores)

# Unir as listas sem criar uma nova lista
valores.extend(anos)
print(valores) 

# Adicionar a lista criando uma nova
nova_lista = valores + anos
print(nova_lista)

# Inserir um novo valor a lista
print(anos[1])
anos.insert(2, 2031)
print(anos)

# Extrair com base no índice da lista
# O pop extrai o item e retorna ele 
anos_2020 = anos.pop(0)
print(anos)
print(anos_2020)

# Remover da lista
anos.remove(2050)
print(anos)

# Del remove 1 ou uma faixa de números
print(valores)
del valores[2:5] # Remove depois do primeiro indice e o último
print(valores)

# Contando a ocorrência de um valor na lista
quantas_vezes_aparece_o_2 = nova_lista.count(2)
print(quantas_vezes_aparece_o_2)  

# Resetar a lista por completo
nova_lista.clear()
print(nova_lista)