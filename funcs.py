import random


def menu(): # Funcion para el menú
    print("=== CALCULATRON 2.0 ===")
    print("1. Jugar")
    print("2. Configuración")
    print("3. Estadísticas")
    print("4. Logros")
    print("0. Salir")
    print("========================")

def operadorRandom() -> str: # Función para generar un operador aleatorio
    operadorAleatorio = random.randint(1,4)
    match operadorAleatorio:
        case 1:
            operador = "+"
        case 2:
            operador = "-"
        case 3:
            operador = "*"
        case 4:
            operador = "%"

    return operador

def operaciones(numMin: int, numMax: int) -> int: # Funcion para crear una cuenta aleatoria
    operador = operadorRandom()
    num1 = random.randint(numMin, numMax)
    num2 = random.randint(numMin, numMax)

    if operador == "%":
        while num1 % num2 != 0:
            num1 = random.randint(numMin, numMax)
            num2 = random.randint(numMin, numMax)

    match operador:
        case "+":
            resultado = num1 + num2
        case "-":
            resultado = num1 - num2
        case "*":
            resultado = num1 * num2
        case "%":
            resultado = num1 / num2
    print(f"{num1} {operador} {num2} = ?")
    return resultado

def configuracionActual(vidaConfig: int, numMin:int, numMax:int) -> str: # Funcion para el menú de configuración
    print("La configuración actual es: ")
    print(f"Tienes {vidaConfig} vidas.")
    print(f"El número mínimo es {numMin}.")
    print(f"El número máximo es {numMax}.")

def logros(bronce:bool, plata:bool, oro:bool,platino:bool)-> str: # Funcion para los logros
    if bronce == True:
        print("Logro de bronce: acierta tres operaciones seguidas en la misma partida -> LOGRADO")
    elif bronce == False:
        print("Logro de bronce: acierta tres operaciones seguidas en la misma partida -> NO LOGRADO")

    if plata == True:
        print("Logro de plata: acierta siete operaciones consecutivas en la misma partida -> LOGRADO")
    elif plata == False:
        print("Logro de plata: acierta siete operaciones consecutivas en la misma partida -> NO LOGRADO")

    if oro == True:
        print("Logro de oro: acierta diez operaciones consecutivas en la misma partida -> LOGRADO")
    elif oro == False:
        print("Logro de oro: acierta diez operaciones consecutivas en la misma partida -> NO LOGRADO")

    if platino == True:
        print("Logro de platino: acierta diez operaciones consecutivas en la misma partida con dificultad aumentada a numMin >= 10 y NumMax >= 15 -> LOGRADO")
    elif platino == False:
        print(
            "Logro de platino: acierta diez operaciones consecutivas en la misma partida con dificultad aumentada a numMin >= 10 y NumMax >= 15 -> NO LOGRADO")

