import random


class Periferico:
    def __init__(self):
        self.numero_serie = random.randrange(100, 10000)
        self.estado = 100


class MonitorAcerPredator(Periferico):
    alto = 40
    ancho = 50
    profundidad = 10
    peso = 4
    color = "negro"
    pulgadas = 27
    conectores = ["hdmi", "dp"]
    botones = ["encendido", "menu"]
    resolucion = [2560, 1440]


monitor1 = MonitorAcerPredator()
monitor2 = MonitorAcerPredator()
monitor3 = MonitorAcerPredator()


class Teclado(Periferico):
    alto = 3
    ancho = 50
    profundidad = 30
    peso = 1
    color = "negro"
    numero_teclas = 74
    idioma = "es"

