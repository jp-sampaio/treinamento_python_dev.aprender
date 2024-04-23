# Metodos comuns => São os metodos que utilizan as propriedades da instacia, eles obrigatoriamente precisam utilizar o self;
# Metodos de Classes => Eles são utilizados quando preciso modificar algo na classe;
# Metodos estaticos => Não utilizam as propriedades da instancia nem modificam a classe mas é interessante manter na classe

class Computador:
    sistema_operacional = 'Windows 10'

    def __init__(self, marca, memoria_ram, placa_de_video):
        self.marca = marca
        self.memoria_ram = memoria_ram
        self.placa_de_video = placa_de_video

    # Metodos comuns que utilizam a propriedades da classe com o self
    def exibir_as_informacoes_do_computador(self):
        print(self.marca, self.memoria_ram, self.placa_de_video, self.sistema_operacional)

    # Metodos de classe que modificam a classe 
    @classmethod
    def configuracoes_para_pc_fraco(cls, memoria_ram): # cls é uma conferção mundial, é a própria class
        return cls('Asus', memoria_ram, 'Placa de video - custo beneficio')
    @classmethod
    def configuracoes_para_pc_potente(cls, memoria_ram):
        return cls('Dell', memoria_ram, 'Placa de video - alto custo')
    
    # Metodos estaticos que não recebe as propriedades da instacia e nem a modifica, mas é importanrte está na classe
    @staticmethod
    def roda_programas_pesados(memoria_ram):
        if memoria_ram >= 10:
            return True
        else:
            return False
        
computador1 = Computador.configuracoes_para_pc_fraco('8gb')
computador2 = Computador.configuracoes_para_pc_potente('16gb')

computador1.exibir_as_informacoes_do_computador()
computador2.exibir_as_informacoes_do_computador()

print(Computador.roda_programas_pesados(16))