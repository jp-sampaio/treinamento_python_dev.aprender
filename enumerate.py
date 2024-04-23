# O enumerate serve para identificar onde estamos dentro do loop e com isso podemos criar condições que atendam as nessidades 
# como por exemplo parar o loop ou então mostrar alguma informação

for indice, numero in enumerate(range(1, 11), 1):
    print(indice, numero)
    if numero == 5: 
        print('Estamos na metade da lista')


nomes = ['nomes1', 'nomes2', 'nomes3', 'nomes4', 'nomes5']

for indice, nome in enumerate(nomes, 0):
    print(f'{indice} possui {nome}')
    if indice == 2: 
        print('Já foram registrado 3 nomes')


# Desafios 
# Itere sobre a lista abaixo exibindo o número do indice + nome da fruta. Porém quando o índice for 3 exiba 'N° índice + nome da fruta EM PROMOÇÃO'
 
frutas = ['Maça', 'Laranja', 'Morango', 'Limão']
for indice, fruta in enumerate(frutas, 0):
    print(indice, fruta)
    if indice == 3:
        print(f'{indice} {fruta} EM PROMOÇÃO')