import os
import random


def main():

    ######################################################### Ej. 1 #########################################################
    # Cree una funcion que calcule el promedio de N notas

    def calcularPromedioNotasRandom(nNotas=0):
        promedio = 0.0
        if nNotas > 0:
            contadorNotas = 0
            for n in range(nNotas):
                nota = round(random.uniform(0.0, 10.0), 2)
                print(f"Nota #{n+1}: {nota}.")
                contadorNotas += nota
            promedio = round(contadorNotas / nNotas, 2)
            print(
                f"El número de notas ingresado es {nNotas} y el promedio obtenido es de: {promedio}."
            )
        elif nNotas == 0:
            promedio = 0.0
            print(
                f"El número de notas ingresado es 0. Por lo tanto el promedio es {promedio}."
            )
        else:
            print(
                f"El número de notas ingresado: {nNotas} es invalido. El parámetro debe ser un entero mayor o igual a 0."
            )
            promedio = (
                -1
            )  # devuelve -1 en caso que el parámetro nNotas esté fuera de un rango válido.
        return promedio

    # promedio = calcularPromedioNotasRandom(10)
    # promedio = calcularPromedioNotasRandom(0)
    # promedio = calcularPromedioNotasRandom(-1)

    ######################################################### Ej. 2 #########################################################
    # Cree una funcion que determine si un color es primario o no, se debe imprimir por pantalla la leyenda “el color X es primero “ o “el color X no es primario”

    def esColorPrimario(color="blanco"):
        esPrimario = False
        coloresPrimarios = {"rojo": True, "amarillo": True, "azul": True}
        if coloresPrimarios.get(color):
            esPrimario = True
            print(f"El color {color} es primario.")
        else:
            print(f"El color {color} no es primario.")
        return esPrimario

    # esPrimario = esColorPrimario("blanco")
    # esPrimario = esColorPrimario("rojo")
    # esPrimario = esColorPrimario("negro")
    # esPrimario = esColorPrimario("amarillo")
    # esPrimario = esColorPrimario("naranja")
    # esPrimario = esColorPrimario("azul")

    ######################################################### Ej. 3 #########################################################
    # Cree una funcion que determine que numero de una serie de N numeros es mayor

    def encontrarNumeroMayorEntreNumerosRandom(nNumerosRandom=0):
        numeroRandomMayor = 0.0
        if nNumerosRandom > 1:
            for n in range(nNumerosRandom):
                numRandom = round(random.random(), 2)  # uniform(0.0, 1000.0), 2)
                print(f"{n+1}° numero: {numRandom}.")
                if numRandom > numeroRandomMayor:
                    print(
                        f"{numRandom} es mayor que {numeroRandomMayor}, por lo tanto pasa a ser el nuevo número mayor."
                    )
                    numeroRandomMayor = numRandom
                else:
                    print(
                        f"{numRandom} es menor o igual a {numeroRandomMayor}, por lo tanto {numeroRandomMayor} sigue siendo el mayor número ingresado."
                    )
            print(
                f"RESULTADO: se generaron {nNumerosRandom} números random y el mayor entre ellos fue: {numeroRandomMayor}."
            )
        elif nNumerosRandom == 1:
            numRandom = round(random.random(), 2)
            numeroRandomMayor = numRandom
            print(
                f"El único número random es {numeroRandomMayor} y se transforma en el número mayor automaticamente."
            )
        elif nNumerosRandom == 0:
            numeroRandomMayor = 0.0
            print(
                f"La cantidad de números random elegidos es 0, no es posible realizar comparaciones."
            )
        else:
            print(
                f"La cantidad de números random ingresado: {nNumerosRandom} es invalido. El parámetro debe ser un entero mayor a 0."
            )
            numeroRandomMayor = (
                -1
            )  # devuelve -1 en caso que el parámetro nNumerosRandom esté fuera de un rango válido.
        return numeroRandomMayor

    # numMayor = encontrarNumeroMayorEntreNumerosRandom(10)
    # numMayor = encontrarNumeroMayorEntreNumerosRandom(1)
    # numMayor = encontrarNumeroMayorEntreNumerosRandom(0)
    # numMayor = encontrarNumeroMayorEntreNumerosRandom(-1)

    ######################################################### Ej. 4 #########################################################
    # Cree una funcion que dibuje un rectangulo de X filas y X columnas determinadas por el usuario

    def dibujarRectangulo(xPos=1, yPos=1):
        cadena = ""
        if xPos >= 1 and yPos >= 1:
            for j in range(yPos):
                cadena = ""
                for i in range(xPos):
                    if i == 0 or i == xPos - 1 or j == 0 or j == yPos - 1:
                        cadena += "*"
                    else:
                        cadena += " "
                print(cadena)
        else:
            print("*")

    # dibujarRectangulo(10, 20)
    # dibujarRectangulo(0, 0)
    # dibujarRectangulo(-20, -5)
    # dibujarRectangulo(50, 50)
    # dibujarRectangulo(20, 10)
    # dibujarRectangulo(12, 12)

    ######################################################### Ej. 5 #########################################################
    # Cree una funcion que calcule el Factorial de un numero entero positivo

    def factorial(entero=0):
        factorial = 1
        i = 1
        while i <= entero:
            factorial = factorial * i
            i = i + 1
        return factorial

    # num = 0
    # num = 3
    # num = 2
    # num = 10
    # num = -1
    # valorFactorial = factorial(num)
    # print(f"FACTORIAL({num}) = {valorFactorial}")


#########################################################################################################################

# Ejecución de la función main()
if __name__ == "__main__":
    main()
