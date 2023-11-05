from time import time


# cover es una lista de 0s, 1s y Nones.
# Si i es la posicion de un 1, el i-esimo nodo esta en el cover.
# Si i es la posicion de un 0, el i-esimo nodo no esta en el cover.
# Si i es la posicion de un None, no sabemos si el i-esimo nodo estara en el cover.
#
# partial_validity_check comprueba, dado un posible cover y un grafo,
# si los nodos del cover pueden llegar a cubirir todas las aristas del grafo o no.
def partial_validity_check(cover, graph):
    # TODO: Programa el codigo de la funcion
    for i in range(len(graph)):
        for j in range(len(graph)):
            if graph[i][j] == 1 and cover[i] == 0 and cover[j] == 0:
                return False
    return True


# vertex_cover_tree inicializa y llama al arbol de busqueda
def vertex_cover_tree(graph):
    n = len(graph)
    cover = [None] * n
    return recursive_vertex_cover(graph, cover)


# recursive_vertex_cover construye recursivamente el arbol de busqueda
def recursive_vertex_cover(graph, cover):
    ############
    # TODO: Programa esta parte de la funcion
    #
    # Comprueba es posible construir un cover valido.
    # Si no es posible, devuelve [1]*len(cover).
    # En otro caso, 
    # si el cover esta completo, lo devuelve.
    # Si esta incompleto, encuentra un nodo v que no esta en el cover.

    if (not partial_validity_check(cover, graph)):
        return [1] * len(cover)
    if (None not in cover):
        return cover
    v = cover.index(None)

    # Final de tu codigo
    # Lo siguiente abre las dos ramas del arbol de busqueda.
    # No modificar nada.
    ##############
    copy_cover = list(cover)
    cover[v] = 0
    c0 = recursive_vertex_cover(graph, cover)
    cover = list(copy_cover)
    cover[v] = 1
    c1 = recursive_vertex_cover(graph, cover)
    return c0 if c0.count(1) < c1.count(1) else c1


