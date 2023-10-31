def sumar_5_enteros():
    # definicion de variables
    lista = []
    contadorWhile = 0
    tamaño = 5
    suma = 0

    #Ingresamos los numeros
    while contadorWhile < tamaño:
        lista.append(int(input("ingrese numero" + str(contadorWhile+1) + ": ")))
        contadorWhile += 1

    # Sumamos los numeros:
    contadorWhile = 0
    while contadorWhile < tamaño:
        suma += lista[contadorWhile]
        contadorWhile += 1

    print("Los elementos de la lista son:")
    for numero in lista:
        print(numero,end= ', ')

    print("\nLa suma de todos sus elmentos es:")
    print(suma)



