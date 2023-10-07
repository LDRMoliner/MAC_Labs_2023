from vertex_cover import solve_vc

def get_complementary_graph(graph):
    return [[1 if elem == 0 and not row_index == index else 0 for index, elem in enumerate(row)] for row_index, row in enumerate(graph)]

def get_independent_set (graph):
    sol = solve_vc(graph)
    return [1 if num == 0 else 0 for num in sol]
def get_clique(graph):
    comp_graph = get_complementary_graph(graph)
    return get_independent_set(comp_graph)


def multisolve(graph, problem):
    #TODO
    if (problem == "VERTEX COVER"):
        return solve_vc(graph)
    if (problem == "CLIQUE"):
        return get_clique(graph)
    if (problem == "INDEPENDENT SET"):
        return get_independent_set(graph)
    return 0

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

