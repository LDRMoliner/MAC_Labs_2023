from math import inf



# algoritmo voraz de Dijkstra
def Dijkstra (graph, initial):
    sol = [0] * (len(graph))
    visitados = [False] * (len(graph))
    unvisited_nodes = True
    minimum = inf
    for v in range(len(graph)):
        sol[v] = graph[initial][v]
        visitados[v] = False
    sol[initial] = 0
    visitados[initial] = True

    while unvisited_nodes:
        index = -1
        minimum = inf
        for visited in range(len(visitados)):
            if not visitados[visited] and sol[visited] < minimum:
                minimum = sol[visited]
                index = visited
        visitados[index] = True

        unvisited_nodes = False
        for n in range(len(graph)):
            if sol[n] > sol[index] + graph[index][n]:
                sol[n] = sol[index] + graph[index][n]
            if not visitados[n]:
                unvisited_nodes = True
    return sol






def test():
    
    g0 =  [[inf, 5.0, 1.0, inf],
          [5.0, inf, 1.0, 2.0],
          [1.0, 1.0, inf, 10.0],
          [inf, 2.0, 10.0, inf]]
    
    assert Dijkstra(g0, 3) == [4.0, 2.0, 3.0, 0.0]
    
    g1 =  [[inf, 2.0],
           [2.0, inf]]
    
    assert Dijkstra(g1,0) == [0.0,2.0]
    
    g2 = [[inf, 5.0, 3.0],
         [5.0, inf, inf],
         [3.0, inf, inf]]
    
    assert Dijkstra(g2, 1) == [5.0, 0.0, 8.0]
        
     
    g3 = [[inf, 1.0, 2.0, 3.0, 4.0],
          [1.0, inf, inf, inf, 8.0],
          [2.0, inf, inf, 2.0, 2.0],
          [3.0, inf, 2.0, inf, 5.0],
          [4.0, 8.0, 2.0, 5.0, inf]]
    
    assert Dijkstra(g3, 3) == [3.0, 4.0, 2.0, 0.0, 4.0]
        
    g4 = [[inf, 6.0, 2.0, 5.0],
          [6.0, inf, 4.0, inf],
          [2.0, 4.0, inf, 2.0],
          [5.0, inf, 2.0, inf]]
    
    assert Dijkstra(g4, 3) == [4.0, 6.0, 2.0, 0.0]
    
    g5 = [[inf, 10.0, 1.0, inf, inf, inf],
          [10.0, inf, inf, 5.0, 4.0, inf],
          [1.0, inf, inf, 8.0, 2.0, 3.0],
          [inf, 5.0, 8.0, inf, inf, 2.0],
          [inf, 4.0, 2.0, inf, inf, inf],
          [inf, inf, 3.0, 2.0, inf, inf]]
    
    assert Dijkstra(g5, 0) == [0.0, 7.0, 1.0, 6.0, 3.0, 4.0]
    
    
    g6 = [[inf, 3.0, 1.0, inf, inf, inf, inf],
          [3.0, inf, 8.0, 10.0, 5.0, inf, inf],
          [1.0, 8.0, inf, inf, inf, inf, inf],
          [inf, 10.0, inf, inf, 6.0, inf, 9.0],
          [inf, 5.0, inf, 6.0, inf, 1.0, 2.0],
          [inf, inf, inf, inf, 1.0, inf, 4.0],
          [inf,inf,inf, 9.0, 2.0, 4.0, inf]]
    
    assert Dijkstra(g6, 3)  == [13.0, 10.0, 14.0, 0.0, 6.0, 7.0, 8.0]
    
test()    