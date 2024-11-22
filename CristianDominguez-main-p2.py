from funcs import imprimirMenu, generarCuenta, configuracionActual, logros


cuentas = 0
numMin = 0
numMax = 10
aciertosTotales = 0
fallosTotales = 0
partida = 0
cuentasTotales = 0
rachaMaxima = 0
logroBronce = False
logroPlata = False
logroOro = False
logroPlatino = False
vidaConfiguracion = 3

while True:
    aciertos = 0
    fallos = 0
    falloRacha = 0
    racha = 0
    vida = vidaConfiguracion

    imprimirMenu()
    opcion = int(input("Inserta una opción: "))

    if opcion == 0:
        break
    elif opcion == 1:
        print(f"Partida comenzada {partida}")
        partida += 1
        while vida > 0:
            cuentas +=1
            cuentasTotales +=1
            resultadoCalculado = generarCuenta(numMin, numMax)
            resultadoMio = int(input("Inserta el resultado: "))

            if resultadoMio == resultadoCalculado:
                aciertos +=1
                aciertosTotales +=1
                racha +=1

                if racha > rachaMaxima:
                    rachaMaxima = racha

                if racha == 3 and logroBronce == False:
                    print("LOGRO DE BRONCE DESBLOQUEADO")
                    logroBronce = True
                elif racha == 7 and logroPlata == False:
                    print("LOGRO DE PLATA DESBLOQUEADO")
                    logroPlata = True
                elif racha == 10 and logroOro == False:
                    print("LOGRO DE ORO DESBLOQUEADO")
                    logroOro = True
                elif racha == 10 and numMin >=10 and numMax >=25:
                    print("LOGRO PLATINO DESBLOQUEADO")
                    logroPlatino = True

                print("Has acertado")

            else:
                vida -=1
                fallosTotales +=1
                fallos += 1
                racha = 0
                print("No has acertado")
                print(f"El resultado es {resultadoCalculado}")
                print(f"Te quedan {vida} vidas.")
            falloRacha +=1
        print(f"En tu partida número {partida} has acertado {aciertos} y has fallado {fallos}")
        print(f"Has acertado {round(aciertos * 100 / cuentasTotales, 2)}%")

    elif opcion == 2:
        while True:
            configuracionActual(vidaConfiguracion, numMin, numMax)
            print("")
            print("1. Configuración de vida")
            print(f"2. Número mínimo {numMin}")
            print(f"3. Número máximo {numMax}")
            print("0. Salir")

            opcionConfiguracion = int(input("Inserta una opcion: "))

            if opcionConfiguracion == 1:
                vidaConfiguracion = int(input("Inserta un número de vidas entre 1 y 10: "))
                while vidaConfiguracion <1 or vidaConfiguracion >10:
                    vidaConfiguracion = int(input("Inserta un número de vidas entre 1 y 10: "))

                configuracionActual(vidaConfiguracion, numMin, numMax)
            elif opcionConfiguracion == 2:
                numMin = int(input("¿Que número minimo quieres?: "))
                while numMin > numMax:
                    numMin = int(input("El número mínimo no puede ser mayor que el maximo: "))

                configuracionActual(vidaConfiguracion,numMin, numMax)

            elif opcionConfiguracion == 3:
                numMax = int(input("¿Que número máximo quieres?: "))
                while numMax < numMin:
                    numMax = int(input("El número máximo no puede ser menor que el número mínimo: "))
                configuracionActual(vidaConfiguracion,numMin, numMax)

            elif opcionConfiguracion == 0:
                print("Has salido del menú")
                break
            else:
                print("No has insertado una opción valida")
    elif opcion == 3:

        print(f"Has jugado un total de {partida} partidas.")
        print(f"En esas partidas has realizado un total de {cuentas} cuentas.")
        print(f"Has acertado un total de {aciertosTotales} cuentas.")
        if aciertosTotales == 0:
            print("Tu porcentaje de aciertos es del 0%")
        else:
            porcentajeAciertos = int(aciertosTotales * 100 / cuentasTotales)
            print(f"Tu porcentaje de aciertos es del {porcentajeAciertos} %")
        print(f"Has fallado un total de {fallosTotales} cuentas.")
    elif opcion == 4:
        logros(logroBronce,logroPlata,logroOro,logroPlatino)
