# Regex ou Regular Expression
'''
    De forma geral, o regex é como se fosse uma forma de encontrar, substituir ou extrair um único ou uma sequência de 
    carácteres de dentro de uma string.

    CARACTERES => qualquer letra, digito ou símbolo
'''

# Módulo da expressões regulares
import re

hey = 'jpsampaio@gmail.com'

#Função que busca todas as ocorrências de um padrão em uma string e retorna uma lista com todas as correspondências encontradas.
resultado_findall = re.findall(r"(@.{1,8}\.)", hey)
print(resultado_findall)

# O método search() procura pelo padrão na string, mas retorna apenas o primeiro match encontrado.
resultado_search = re.search(r"(@.{1,8}\.)", hey)
print(resultado_search)

# O método split() divide a string com base no padrão especificado e retorna uma lista de substrings.
resultado_split = re.split(r"(@.{1,8}\.)", hey)
print(resultado_split)

# O método sub() substitui todas as ocorrências do padrão por uma string específica.
resultado_sub = re.sub(r"(@.{1,8}\.)", "@hotmail", hey)
print(resultado_sub)