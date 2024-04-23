# Os kwargs serve para definir uma quantidade ilimitada de argumentos do tipo 
# chave/valor (Nomeados).

def concatenar(**palavras):
  frase = ''
  for palavra in palavras.values():
    frase += palavra + ' '
  print(frase)

concatenar(a='Nós', b='Somos', c='Pythonistas', d='Profissionais')


# Utilizando os args e os kwargs na mesma função para fixar os conhecimentos sobre 
# argumentos posicionais e nomeados.
def fazer_calculo(nome, *args, **kwargs):
  print(nome)  
  print(args) # Tuplas
  print(kwargs) # Dicionário

  for arg in args:
    print(arg)

  # Preciso utilizar o value nos kwargs divido eu querer somente o valor 
  for kwarg in kwargs.values():
    print(kwarg)

fazer_calculo('joão', 23, 56, 84, a=1, b=2, c=4)