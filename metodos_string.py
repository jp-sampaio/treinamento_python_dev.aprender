nome_curso = ' Edição de Vídeo '

print(nome_curso.upper())
print(nome_curso.lower())
print(nome_curso.strip())
print(nome_curso.lstrip())
print(nome_curso.rstrip())
print(nome_curso.find('ção'))
print(nome_curso.replace('Vídeo', 'Música'))
print('https://sc.olx.com.br/?o=90&q=relogio'.replace('relogio', 'carro'))

# Desafio
# # Através da criação de string dinâmicas e os métodos de um string que acabou de aprender, use como base as variáveis a seguir para criar as seguintes frases
a = 'é'
b = 'MELHOR'
c = 'QUE'
d = 'feito'
e = 'perfeito'

# É melhor FEITO que PERFEITO

print(f'{a.upper()} {b.lower()} {d.upper()} {c.lower()} {e.upper()}')