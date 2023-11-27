from pysat.solvers import Solver
from pysat.process import Processor


def son_similares(clause1, clause2):
    clause1_set_abs = set(map(abs, clause1))
    clause2_set_abs = set(map(abs, clause2))

    comunes_absoluto = clause1_set_abs.intersection(clause2_set_abs)

    if sum(1 for num in clause1 if num > 0) == 3:
        return len(comunes_absoluto) == 3 and sum(1 for num in clause2 if num < 0) == 2
    if sum(1 for num in clause1 if num < 0) == 3:
        return len(comunes_absoluto) == 3 and sum(1 for num in clause2 if num > 0) == 2
    # Check if there are at least two numbers with the same sign
    return len(comunes_absoluto) == 3 and (sum(1 for num in clause1 if num > 0) == 2 or
                                           sum(1 for num in clause1 if num < 0) == 2)


def eliminar_similares(clauses):
    i = 0
    j = 1
    new_clauses = list(clauses)
    while j < len(clauses):
        if son_similares(clauses[i], clauses[j]):
            new_clauses.remove(clauses[j])
        j += 1
        i += 1
    return new_clauses


def eliminar_iguales(clauses):
    unique_lists = []

    for clause in clauses:
        # Sort the literals and convert to a tuple for uniqueness checking
        sorted_clause = sorted(clause)

        if sorted_clause not in unique_lists:
            unique_lists.append(sorted_clause)

    return unique_lists


borja = [[39, 40, 1], [-39, -40, 1], [39, -40, -1], [-39, 40, -1],
         [1, 41, 2], [-1, -41, 2], [1, -41, -2], [-1, 41, -2],
         [2, 42, 3], [-2, -42, 3], [2, -42, -3], [-2, 42, -3],
         [3, 43, 4], [-3, -43, 4], [3, -43, -4], [-3, 43, -4],
         [4, 44, 5], [-4, -44, 5], [4, -44, -5], [-4, 44, -5],
         [5, 45, 6], [-5, -45, 6], [5, -45, -6], [-5, 45, -6],
         [6, 46, 7], [-6, -46, 7], [6, -46, -7], [-6, 46, -7],
         [7, 47, 8], [-7, -47, 8], [7, -47, -8], [-7, 47, -8],
         [8, 48, 9], [-8, -48, 9], [8, -48, -9], [-8, 48, -9],
         [9, 49, 10], [-9, -49, 10], [9, -49, -10], [-9, 49, -10],
         [10, 50, 11], [-10, -50, 11], [10, -50, -11],
         [-10, 50, -11], [11, 51, 12], [-11, -51, 12],
         [11, -51, -12], [-11, 51, -12], [12, 52, 13],
         [-12, -52, 13], [12, -52, -13], [-12, 52, -13],
         [13, 53, 14], [-13, -53, 14], [13, -53, -14],
         [-13, 53, -14], [14, 54, 15], [-14, -54, 15],
         [14, -54, -15], [-14, 54, -15], [15, 55, 16],
         [-15, -55, 16], [15, -55, -16], [-15, 55, -16],
         [16, 56, 17], [-16, -56, 17], [16, -56, -17],
         [-16, 56, -17], [17, 57, 18], [-17, -57, 18],
         [17, -57, -18], [-17, 57, -18], [18, 58, 19],
         [-18, -58, 19], [18, -58, -19], [-18, 58, -19],
         [19, 59, 60], [-19, -59, 60], [19, -59, -60],
         [-19, 59, -60], [20, 59, 60], [-20, -59, 60],
         [20, -59, -60], [-20, 59, -60], [21, 58, 20],
         [-21, -58, 20], [21, -58, -20], [-21, 58, -20],
         [22, 57, 21], [-22, -57, 21], [22, -57, -21],
         [-22, 57, -21], [23, 56, 22], [-23, -56, 22],
         [23, -56, -22], [-23, 56, -22], [24, 55, 23],
         [-24, -55, 23], [24, -55, -23], [-24, 55, -23],
         [25, 54, 24], [-25, -54, 24], [25, -54, -24],
         [-25, 54, -24], [26, 53, 25], [-26, -53, 25],
         [26, -53, -25], [-26, 53, -25], [27, 52, 26],
         [-27, -52, 26], [27, -52, -26], [-27, 52, -26],
         [28, 51, 27], [-28, -51, 27], [28, -51, -27],
         [-28, 51, -27], [29, 50, 28], [-29, -50, 28],
         [29, -50, -28], [-29, 50, -28], [30, 49, 29],
         [-30, -49, 29], [30, -49, -29], [-30, 49, -29],
         [31, 48, 30], [-31, -48, 30], [31, -48, -30],
         [-31, 48, -30], [32, 47, 31], [-32, -47, 31],
         [32, -47, -31], [-32, 47, -31], [33, 46, 32],
         [-33, -46, 32], [33, -46, -32], [-33, 46, -32],
         [34, 45, 33], [-34, -45, 33], [34, -45, -33],
         [-34, 45, -33], [35, 44, 34], [-35, -44, 34],
         [35, -44, -34], [-35, 44, -34], [36, 43, 35],
         [-36, -43, 35], [36, -43, -35], [-36, 43, -35],
         [37, 42, 36], [-37, -42, 36], [37, -42, -36],
         [-37, 42, -36], [38, 41, 37], [-38, -41, 37],
         [38, -41, -37], [-38, 41, -37], [39, 40, -38],
         [-39, -40, -38], [39, -40, 38], [-39, 40, 38]]

borjagoras = [[2, 1, 3], [-2, -1, 3], [-2, 3, -1], [-2, -1, 3],
              [2, 3, 1], [-1, 3, -2], [-3, 2, 1], [1, -3, -2],
              [-2, -1, 3], [1, -2, -3], [-2, -1, 3], [-1, -2, -3],
              [3, -2, 1], [2, 1, 3], [-3, -1, 2], [-3, -2, 1],
              [-1, 3, -2], [1, 2, -3], [-3, -1, 2], [2, -1, 3]]

print("Antes:")
print(borjagoras)
print(len(borjagoras))
print("Ahora:")
print(eliminar_similares(borjagoras))
processor = Processor([[2, 1, 3], [-2, -1, 3], [-2, 3, -1], [-2, -1, 3],
                       [2, 3, 1], [-1, 3, -2], [-3, 2, 1], [1, -3, -2],
                       [-2, -1, 3], [1, -2, -3], [-2, -1, 3], [-1, -2, -3],
                       [3, -2, 1], [2, 1, 3], [-3, -1, 2], [-3, -2, 1],
                       [-1, 3, -2], [1, 2, -3], [-3, -1, 2], [2, -1, 3]])
processed = processor.process(rounds=1, block=False, cover=False, condition=False, decompose=False, elim=False,
                              probe=True,
                              probehbr=False, subsume=False, vivify=False)
print(processed.clauses)
print(len(processed.clauses))
