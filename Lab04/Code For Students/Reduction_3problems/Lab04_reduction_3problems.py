from vertex_cover import solve_vc



def multisolve(graph, problem):    
    #TODO
    

def test():
   graph = [[0, 0, 1, 0], 
            [0, 0, 0, 1], 
            [1, 0, 0, 1], 
            [0, 1, 1, 0]]
   
   
   sol_vertex = multisolve(graph, "VERTEX COVER")
   sol_clique = multisolve(graph, "CLIQUE")
   sol_independent_set =  multisolve(graph, "INDEPENDENT SET")
   
   assert sol_vertex in [[0,0,1,1], [1,0,0,1], [0,1,1,0]]
   assert sol_independent_set in [[1,0,0,1],[1,1,0,0],[0,1,1,0]]
   assert sol_clique in [[1,0,1,0],[0,0,1,1],[0,1,0,1]]
   
   graph = [[0,1,1],[1,0,1],[1,1,0]]
   
   
   sol_vertex = multisolve(graph, "VERTEX COVER")
   sol_clique = multisolve(graph, "CLIQUE")
   sol_independent_set =  multisolve(graph, "INDEPENDENT SET")
     
   assert sol_vertex in [[0,1,1], [1,0,1], [1,1,0]]
   assert sol_independent_set in [[1,0,0],[0,1,0],[0,0,1]]
   assert sol_clique in [[1,1,1]]

   graph = [[0,1,1,1,1,1,1],
            [1,0,1,0,0,0,1],
            [1,1,0,1,0,0,0],
            [1,0,1,0,1,0,0],
            [1,0,0,1,0,1,0],
            [1,0,0,0,1,0,1],
            [1,1,0,0,0,0,1]]   
   
   sol_vertex = multisolve(graph, "VERTEX COVER")
   sol_clique = multisolve(graph, "CLIQUE")
   sol_independent_set =  multisolve(graph, "INDEPENDENT SET")
   
   assert sol_vertex in [[1,1,0,1,0,1,0], [1,0,1,0,1,0,1]]
   assert sol_independent_set in  [[0,1,0,1,0,1,0], [0,0,1,0,1,0,1]]
   assert sol_clique in  [[1,1,0,0,0,0,1], [1,1,1,0,0,0,0],[1,0,1,1,0,0,0],
                          [1,0,0,1,1,0,0],[1,0,0,0,1,1,0],[1,0,0,0,0,1,1]]

test()

