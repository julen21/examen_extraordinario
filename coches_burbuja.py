lista_coche = []
while True:
    marcacoche = input("Nombra las diferentes marcas de los coches: ")
    if marcacoche == "fin":
        break

    cadena = marcacoche.lower()
    cadena = cadena.split()

    for i in range(len(cadena)):
        for j in range(i + 1, len(cadena)):
            if cadena[i] > cadena[j]:
                cadena[j], cadena[i] = cadena[i], cadena[j]

    modelo = input("modelo de los coche: ")
    cambio = input("¿Qué tipo de cambio utilizan?: ")
    traccion = input("¿Qué traccion tienen?: ")
    linea= {}
    linea["marca coche: "] = marcacoche
    linea["modelo: "] = modelo
    linea["cambio: "] = cambio
    linea["traccion: "] = traccion
    lista_coche.append(linea)

for palabra in cadena:
    print(palabra, lista_coche)