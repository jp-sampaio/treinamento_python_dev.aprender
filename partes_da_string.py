teclado = 'teclado'
print(teclado[3]) # l
print(teclado[-1]) # O último => o
print(teclado.index('d')) # Indice do d => 5

link = 'facebook.com/devaprender'
print(link[0]) # Primeiro
print(link[-1]) # Último
print(link[0:5]) # Primeiro ao anterior do indice 5
print(link[0:]) # Primeiro ao último
print(link[-5:]) # Indice 5 de trás para frente e contando apartir dele até o último
print(link[5:]) # Indice 5 até o final
print(link[:-5]) # Do inicio até o indice 5 de trás para frente 

# Pega o último C
frase = 'Clean Code'
print(frase.rindex('C'))

'''
  Dessafio
    # Encontrar o indice de 'o' dentro da variável biblioteca
    biblioteca = 'biblioteca'

    # Usando as palavras
    'Desenvolvimento De Aplicações'

    # Imprima apenas a palavra de 'De Aplicações'
'''

biblioteca = 'biblioteca'
print(biblioteca.index('o'))

palavra = 'Desenvolvimento De Aplicações'
indice_d = palavra.rindex('D')
indice_s = palavra.rindex('s')
print(palavra[indice_d:indice_s])