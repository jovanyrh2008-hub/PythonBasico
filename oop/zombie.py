from enemigo import *

class Zombie(Enemigo):
    def _init_(self, puntos_energia, ataque):
        super()._init_(tipo_enemigo='Zombie', puntos_energia=puntos_energia, ataque=ataque)

    def hablar(self):
        print("¡Grrrr...!")

    def propagar_enfermedad(self):
        print("El Zombie está tratando de propagar la enfermedad!")