def test():
    g1 = [[0, 1],
          [1, 0]]

    g2 = [[0, 1, 1],
          [1, 0, 0],
          [1, 0, 0]]

    g3 = [[0, 1, 1, 1, 1],
          [1, 0, 0, 0, 1],
          [1, 0, 0, 1, 1],
          [1, 0, 1, 0, 1],
          [1, 1, 1, 1, 0]]

    g4 = [[0, 1, 1, 1],
          [1, 0, 1, 0],
          [1, 1, 0, 1],
          [1, 0, 1, 0]]

    g5 = [[0, 1, 1, 0, 0, 0],
          [1, 0, 0, 1, 1, 0],
          [1, 0, 0, 1, 1, 1],
          [0, 1, 1, 0, 0, 1],
          [0, 1, 1, 0, 0, 0],
          [0, 0, 1, 1, 0, 0]]

    g6 = [[0, 1, 1, 0, 0, 0, 1, 1, 1, 1, 1, 1, 0, 0, 0],
          [1, 0, 1, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0],
          [1, 1, 0, 1, 1, 0, 1, 0, 1, 0, 0, 1, 0, 0, 0],
          [0, 1, 1, 0, 1, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0],
          [0, 0, 1, 1, 0, 1, 1, 0, 0, 0, 1, 0, 0, 0, 1],
          [0, 0, 0, 1, 1, 0, 1, 1, 0, 0, 0, 0, 0, 1, 0],
          [1, 0, 1, 0, 1, 1, 0, 1, 0, 0, 1, 0, 0, 0, 0],
          [1, 1, 0, 0, 0, 1, 1, 0, 0, 1, 0, 0, 0, 0, 0],
          [1, 0, 1, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 1, 0],
          [1, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 1, 1, 0, 0],
          [1, 0, 0, 0, 1, 0, 1, 0, 1, 0, 0, 1, 0, 1, 1],
          [1, 0, 1, 0, 0, 0, 0, 0, 0, 1, 1, 0, 1, 0, 1],
          [0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 1, 0, 1, 1],
          [0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 1, 0, 1, 0, 1],
          [0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 1, 1, 1, 0]]

    g7 = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0],
          [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0],
          [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0],
          [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0],
          [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0],
          [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0],
          [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0],
          [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0],
          [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0],
          [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0],
          [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0],
          [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1],
          [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0],
          [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0],
          [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0],
          [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0],
          [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0],
          [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0],
          [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0]]

    # #    Descomentar para probar la funcion partial_validity_check
    assert not partial_validity_check([0, 0], g1)
    assert not partial_validity_check([0, 0, 1], g2)
    assert partial_validity_check([1, None, None], g2)
    assert partial_validity_check([0, None, None], g2)
    assert partial_validity_check([1, 0, 0], g2)
    assert partial_validity_check([1, 1, 0], g2)
    assert partial_validity_check([0, 1, None], g2)
    assert not partial_validity_check([0, None, 0], g2)
    assert not partial_validity_check([0, 1, 1, 0, 1, 0], g5)
    assert partial_validity_check([0, 1, 1, 1, 0, 0], g5)
    assert partial_validity_check([1, 0, 1, 1, 0, 1, 1, 1, 0, 1, 1, 0, 1, 1, 1], g6)
    # ##################################################################

    # ##Descomentar para probar la funcion recursive_vertex_cover
    assert vertex_cover_tree(g1) in [[1, 0], [0, 1]]
    assert vertex_cover_tree(g2) == [1, 0, 0]
    assert vertex_cover_tree(g3) in [[1, 0, 1, 0, 1],
                                     [1, 0, 0, 1, 1]]
    assert vertex_cover_tree(g4) == [1, 0, 1, 0]
    assert vertex_cover_tree(g5) in [[0, 1, 1, 1, 0, 0],
                                     [0, 1, 1, 0, 0, 1]]

    assert vertex_cover_tree(g6) in [[1, 0, 1, 1, 0, 1, 1, 1, 0, 1, 1, 0, 1, 1, 1],
                                     [1, 0, 1, 1, 0, 1, 1, 1, 0, 1, 1, 1, 0, 1, 1],
                                     [1, 0, 1, 1, 0, 1, 1, 1, 1, 0, 1, 1, 1, 0, 1],
                                     [1, 0, 1, 1, 0, 1, 1, 1, 1, 1, 1, 0, 1, 0, 1],
                                     [1, 0, 1, 1, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 1],
                                     [1, 0, 1, 1, 1, 0, 1, 1, 0, 1, 1, 1, 0, 1, 1],
                                     [1, 0, 1, 1, 1, 0, 1, 1, 0, 1, 1, 1, 1, 1, 0],
                                     [1, 0, 1, 1, 1, 0, 1, 1, 1, 0, 0, 1, 1, 1, 1],
                                     [1, 0, 1, 1, 1, 0, 1, 1, 1, 0, 1, 1, 1, 1, 0],
                                     [1, 0, 1, 1, 1, 0, 1, 1, 1, 1, 0, 1, 0, 1, 1],
                                     [1, 0, 1, 1, 1, 1, 0, 1, 0, 1, 1, 0, 1, 1, 1],
                                     [1, 0, 1, 1, 1, 1, 0, 1, 0, 1, 1, 1, 0, 1, 1],
                                     [1, 0, 1, 1, 1, 1, 0, 1, 0, 1, 1, 1, 1, 1, 0],
                                     [1, 0, 1, 1, 1, 1, 0, 1, 1, 0, 1, 1, 1, 0, 1],
                                     [1, 0, 1, 1, 1, 1, 0, 1, 1, 0, 1, 1, 1, 1, 0],
                                     [1, 0, 1, 1, 1, 1, 0, 1, 1, 1, 1, 0, 1, 0, 1],
                                     [1, 1, 0, 1, 1, 0, 1, 1, 1, 0, 0, 1, 1, 1, 1],
                                     [1, 1, 0, 1, 1, 0, 1, 1, 1, 0, 1, 1, 1, 1, 0],
                                     [1, 1, 0, 1, 1, 0, 1, 1, 1, 1, 0, 1, 0, 1, 1],
                                     [1, 1, 0, 1, 1, 1, 1, 0, 1, 1, 0, 1, 0, 1, 1],
                                     [1, 1, 1, 0, 1, 1, 0, 1, 0, 1, 1, 0, 1, 1, 1],
                                     [1, 1, 1, 0, 1, 1, 0, 1, 0, 1, 1, 1, 1, 1, 0],
                                     [1, 1, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 1, 0, 1],
                                     [1, 1, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 1, 1, 0],
                                     [1, 1, 1, 0, 1, 1, 0, 1, 1, 1, 1, 0, 1, 0, 1],
                                     [1, 1, 1, 0, 1, 1, 1, 0, 0, 1, 1, 0, 1, 1, 1],
                                     [1, 1, 1, 0, 1, 1, 1, 0, 0, 1, 1, 1, 1, 1, 0],
                                     [1, 1, 1, 0, 1, 1, 1, 0, 1, 1, 1, 0, 1, 0, 1],
                                     [1, 1, 1, 1, 0, 1, 1, 0, 0, 1, 1, 0, 1, 1, 1],
                                     [1, 1, 1, 1, 0, 1, 1, 0, 0, 1, 1, 1, 0, 1, 1],
                                     [1, 1, 1, 1, 0, 1, 1, 0, 1, 1, 1, 0, 1, 0, 1]]

    assert vertex_cover_tree(g7) in [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0]]


start_time = time()
test()
elapsed_time = time() - start_time
print("Elapsed time: %0.10f seconds." % elapsed_time)
