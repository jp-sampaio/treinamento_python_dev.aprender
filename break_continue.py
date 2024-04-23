#  O break para o fluxo de vez e imperrompe a aplicação
#  O continue interrompe o fluxo e pula para o próximo passo

# Imterrompe o fluxo e pula para o próximo
# for numero in range(50):
#     if numero % 2 == 0:
#         print(numero)
#     else:
#         continue

# Interrompe o fluxo e para 
# for numero in range(50):
#     if numero % 2 == 0:
#         print(numero)
#     else:
#         break

# frutas = ['macã', 'uva', 'manga', 'banana', 'melancia', 'limão']

# Pula a fruta manga  
# for fruta in frutas:
#     if fruta == 'manga':
#         continue
#     print(f'Adicionar na dieta {fruta}')

# Para na fruta manga
# for fruta in frutas:
#     if fruta == 'manga':
#         break
#     print(fruta)

# ================ Desafio =============================

# DESAFIOS 🥇

## Desafio 1

# Use a operação necessária(break ou continue) para que a seguinte condição aconteça.

# * Ao chegar ao estilo "Rap" o mesmo não deve ser impresso na tela

# estilos = ['Hip-Hop','Rock','Rap','Pop']

# for estilo in estilos:
#     if estilo == 'Rap':
#         continue
#     print(estilo)

# ## Desafio 2 

# Use a operação necessária(braek ou continue) para que a seguinte condição aconteça:

# * Ao chegar ao estilo "Rock" a execução deve interrompida

estilos = ['Hip-Hop','Rock','Rap','Pop']

for estilo in estilos:
    if estilo == 'Rock':
        break
    print(estilo)