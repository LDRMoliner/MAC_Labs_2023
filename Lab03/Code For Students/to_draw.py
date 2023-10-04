import networkx as nx
import matplotlib.pyplot as plt


#Build a graph from its adjacency matrix
def new_format(matrix):
    G = nx.Graph()
    G.add_nodes_from(range(len(matrix)))
    for i in range(len(matrix)):
        for j in range(i+1, len(matrix)):
            if matrix[i][j]==1:
                G.add_edge(i,j)
    return G

#Draw the graph
#Pre: The format must be those returned by the function new_format(graph)    
def draw(graph):
    nx.draw_shell(new_format(graph), with_labels = True)
    plt.show()
    plt.clf()

