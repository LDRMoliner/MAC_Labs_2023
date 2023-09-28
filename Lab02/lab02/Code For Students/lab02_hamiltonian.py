from itertools import permutations

def es_circuito_euleriano(prueba, g):
    i = 0;
    while (i < len(prueba) - 1):
        if (g[prueba[i]][prueba[i+1]] == 0):
            return False
        i+=1
    if (g[prueba[len(prueba) - 1]][prueba[0]] == 1):
        return True
    return False


#Coste exponencial.
def graph_has_Hamiltonian_circuit(g):
    # g is a conected nondirected graph
    # decides whether g has a Hamiltonian circuit
    
    asignaciones = permutations(list(range(len(g))))
    
    #TODO

    for elem in asignaciones:
        if (es_circuito_euleriano(elem, g)):
            return True

def test():
    g1 = [[0, 1, 1, 0, 0],
          [1, 0, 1, 1, 1],
          [1, 1, 0, 1, 1],
          [0, 1, 1, 0, 1],
          [0, 1, 1, 1, 0]]
    assert graph_has_Hamiltonian_circuit(g1)


    g2 = [[0, 1, 1, 0, 0, 0],
          [1, 0, 1, 1, 1, 0],
          [1, 1, 0, 1, 1, 0],
          [0, 1, 1, 0, 1, 1],
          [0, 1, 1, 1, 0, 1],
          [0, 0, 0, 1, 1, 0]]
    
    assert graph_has_Hamiltonian_circuit(g2)

    g3 = [[0, 1, 1, 0, 0, 0, 0, 0],
          [1, 0, 1, 1, 0, 1, 1, 1],
          [1, 1, 0, 0, 1, 1, 1, 1],
          [0, 1, 0, 0, 0, 1, 0, 0],
          [0, 0, 1, 0, 0, 0, 1, 0],
          [0, 1, 1, 1, 0, 0, 1, 1],
          [0, 1, 1, 0, 1, 1, 0, 1],
          [0, 1, 1, 0, 0, 1, 1, 0]]
    
    assert graph_has_Hamiltonian_circuit(g3)
    
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
    
    assert not graph_has_Hamiltonian_circuit(g4)
    
    g5 = [[0, 1, 1, 0, 0, 0],
          [1, 0, 0, 1, 1, 0],
          [1, 0, 0, 1, 1, 1],
          [0, 1, 1, 0, 0, 1],
          [0, 1, 1, 0, 0, 0],
          [0, 0, 1, 1, 0, 0]]
    
    assert not graph_has_Hamiltonian_circuit(g5)
    
    g6 = [[0, 1, 0, 0],
          [1, 0, 1, 0],
          [0, 1, 0, 1],
          [0, 0, 1, 0]]
    
    assert not graph_has_Hamiltonian_circuit(g6)
    
    g7 = [[0, 1, 1, 1, 1, 1, 1, 1, 1, 0],
          [1, 0, 1, 1, 1, 1, 1, 1, 1, 0],
          [1, 1, 0, 1, 1, 1, 1, 1, 1, 0],
          [1, 1, 1, 0, 1, 1, 1, 1, 1, 0],
          [1, 1, 1, 1, 0, 1, 1, 1, 1, 0],
          [1, 1, 1, 1, 1, 0, 1, 1, 1, 0],
          [1, 1, 1, 1, 1, 1, 0, 1, 1, 0],
          [1, 1, 1, 1, 1, 1, 1, 0, 1, 0],
          [1, 1, 1, 1, 1, 1, 1, 1, 0, 1],
          [0, 0, 0, 0, 0, 0, 0, 0, 1, 0]]
     
    
    assert not graph_has_Hamiltonian_circuit(g7)    

test()

