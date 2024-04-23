# Desafio 1 => Encontre a palavra simples
    # Olá! sou uma frase simples
# Resposta: simples

'''
 Desafio 2 => Encontre todas as ocorrências de 23(os números juntos) e exatamente com esses valores
    dev123com
    developer 123
    dev = 123
    dev = 1234
    dev = 1337
    dev = 9000

    Resposta: 23
'''

'''
 Desafio 3 => Encontre todos os valores onde o valor inicial é 2, porém o segundo valor não conhecemos: ex: 23, 25, etc...
    dev123com
    developer 123
    dev = 123
    dev = 1234
    dev = 1337
    dev = 900

    Resposta: 2\d
'''

'''
 Desafio 4 => Usando os valores a seguir, encontre os seguintes números por completo, usando regex
    13.35.86
    22.36.77
    53.12.34

    Resposta: \d\d\.\d\d\.\d\d
'''

'''
 Desafio 5 => Crie um regex para encontrar o seguinte padrão: Encontre as combinações segundo descrito abaixo

    bah pular
    tah encontrar
    jah encontrar
    nah encontrar
    uai pular

    Resposta: [tjn]ah  // As 3 primeiras letras com o final igual
'''

'''
 Desafio 6 => Encontre a combinação de acordo com o descrito abaixo:

    (123)1234-1235 encontrar
    (123)1234-1235 encontrar
    (129)1234-1235 pular
    (129)1234-1235 pular

    Resposta: [(]123[)]\d\d\d\d[-]\d{4} // Foram adicionados a simplificação dos \d
'''

'''
 Desafio 7 => Usando o regex, encontre apenas a sequência 1234 abaixo:
    1234 encontrar
    6462 pular

    Resposta: [1-4]
'''

'''
 Desafio 8 => Usando regex, encontre apenas as letras que iniciam com p até a letra v

    pqrstuv encontrar
    wxyz pular
    abcdefg pular

    Resposta: [p-v] ou [p].+[v]
'''

'''
 Desafio 9 => Crie uma regex para encontrar tanto as pizzas enviadas como pizza enviada

    2 pizzas enviadas

    1 pizza enviada

    3 pizzas enviadas

    Resposta: pizzas? enviadas?
'''