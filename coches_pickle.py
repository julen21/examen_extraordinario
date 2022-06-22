import pickle
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

with open('coches.txt', 'w') as fp:
    json.dump(lista_coche, fp)

with open('coches.txt', 'r') as fp:
    data = json.load(fp)
print(data)
print(type(data))