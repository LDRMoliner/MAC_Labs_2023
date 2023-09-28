import math
import random


# 1. Calcular el valor absoluto de un número negativo dado como entrada.

def valor_absoluto(numero_negativo):
    return abs(numero_negativo)


# 2. Suma de dos números enteros (los dos números se propocionan como entrada.)

def suma_2_valores(sumando1, sumando2):
    return sumando1 + sumando2


# 3. Convierte la temperatura de grados Celsius (tCelsius como valor de entrada) a grados Fahrenheit.

def convertir_celsius_fahrenheit(grados_celsius):
    return (9 / 5 * grados_celsius + 32)


# 4. Calcula el área de una esfera (radio como entrada)

def calcular_area_esfera(radio):
    return 4 * math.pi * radio ** 2


# 5. Dados 3 números guardados en las variables a, b y c (de forma que a y b
#    tengan el mismo número y c sea mayor), programa las instrucciones assert que
#    verifiquen que:
#    a y b son iguales
#    b es menor que c
#    c es mayor que a

def comprobar_relaciones(a, b, c):
    if a == b:
        print("a es igual que b")
    else:
        print("a y b no son iguales")
    if b < c:
        print("b es menor que c")
    else:
        print("b no es menor que c")
    if c > a:
        print("c es mayor que a")
    else:
        print("c no es mayor que a")


# 6. Calcula la distancia euclı́dea entre dos punts. Las coordenadas de cada punto
#    se dan como entrada.

def distancia_euclidea(x1, x2, y1, y2):
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)


# 7. Calcula la siguiente expresión (x, y son datos de entrada):

def calcular_expresion(x, y):
    res = 5 * (x ** 3) + math.sqrt(x ** 2 + y ** 2) + math.e ** math.log(x)
    return res


# 8. Inicializa una colección de datos en Python que tenga los siguientes valores: 1,
#    2, 3, 4, 5 Usa los operadores corchete ([, ]) para indicar el inicio y el final de
#    los elementos de la colección.

def inicializar_lista():
    return [1, 2, 3, 4, 5]


# 9. Inicializa una lista en Python en la que haya al menos 3 apariciones del número
#    4. Sustituir todas las apariciones del número 4 por 10.

def comprobar_y_sustituir_4(lista):
    numero_4 = lista.count(4)
    if (3 > numero_4):
        print("No hay suficientes cuatro.")
        return
    for i in range(len(lista)):
        if lista[i] == 4:
            lista[i] = 10


# 10. Conjetura de Collatz: Pasada una lista con números arbitrarios, vamos a devolver otra lista
#     con el número de pasos necesarios para que cada número pueda ser reducido a 1.

def pasos_collatz(a):
    pasos = 0
    while (a != 1):
        if (a % 2 == 0):
            a = a // 2
        else:
            a = 3 * a + 1
        pasos += 1
    return pasos


def conjetura_collatz_pasos_lista(old_list):
    return [pasos_collatz(elem) for elem in old_list]


# 11. Inicializa una matriz (lista de listas) de 6 × 3 con valores comprendidos entre
#     -5 y 5.

def matriz_negativa_5():
    return [[random.randint(-5, 5) for i in range(3)] for j in range(6)]


# 12. Crea un método en Python que, dada una matriz cualquiera y un número x,
#     devuelva el número de veces que x aparece en dicha matriz.

def veces_numero(matriz, numero_a_buscar):
    return matriz.count(numero_a_buscar)


# 13. Crea un método en Python que devuelva si hay algún número entre 4 y 7 en
#     una matriz (lista de listas) de números.

def comprobar_4_y_7(matriz):
    hay_numero_entre_rango = False
    for fila in matriz:
        for elemento in fila:
            if (4 <= elemento <= 7):
                hay_numero_entre_rango = True
        if hay_numero_entre_rango:
            break

    print (hay_numero_entre_rango)

# 14. Dadas una lista de números enteros, que siempre son positivos o negativos, y
# una lista de booleanos (True, False) con el mismo tamaño, crea una función que
# devuelva el número de veces que un número positivo es True y uno negativo
# es False en su correspondiente posición. Por ejemplo, dados: a = [-2, 3, 4, -
# 7, 10, -234] y b = [True, True, True, True, False, False], se debe devolver: (2, 1).

def contar_correspondencias(lista, lista_booleana):

    correspondencia_positiva = 0
    correspondencia_negativa = 0

    for i in range(len(lista)):
        if ((lista[i] > 0) and lista_booleana[i]):
            correspondencia_positiva += 1
        if ((lista[i] < 0) and not (lista_booleana[i])):
            correspondencia_negativa += 1

    return [correspondencia_positiva, correspondencia_negativa]