
# Please implement the greedy VERTEX COVER approximation algorithm
# from this unit into a function called greedy_vc:
#
# while not all edges are covered
# choose a vertex with the most uncovered edges
# put that vertex into the vertex cover
#
# As always, the input graph will be given to you as an adjacency
# matrix. The output should be a list containing the vertexes in
# the vertex cover, listed in the order that your function added them
#
# See the test for an example
def is_not_cover(cover, graph):
    for i in range(len(graph)):
        if cover[i] == 1:
            continue
        for j in range(len(graph)):
            if i != j and graph[i][j] == 1 and cover[i] != 1 and cover[j] != 1:
                return True
    return False

def get_uncovered_nodes(cover, node):
    num_uncovered = 0
    for i in range(len(node)):
        if node[i] == 1 and cover[i] != 1:
            num_uncovered += 1
    return num_uncovered


def get_most_uncovered(cover, input_graph):
    least_covered_nodes = -1
    node_index = -1
    for node in range(len(input_graph)):
        if cover[node] == 1:
            continue
        uncovered_nodes = get_uncovered_nodes(cover, input_graph[node])
        if uncovered_nodes > least_covered_nodes:
            least_covered_nodes = uncovered_nodes
            node_index = node
    return node_index


def greedy_vc(input_graph):
    # YOUR CODE HERE
    cover = [None for i in range(len(input_graph))]
    while is_not_cover(cover, input_graph):
        node_index = get_most_uncovered(cover, input_graph)
        cover[node_index] = 1
    index_cover = []
    for i in range(len(cover)):
        if cover[i] == 1:
            index_cover.append(i)
    return index_cover


def test():
    graph = [[0, 1, 1, 1, 1],
             [1, 0, 0, 0, 1],
             [1, 0, 0, 1, 1],
             [1, 0, 1, 0, 1],
             [1, 1, 1, 1, 0]]
    cover = greedy_vc(graph)
    # There are multiple possible right answers
    assert (cover == [0, 4, 2] or
            cover == [0, 2, 4] or
            cover == [0, 4, 3] or
            cover == [4, 0, 2] or
            cover == [4, 0, 3])

test()