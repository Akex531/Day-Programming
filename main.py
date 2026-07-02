# 1. Obtener la entrada del usuario
numBin: str = input("Ingresa un numero binario de 8 digitos:\n")

# 2. Verificar la entrada: tamaño, todos los caracteres numericos
tamañoString: int = len(numBin) 
if tamañoString > 8 or tamañoString == 0:
    print("Debes de ingresar un numero que no superes los 8 digitos.")
else:
    for letter in numBin:
        if letter != "0" or letter != "1":
            print("Debes de ingresar un numero binario(0 o 1)")



