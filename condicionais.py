# pessoa 1 => Podemos sair hoje?
# pessoa 2 => Se eu tiver terminado o trabalho, podemos sim.

trabalho_terminado = True
if trabalho_terminado == True:
  print('Podemos dar uma saída')
else:
  print('Infelizmente não consegui concluir o trabalho')


# Se um funcionário chegar atrasado 3 ou mais vezes no trabalho, ele deve  ir no RH

numero_de_atrasos = 8

if numero_de_atrasos >= 3:
  print('Passe no RH')
elif numero_de_atrasos == 2:
  print('Você tem 2 faltas')
elif numero_de_atrasos == 1:
  print('Você tem 1 falta')
else: 
  print('Pode entrar')


# A velocidade máxima para essa rua é de 50km;
# Cruzou entre 51km a 60km, levou multa de 2 pontos 
# Cruzou entre 61km a 70km, levou multa de 3 pontos 
# Cruzou acima de 75km, levou multa de 7 pontos 

velocidade = 120

if velocidade == 50:
  print('Não levou multa')
elif 51 <= velocidade <= 60:
  print('Levou multa de 2 pontos')
elif 61 <= velocidade <= 75:
  print('Levou multa de 3 pontos')
else:
  print('Levou multa de 7 pontos')



# Desafio 🥇

# Monte o seguinte cenário usando condicionais

# Você está montando um sistema para um salão de beleza para calcular o preço do corte de cabelos grandes que irá seguir as seguinte regras

# Disclaimer the haircut values are completely ficticious, I have no ideia of actual prices

'''

Se seu cabelo estiver com ou abaixo de 20cm você paga o valor de R$50,00

Se seu cabelo estiver entre 21cm a 30cm você paga o valor de R$70,00

Se seu cabelo estiver entre 31cm a 50cm você paga o valor de R$100,00

Acima de 50cm Favor consultar na recepção

# Declare uma variável que represente o tamanho atual do cabelo

# Apenas imprima na tela a mensagem apropriada, nada além disso é necesário

'''

tamanho_do_cabelo = 80

if tamanho_do_cabelo <= 20:
  print('Você paga o valor de R$50,00')
elif 21 <= tamanho_do_cabelo <= 30:
  print('Você paga o valor de R$70,00')
elif 31 <= tamanho_do_cabelo <= 50:
  print('Você paga o valor de R$100,00')
else:
  print('Favor consultar na recepção')