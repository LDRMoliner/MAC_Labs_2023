def isSafe(g, v, colour, c):
    for i in range(len(g[v])):
        if g[v][i] == 1 and colour[i] == c:
            return False

    return True


def graphColourUtil(g, m, colour, v, length):
    if v == length:
        return True
    else:
        for c in range(m):
            if isSafe(g, v, colour, c):
                colour[v] = c
                return graphColourUtil(g, m, colour, v + 1, length)

        return False


def graph_is_mcolorable(g, m):
    length = len(g[0])
    colour = []
    for i in range(length):
        colour.append(-1)

    return graphColourUtil(g, m, colour, 0, length)


def graph_is_4colorable(g):
    return graph_is_mcolorable(g, 4)

