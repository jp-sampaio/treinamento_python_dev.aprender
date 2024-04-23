# Um modulo nada mais é do que um arquivo python
# from imagem import * => dessa forma é importado todas as funcionalidades e propriedades do arquivo, também posso renomear com o as
from imagem import tirar_foto, qualidade_da_foto, Camera

def gravando_um_video():
    print('Gravando uma video.')

tirar_foto()
print(qualidade_da_foto)
camera = Camera()