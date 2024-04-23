# Classes abstratas
# Criar um contrato(esqueleto) => que deve ser implementado na classe que a herda.

from abc import ABC, abstractmethod

class Camera(ABC):
    # Obriga a nova classe que vai herdar definir esse mesmo metodo
    @abstractmethod
    def definir_tamanho_lente(self, tamanho):
        pass

class CameraProfissional(Camera):
    def definir_tamanho_lente(self, tamanho):
        print(f'Alterando a lente para {tamanho}')

camera_profissional = CameraProfissional()
camera_profissional.definir_tamanho_lente(4)


# =====================================================

# Desafio 
class Monitor(ABC):
    @abstractmethod
    def aumentar_claridade(self, brilho):
        pass

    @abstractmethod       
    def reduzir_claridade(self, brilho):
        pass

class MonitorFullHD(Monitor):
    def aumentar_claridade(self, brilho):
        print(f'Aumentando a claridade em {brilho} pontos')

    def reduzir_claridade(self, brilho):
        print(f'Reduzindo a claridade em {brilho} pontos')

monitor_full_hd = MonitorFullHD()
monitor_full_hd.aumentar_claridade(5)
monitor_full_hd.reduzir_claridade(5)