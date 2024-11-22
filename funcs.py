import random

def imprimirMenu(): # Funcion para el menú
    print("=== CALCULATRON 2.0 ===")
    print("1. Jugar")
    print("2. Configuración")
    print("3. Estadísticas")
    print("4. Logros")
    print("0. Salir")
    print("========================")


def operadorRandom() -> str: # Función para generar un operador aleatorio
    operadorAleatorio = random.randint(1,4)
    if operadorAleatorio == 1:
        operador = "+"
    elif operadorAleatorio == 2:
        operador = "-"
    elif operadorAleatorio == 3:
        operador = "*"
    elif operadorAleatorio == 4:
        operador = "//"

    return operador


def generarCuenta(numMin: int, numMax: int) -> int: # Funcion para crear una cuenta aleatoria
    operador = operadorRandom()
    num1 = random.randint(numMin, numMax)
    num2 = random.randint(numMin, numMax)

    if operador == "//":
        while num2 == 0 or num1 % num2 != 0:
            num1 = random.randint(numMin, numMax)
            num2 = random.randint(numMin, numMax)

    match operador:
        case "+":
            resultado = num1 + num2
        case "-":
            resultado = num1 - num2
        case "*":
            resultado = num1 * num2
        case "//":
            resultado = num1 // num2
    print(f"{num1} {operador} {num2} = ?")
    return resultado


def configuracionActual(vidaConfiguracion: int, numMin:int, numMax:int) -> str: # Funcion para el menú de configuración
    print("La configuración actual es: ")
    print(f"Tienes {vidaConfiguracion} vidas.")
    print(f"El número mínimo es {numMin}.")
    print(f"El número máximo es {numMax}.")


def logros(logroBronce:bool, logroPlata:bool, logroOro:bool, logroPlatino:bool)-> str:# Funcion para los logros
    if logroBronce == True:
        print("Logro de bronce: acierta tres operaciones seguidas en la misma partida -> LOGRADO")
    elif logroBronce == False:
        print("Logro de bronce: acierta tres operaciones seguidas en la misma partida -> NO LOGRADO")

    if logroPlata == True:
        print("Logro de plata: acierta siete operaciones consecutivas en la misma partida -> LOGRADO")
    elif logroPlata == False:
        print("Logro de plata: acierta siete operaciones consecutivas en la misma partida -> NO LOGRADO")

    if logroOro == True:
        print("Logro de oro: acierta diez operaciones consecutivas en la misma partida -> LOGRADO")
    elif logroOro == False:
        print("Logro de oro: acierta diez operaciones consecutivas en la misma partida -> NO LOGRADO")

    if logroPlatino == True:
        print("Logro de platino: acierta diez operaciones consecutivas en la misma partida con dificultad aumentada a numMin >= 10 y NumMax >= 15 -> LOGRADO")
    elif logroPlatino == False:
        print(
            "Logro de platino: acierta diez operaciones consecutivas en la misma partida con dificultad aumentada a numMin >= 10 y NumMax >= 15 -> NO LOGRADO")

