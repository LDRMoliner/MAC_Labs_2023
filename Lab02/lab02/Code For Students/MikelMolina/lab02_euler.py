
def tiene_1s_pares(g):
    unos = 0;
    for elem in g:
        if elem == 1:
            unos+=1
    return unos % 2 == 0


# Coste: O(n²)
def graph_has_Eulerian_circuit(g):
    # TODO:
    # Programar el codigo esta funcion
    # Puedes definir funciones auxiliares si lo estimas oportuno
    for elem in g:
        if (not tiene_1s_pares(elem)):
            return False

    return True
    
    
def test():
    g1 = [[0, 1, 1, 0, 0],
          [1, 0, 1, 1, 1],
          [1, 1, 0, 1, 1],
          [0, 1, 1, 0, 1],
          [0, 1, 1, 1, 0]]
    assert not graph_has_Eulerian_circuit(g1)


    g2 = [[0, 1, 1, 0, 0, 0],
          [1, 0, 1, 1, 1, 0],
          [1, 1, 0, 1, 1, 0],
          [0, 1, 1, 0, 1, 1],
          [0, 1, 1, 1, 0, 1],
          [0, 0, 0, 1, 1, 0]]
    
    assert graph_has_Eulerian_circuit(g2)

    g3 = [[0, 1, 1, 0, 0, 0, 0, 0],
          [1, 0, 1, 1, 0, 1, 1, 1],
          [1, 1, 0, 0, 1, 1, 1, 1],
          [0, 1, 0, 0, 0, 1, 0, 0],
          [0, 0, 1, 0, 0, 0, 1, 0],
          [0, 1, 1, 1, 0, 0, 1, 1],
          [0, 1, 1, 0, 1, 1, 0, 1],
          [0, 1, 1, 0, 0, 1, 1, 0]]
    
    assert not graph_has_Eulerian_circuit(g3)
    
    g4 = [[0, 1, 1, 0, 0, 0, 0, 0, 0, 0],
          [1, 0, 1, 1, 1, 1, 1, 0, 0, 0],
          [1, 1, 0, 0, 1, 1, 1, 0, 1, 0],
          [0, 1, 0, 0, 0, 1, 0, 0, 0, 0],
          [0, 1, 1, 0, 0, 1, 1, 0, 0, 0],
          [0, 1, 1, 1, 1, 0, 1, 1, 0, 0],
          [0, 1, 1, 0, 1, 1, 0, 1, 0, 1],
          [0, 0, 0, 0, 0, 1, 1, 0, 0, 0],
          [0, 0, 1, 0, 0, 0, 0, 0, 0, 1],
          [0, 0, 0, 0, 0, 0, 1, 0, 1, 0]]
    
    assert graph_has_Eulerian_circuit(g4)
    
    g5 = [[0, 1, 0, 0],
          [1, 0, 1, 0],
          [0, 1, 0, 1],
          [0, 0, 1, 0]]
    
    assert not graph_has_Eulerian_circuit(g5)
    

    g6 = [[0, 1, 1, 0, 0, 0],
          [1, 0, 0, 1, 1, 0],
          [1, 0, 0, 1, 1, 1],
          [0, 1, 1, 0, 0, 1],
          [0, 1, 1, 0, 0, 0],
          [0, 0, 1, 1, 0, 0]]
    
    assert not graph_has_Eulerian_circuit(g6)
    
    g7 = [[0, 1, 0, 0],
          [1, 0, 1, 0],
          [0, 1, 0, 1],
          [0, 0, 1, 0]]
    
    assert not graph_has_Eulerian_circuit(g7)
    
    g8 = [[0, 1, 1, 1, 1, 1, 1, 1, 1, 0],
          [1, 0, 1, 1, 1, 1, 1, 1, 1, 0],
          [1, 1, 0, 1, 1, 1, 1, 1, 1, 0],
          [1, 1, 1, 0, 1, 1, 1, 1, 1, 0],
          [1, 1, 1, 1, 0, 1, 1, 1, 1, 0],
          [1, 1, 1, 1, 1, 0, 1, 1, 1, 0],
          [1, 1, 1, 1, 1, 1, 0, 1, 1, 0],
          [1, 1, 1, 1, 1, 1, 1, 0, 1, 0],
          [1, 1, 1, 1, 1, 1, 1, 1, 0, 1],
          [0, 0, 0, 0, 0, 0, 0, 0, 1, 0]]
     
    
    assert not graph_has_Eulerian_circuit(g8)    

test()

