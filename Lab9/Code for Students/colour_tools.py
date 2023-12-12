from pysat.solvers import Mergesat3
import matplotlib.pyplot as plt
import networkx as nx

def positive2var(n):
    node = (n-1)//3
    color = (n-1)%3
    return (node, color)
    

#Graph Visualization
def visualizeGXGraph(graph, cnf):
    
    # crea el solver
    solver = Mergesat3(bootstrap_with=cnf)
   
    # llama al solver
    solver.solve()
   
    # obtiene una asignación
    assignment = solver.get_model()

    #para visualizar
    G = fromAdjacencyToGX(graph)
    
    if assignment == None:
        print("NOT SATISFIABLE -> CANNOT GRAPHICALLY REPRESENT GRAPH")
    else:
        print("DISPLAYING GRAPH FOR: ")
        color_map = [0]*(len(graph))
        for value in list(assignment):
            if value > 0:
                color_map[positive2var(value)[0]] = positive2var(value)[1]
     
        nx.draw(G, node_color = color_map, with_labels = True)
    
        plt.show()
    
        
        
#From adjacency matrix to GX graph, plot included
def fromAdjacencyToGX(graph):
    GX_nodes = []
    for i in range(0, len(graph)):
        for j in range(i+1, len(graph)):
            if graph[i][j]==1:
                GX_nodes.append([i, j])
                
    nodes = set([n1 for n1, n2 in GX_nodes] + [n2 for n1, n2 in GX_nodes])

    G = nx.Graph()
    # add nodes
    for node in nodes:
        G.add_node(node)    
    # add edges
    for edge in GX_nodes:
        G.add_edge(edge[0], edge[1])
    return G

