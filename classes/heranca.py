# Herança
class Camera:
    def __init__(self, marca, megapixels):
        self.marca = marca
        self.megapixels = megapixels

    def tirar_foto(self):
        print(f'Foto tirada com a camera {self.marca} com a qualidade de {self.megapixels} megapixels')


# A classe filho vai herdar as propriedades da classe pai
class CameraCelular(Camera):
    def __init__(self, marca, megapixels, quantidade_de_cameras):
        # O metodo super vai herdar as propriedades de init da class pai
        super().__init__(marca, megapixels)
        self.quantidade_de_cameras = quantidade_de_cameras

    def aplicar_filtro(self, filtro):
        print(f'Aplicando filtro {filtro}')

    # Modificando o metodo da classe pai, precisa ter o mesmo nome do metodo original
    def tirar_foto(self, camera_a_utilizar):
        print(f'Foto tirada com a marca {self.marca} com a qualidade de {self.megapixels} megapixels utilizando a camera de número {camera_a_utilizar}')

camera_celular = CameraCelular('motorola', '100mp', 4)
camera_celular.aplicar_filtro('Azul')
print(camera_celular.marca)
print(camera_celular.megapixels)
print(camera_celular.quantidade_de_cameras)
camera_celular.tirar_foto(3)

# Mais de uma classe pode herdar de uma mesma classe pai 
class CameraSeguranca(Camera):
    def __init__(self, marca, megapixels, horas_maxima_de_gravacao):
        super().__init__(marca, megapixels)
        self.horas_maxima_de_gravacao = horas_maxima_de_gravacao

    def rotacionar_camera(self, direcao):
        print(f'Rotacionar a câmera para {direcao}')

camera_seguranca = CameraSeguranca('Sony', '25mp', 15)
camera_seguranca.rotacionar_camera('direita')

# Descobrir se uma subclass pertence a uma classe
print(issubclass(CameraSeguranca, Camera))
print(issubclass(CameraCelular, Camera))