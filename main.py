while True:    
    # 1. Obtener la entrada del usuario
    numBin: str = input("Ingresa un numero binario de 8 digitos:\n")

    # 2. Verificar la entrada: tamaño, todos los caracteres numericos, todos los valores son 1 o 0
    es_valido = True
    tamañoString: int = len(numBin)

    if tamañoString > 8 or tamañoString < 8:
        print("Debes de ingresar un numero que no supere los 8 digitos o que no sea menor a 8.")
        es_valido = False
    else:
        for letter in numBin:
            if letter != "0" and letter != "1":
                print("Debes de ingresar un numero binario(0 o 1)")
                es_valido = False
                break

    # 3. Se hace la sumatoria de los valores de los diferentes digitos
    valor_decimal = 0
    if es_valido:
        multiplicador = 1
        for letter in reversed(numBin):
            if letter == "1":
                valor_decimal += int(letter) * multiplicador
            multiplicador *= 2


    # 4. Mostrar por pantalla el valor decimal
    if es_valido:
        print(f"El valor decimal de {numBin} es: {valor_decimal}")

    continuar = False
    print("¿Deseas continuar convirtiendo binario a decimales?")

    while True: 
        print("-- Ingresa Y para continua o N para salir")
        continuar = input("Ingresar opcion: ")
        if continuar == "Y" or continuar == "N": 
            break

    if continuar == "N":
        break

