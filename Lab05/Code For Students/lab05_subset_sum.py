from time import time
import itertools


# la funcion has_sum, dada una coleccion de positivos y un valor "value", decide si
# existe una subcoleccion de positivos que sumen "value" o no.
# Ha tardao una media de: 0.00063872002 segundos.
def has_sum(value, collection):
    if value == 0:
        return True
    if not collection:
        return False
    if collection[0] > value:
        return has_sum(value, collection[1:])
    return has_sum(value, collection[1:]) or has_sum(value - collection[0], collection[1:])


def remove_bigger_than(value, collection):
    return [val for val in collection if val < value]


def subset_preproc(value, collection):
    if sum(collection) < value:
        return [], False
    if sum(collection) == value:
        return collection, True
    if value in collection:
        return [value], True
    collection = remove_bigger_than(value, collection)
    return collection, False


def subset_rec(value, collection, assig):
    if value == 0:
        return assig
    if not collection or value < 0:
        return [None]
    if None not in assig:
        return [None]

    index_to_change = assig.index(None)

    copy_assig = list(assig)
    assig[index_to_change] = 1
    sum1 = subset_rec(value - collection[index_to_change], collection, assig)

    if sum1 != [None]:
        return sum1

    assig = list(copy_assig)
    assig[index_to_change] = 0
    sum2 = subset_rec(value, collection, assig)

    if sum2 != [None]:
        return sum2

    return [None]


def get_collection(assig, collection):
    result = [collection[i] for i in range(len(collection)) if assig[i] == 1]
    return result


# la funcion subset, dada una coleccion de positivos y un valor "value", si existe
# una subcoleccion de positivos que sumen "value" devuelve dicha subcoleccion.
# En otro caso devuelve la lista [None].
# Tarda aproximadamente 0.0013198853 segundos, con el subset de 17 valores tarda 0.0001568794.
def subset(value, collection):
    collection, found = subset_preproc(value, collection)
    assig = [None] * len(collection)
    if not collection:
        return [None]
    if found:
        return collection
    assig = subset_rec(value, collection, assig)
    if assig != [None]:
        subset = get_collection(assig, collection)
        return subset
    return [None]


def test():
    # coleccion 0
    collection0 = [3, 11, 8, 13, 16, 1, 6]
    value0 = 59
    has_sum(value0, collection0)

    # Primera coleccion
    collection1 = [3, 11, 8, 13, 16, 1, 6]
    value1 = 21

    sol11 = [3, 11, 1, 6]
    perm11 = [list(t) for t in itertools.permutations(sol11)]
    perm12 = [[13, 8], [8, 13]]

    # Segunda coleccion
    collection2 = [518533, 1037066, 2074132, 1648264,
                   796528, 1593056, 686112, 1372224,
                   244448, 488896, 977792, 1955584,
                   1411168, 322336, 644672, 1289344,
                   78688, 157376, 314752, 629504, 1259008]
    value2 = 2463098

    sol21 = [1037066, 796528, 629504]
    perm21 = [list(t) for t in itertools.permutations(sol21)]

    # Tercera coleccion
    collection3 = [15, 22, 14, 26, 32, 9, 16, 8]

    value3 = 53

    sol31 = [15, 22, 16]
    perm31 = [list(t) for t in itertools.permutations(sol31)]
    sol32 = [14, 15, 16, 8]
    perm32 = [list(t) for t in itertools.permutations(sol32)]
    sol33 = [9, 22, 14, 8]
    perm33 = [list(t) for t in itertools.permutations(sol33)]

    # Cuarta coleccion
    collection4 = [1, 5, 6]
    value4 = 6
    perm41 = [[6], [1, 5], [5, 1]]

    # Quinta coleccion
    collection5 = [4, 5, 1]
    value5 = 6
    perm51 = [[1, 5], [5, 1]]

    # Sexta coleccion
    collection6 = [6, 400, 100, 6, 10, 20, 30, 40, 3, 4]
    value6 = 7
    perm61 = [[3, 4], [4, 3]]


    assert not has_sum(value0, collection0)
    assert has_sum(value1, collection1)
    assert has_sum(value2, collection2)
    assert has_sum(value3, collection3)
    assert has_sum(value4, collection4)
    assert has_sum(value5, collection5)
    assert has_sum(value6, collection6)


    # #  DESCOMENTAR PARA PROBAR SUBSET
    # ##############################################################
    assert subset(value0, collection0) == [None]
    assert subset(value1, collection1) in perm11 + perm12
    assert subset(value2, collection2) in perm21
    assert subset(value3, collection3) in perm31 + perm32 + perm33
    assert subset(value4, collection4) in perm41
    assert subset(value5, collection5) in perm51
    assert subset(value6, collection6) in perm61

    # # PARA MEDIR TIEMPO USA ESTA COLECCION QUE NO TIENE SUBSECCIONES
    # # QUE SUMEN VALUE6
    # ##################################################################

    collection6 = list(range(1, 27))
    value6 = 409
    assert subset(value6, collection6) == [None]


start_time = time()
test()
elapsed_time = time() - start_time
print("Elapsed time: %0.10f seconds." % elapsed_time)
