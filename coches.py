lista_coche = []
while True:
    marcacoche = input("marca del coche: ")
    if marcacoche == "fin":
        break
    modelo = input("modelo del coche: ")
    cambio = input("¿Qué tipo de cambio utiliza?: ")
    traccion = input("¿Qué traccion tiene?: ")
    linea= {}
    linea["marca coche: "] = marcacoche
    linea["modelo: "] = modelo
    linea["cambio: "] = cambio
    linea["traccion: "] = traccion
    lista_coche.append(linea)

print("Lista coche:\n", lista_coche)
