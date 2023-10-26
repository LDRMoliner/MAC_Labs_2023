import itertools

def is_vertex_cover(adjacency_matrix, nodes):
    for i in range(len(adjacency_matrix)):
        for j in range(len(adjacency_matrix[i])):
            if adjacency_matrix[i][j] == 1 and i not in nodes and j not in nodes:
                return False
    return True

def solve_vc(adjacency_matrix):
    num_nodes = len(adjacency_matrix)
    smallest_vertex_cover = None

    for k in range(num_nodes + 1):
        # Generate all possible combinations of k nodes
        node_combinations = itertools.combinations(range(num_nodes), k)
        for nodes in node_combinations:
            if is_vertex_cover(adjacency_matrix, nodes):
                if smallest_vertex_cover is None or len(nodes) < len(smallest_vertex_cover):
                    smallest_vertex_cover = nodes
    return [1 if i in smallest_vertex_cover else 0 for i in range(num_nodes)]