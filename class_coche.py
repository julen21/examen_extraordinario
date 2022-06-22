class Coche:

    def __init__(self):
        self.marca = input("marca del coche: ")
        self.modelo = input("modelo del coche: ")
        self.cambio = input("¿Qué tipo de cambio utiliza?: ")
        self.traccion = input("¿Qué traccion tiene?: ")
    def imprimir(self):
        print("Marca: ", self.marca)
        print("Modelo: ", self.modelo)
        print("Cambio: ", self.cambio)
        print("Traccion: ",self.traccion)

# Módulo principal

coche1=Coche()
coche1.imprimir()

