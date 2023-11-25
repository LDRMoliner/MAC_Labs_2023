from time import time
from sat_generator import generate_formula
from tools import list_minisat2list_our_sat

def remove_trivial_clauses(clauses):
    return [clause for clause in clauses if not any(lit in clause and -lit in clause for lit in clause)]


def remove_false(clause, assignment):
    if not clause:
        return []
    first_literal = clause[0]
    if assignment[abs(first_literal)] is not None:
        if (first_literal < 0 and assignment[abs(first_literal)] == 1) or (
                first_literal > 0 and assignment[abs(first_literal)] == 0):
            return remove_false(clause[1:], assignment)
    return [first_literal] + remove_false(clause[1:], assignment)


def remove_false_literals(clauses, assignment):
    for i in range(len(clauses)):
        clauses[i] = remove_false(clauses[i], assignment)


def remove_true_clauses(clauses, assignment):
    if not clauses:
        return []
    first_clause = clauses[0]
    for lit in first_clause:
        if assignment[abs(lit)] is None:
            continue
        if (lit < 0 and not assignment[abs(lit)]) or (lit > 0 and assignment[abs(lit)]):
            return remove_true_clauses(clauses[1:], assignment)
    return [first_clause] + remove_true_clauses(clauses[1:], assignment)


def set_only_one_variable(num_variables, clauses, assignment):
    numbers = [[0, False] for _ in range(num_variables + 1)]
    i = 0
    appearances = 0
    for clause in clauses:
        while i < num_variables:
            appearances = 0
            i += 1
            appearances += clause.count(i)
            if appearances > 0:
                numbers[i][1] = True
                numbers[i][0] += appearances

                continue
            appearances += clause.count(-i)
            if appearances > 0:
                numbers[i][1] = False
                numbers[i][0] += appearances
        i = 0
    while i < num_variables:
        i += 1
        if numbers[i][0] == 1:
            assignment[i] = 1 if numbers[i][1] else 0


def assign_lonely_variables(clauses, assignment):
    for clause in clauses:
        if len(clause) == 1:
            if clause[0] < 0:
                assignment[abs(clause[0])] = 0
            else:
                assignment[abs(clause[0])] = 1


def sat_preprocessing(num_variables, clauses, assignment):
    # Rule 0
    update = True
    while update:
        # TODO
        # usa funciones auxiliares
        clauses_old = clauses
        assign_lonely_variables(clauses, assignment)
        set_only_one_variable(num_variables, clauses, assignment)
        clauses = remove_true_clauses(clauses, assignment)
        remove_false_literals(clauses, assignment)
        update = not (clauses_old == clauses)
        if [] in clauses:
            return ([[1], [-1]], assignment)
        else:
            if (clauses == []) or (not update):
                return (clauses, assignment)


def solve_SAT(num_variables, clauses):
    asig = [None] * (num_variables + 1)
    # Rule 0
    clauses = remove_trivial_clauses(clauses)
    clauses, asig = sat_preprocessing(num_variables, clauses, asig)
    if clauses == [[1], [-1]]:
        return "UNSATISFIABLE"
    return solve_SAT_rec(clauses, asig)


def solve_SAT_rec(clauses, asig):
    _, satisfied = eval_3CNF(asig, clauses)

    # Si la asignación es verdadera, la devolvemos.
    if satisfied:
        return asig

    # Si ya no quedan None, insatisfactible.
    if None not in asig[1:]:
        return "UNSATISFIABLE"

    index_to_change = asig.index(None, 1)
    pair_found = None in asig[index_to_change:]

    if pair_found:
        index2_to_change = asig.index(None, index_to_change)
    else:
        copy2_asig = list(asig)
        copy2_asig[index_to_change] = 0
        if eval_3CNF(clauses, copy2_asig) != "UNSATISFIABLE":
            return asig
        copy2_asig[index_to_change] = 1
        if eval_3CNF(clauses, copy2_asig) != "UNSATISFIABLE":
            return asig
        return "UNSATISFIABLE"

    # Abrimos tres ramas.

    copy_asig = list(asig)
    asig[index_to_change] = 0
    asig[index2_to_change] = 1
    asig1 = solve_SAT_rec(clauses, asig)

    asig = list(copy_asig)
    asig[index_to_change] = 1
    asig[index2_to_change] = 0
    asig2 = solve_SAT_rec(clauses, asig)

    asig = list(copy_asig)
    asig[index_to_change] = 1
    asig[index2_to_change] = 1
    asig3 = solve_SAT_rec(clauses, asig)

    if asig1 != "UNSATISFIABLE":
        return asig1
    if asig2 != "UNSATISFIABLE":
        return asig2
    if asig3 != "UNSATISFIABLE":
        return asig3
    return "UNSATISFIABLE"

def solve_SAT_rec(clauses, asig):
    _, satisfied = eval_3CNF(asig, clauses)

    # Si la asignación es verdadera, la devolvemos.
    if satisfied:
        return asig

    # Si ya no quedan None, insatisfactible.
    if None not in asig[1:]:
        return "UNSATISFIABLE"

    index_to_change = asig.index(None, 1)
    pair_found = None in asig[index_to_change:]

    if pair_found:
        index2_to_change = asig.index(None, index_to_change)
    else:
        copy2_asig = list(asig)
        copy2_asig[index_to_change] = 0
        if eval_3CNF(clauses, copy2_asig) != "UNSATISFIABLE":
            return asig
        copy2_asig[index_to_change] = 1
        if eval_3CNF(clauses, copy2_asig) != "UNSATISFIABLE":
            return asig
        return "UNSATISFIABLE"

    # Abrimos tres ramas.

    copy_asig = list(asig)
    asig[index_to_change] = 0
    asig[index2_to_change] = 1
    asig1 = solve_SAT_rec(clauses, asig)

    asig = list(copy_asig)
    asig[index_to_change] = 1
    asig[index2_to_change] = 0
    asig2 = solve_SAT_rec(clauses, asig)

    asig = list(copy_asig)
    asig[index_to_change] = 1
    asig[index2_to_change] = 1
    asig3 = solve_SAT_rec(clauses, asig)

    if asig1 != "UNSATISFIABLE":
        return asig1
    if asig2 != "UNSATISFIABLE":
        return asig2
    if asig3 != "UNSATISFIABLE":
        return asig3
    return "UNSATISFIABLE"

def eval_clause(clause, assignment):
    for i in range(len(clause)):
        if not clause[i]:
            continue
        if clause[i] < 0 and assignment[abs(clause[i])] == 0:
            return True
        if clause[i] > 0 and assignment[abs(clause[i])] == 1:
            return True
    return False


def eval_3CNF(assignment, clauses):
    for i in range(len(clauses)):
        if not eval_clause(clauses[i], assignment):
            return i, False
    return None, True


def test1():
    print("Primera clausula")
    clauses = [[1, 2], [1, -2]]
    solutions = [[0, 1, 0],
                 [0, 1, 1],
                 [0, 1, None],
                 [1, 1, 0],
                 [1, 1, 1],
                 [1, 1, None],
                 [None, 1, 0],
                 [None, 1, 1],
                 [None, 1, None]]
    assert solve_SAT(2, clauses) in solutions

    print("Segunda clausula")

    clauses = [[1, -2, -3], [2, -3, 1], [3, -2, 1],
               [2, 3, 1]]
    solutions = [[0, 1, 0, 0],
                 [0, 1, 0, 1],
                 [0, 1, 1, 0],
                 [0, 1, 1, 1],
                 [1, 1, 0, 0],
                 [1, 1, 0, 1],
                 [1, 1, 1, 0],
                 [1, 1, 1, 1],
                 [None, 1, 0, 0],
                 [None, 1, 0, 1],
                 [None, 1, 1, 0],
                 [None, 1, 1, 1],
                 [None, 1, None, None]]
    assert solve_SAT(3, clauses) in solutions

    print("Tercera clausula")
    clauses = [[2, 1, 3], [-2, -1, 3], [-2, 3, -1], [-2, -1, 3],
               [2, 3, 1], [-1, 3, -2], [-3, 2, 1], [1, -3, -2],
               [-2, -1, 3], [1, -2, -3], [-2, -1, 3], [-1, -2, -3],
               [3, -2, 1], [2, 1, 3], [-3, -1, 2], [-3, -2, 1],
               [-1, 3, -2], [1, 2, -3], [-3, -1, 2], [2, -1, 3]]
    assert solve_SAT(3, clauses) == "UNSATISFIABLE"

    clauses = [[4, -18, 19], [3, 18, -5], [-5, -8, -15], [-20, 7, -16], [10, -13, -7],
               [-12, -9, 17], [17, 19, 5], [-16, 9, 15], [11, -5, -14], [18, -10, 13],
               [-3, 11, 12], [-6, -17, -8], [-18, 14, 1], [-19, -15, 10], [12, 18, -19],
               [-8, 4, 7], [-8, -9, 4], [7, 17, -15], [12, -7, -14], [-10, -11, 8],
               [2, -15, -11], [9, 6, 1], [-11, 20, -17], [9, -15, 13], [12, -7, -17],
               [-18, -2, 20], [20, 12, 4], [19, 11, 14], [-16, 18, -4], [-1, -17, -19],
               [-13, 15, 10], [-12, -14, -13], [12, -14, -7], [-7, 16, 10], [6, 10, 7],
               [20, 14, -16], [-19, 17, 11], [-7, 1, -20], [-5, 12, 15], [-4, -9, -13],
               [12, -11, -7], [-5, 19, -8], [-16], [20, -14, -15], [13, -4, 10],
               [14, 7, 10], [-5, 9, 20], [10, 1, -19], [-16, -15, -1], [16, 3, -11],
               [-15, -10, 4], [4, -15, -3], [-10, -16, 11], [-8, 12, -5], [14, -6, 12],
               [1, 6, 11], [-13, -5, -1], [-12], [1, -20, 19], [-2, -13, -8],
               [18], [-11, 14, 9], [-6, -15, -2], [-5], [-6, 17, 5],
               [-13, 5, -19], [20, -1, 14], [9, -17, 15], [-5, 19, -18], [-12, 8, -10],
               [-18, 14, -4], [15, -9, 13], [9, -5, -1], [10, -19, -14], [20, 9, 4],
               [-9, -2, 19], [-5, 13, -17], [2, -10, -18], [-18, 3, 11], [7, -9, 17],
               [-15, -6, -3], [-2, 3, -13], [12, 3, -2], [2, -2, -3, 17], [20, -15, -16],
               [-5, -17, -19], [-20, -18, 11], [-9, 1, -5], [-19, 9, 17], [17], [1],
               [4, -16, -5]]
    assert solve_SAT(20, clauses) == "UNSATISFIABLE"

    print("Cuarta clausula")
    clauses = [[15, 4, -3], [-14, -15, 5], [-19, -16, 17], [7, 18, -5], [-14, -16, 12], [-16, -9, 18],
               [9, 16, 4], [-10, 18, 5], [-11, 4, 2], [-6, -12, -16], [12, 3, 5], [-1, -12, -18],
               [8, -15, 11], [-1, 5, 13], [-10, -4, -15], [-17, 1, -15], [3, 12, 17], [17, 2, 19],
               [7, 1, -17], [9, 15, -19], [-8, 2, -16], [7, -2, 17], [-3, 11, -6], [-11, 10, -3],
               [15, -13, -3], [5, -16, -9], [8, 15, 11], [12, 14, -18], [12, -8, 19], [-15, 4, -8],
               [8, 9, -1], [-17, -12, -18], [-2, -3, 8], [-3, 4, -1], [15, 2, 19], [-3, -8, -6],
               [12, 17, 2], [-11, 12, 1], [12, -9, -8], [-7, -14, 2], [10, 14, -11], [-2, 17, 14],
               [-17, 15, 1], [19, 2, 7], [18, -16, -7], [-7, -1, 13], [1, 19, -7], [18, 2, -3],
               [15, -3, 1], [10, 14, -12], [15, -3, -2], [1, -18, -2], [18, -3, -13], [2, 16, 6],
               [10, -5, -15], [-13, -1, -16], [-4, -6, -11], [-15, 4, 1], [-12, -16, 5], [-10, 4, -2],
               [-10, 1, 6], [-3, 13, -19], [5, -8, -11], [11, 6, -12], [7, 15, -8], [6, 1, -5],
               [-7, 1, -19], [18, -4, -7], [6, 16, 5], [-8, 19, 2], [13, 4, 11], [-10, -13, -19],
               [1, 19, 12], [-5, 17, 14], [-5, 1, -7], [-6, 13, -11], [18, -10, -12], [-7, -8, 12],
               [2, -5, 8], [-14, -15, 16], [13, -6, -7], [15, 14, -1], [14, -2, 3], [18, 15, 5],
               [3, -8, -19], [-3, -11, -6], [10, 12, -17], [2, -12, 1], [-8, -9, -19], [-11, 17, 5],
               [-18, -3, 8], [-17, -8, -12]]

    assert solve_SAT(19, clauses) != "UNSATISFIABLE"

    print("Quinta clausula")
    clauses = [[-15, -4, 14], [-7, -4, 13], [-2, 18, 11], [-12, -11, -6], [7, 17, 4], [4, 6, 13], [-15, -9, -14],
               [14, -4, 8],
               [12, -5, -8], [6, -5, -2], [8, -9, 10], [-15, -11, -12], [12, 16, 17], [17, -9, -12], [-12, -4, 11],
               [-18, 17, -9], [-10, -12, -11], [-7, 15, 2], [2, 15, 17], [-15, -7, 10], [1, -15, 11], [-13, -1, -6],
               [-7, -11, 2], [-5, 1, 15], [-14, -13, 18], [14, 12, -1], [18, -16, 9], [5, -11, -13], [-6, 10, -16],
               [-2, 1, 4], [-4, -11, 8], [-8, 18, 1], [-2, 15, -13], [-15, -12, -10], [-18, -14, -6], [1, -17, 10],
               [10, -13, 2], [2, 17, -3], [14, 1, -17], [-16, -2, -11], [16, 7, 15], [-10, -6, 16], [4, -5, 10],
               [8, 10, -12], [1, -9, -14], [18, -9, 11], [16, 7, 12], [-5, -14, -13], [1, 18, 5], [11, 16, 5],
               [-8, 12, -2], [-6, -2, -13], [18, 16, 7], [-3, 9, -13], [-1, 3, 12], [-10, 7, 3], [-15, -6, -1],
               [-1, -7, -3], [1, 5, 13], [7, 6, -9], [1, -4, 3], [6, 8, 1], [12, 14, -8], [12, 5, -13], [-12, 15, 9],
               [-17, -8, 3], [17, -6, 8], [-3, -14, 4]]

    assert solve_SAT(19, clauses) != "UNSATISFIABLE"

    print("First test passed")
    print("____________________________")


def test2():
    print("Primera CNF de instancias.")
    tupla = list_minisat2list_our_sat('instancias/1-unsat.cnf')
    assert (solve_SAT(tupla[0], tupla[1])) == "UNSATISFIABLE"

    print("Segunda CNF de instancias.")
    tupla = list_minisat2list_our_sat('instancias/2-sat.cnf')
    assert (solve_SAT(tupla[0], tupla[1])) != "UNSATISFIABLE"

    print("Tercera CNF de instancias.")
    tupla = list_minisat2list_our_sat('instancias/3-sat.cnf')
    assert (solve_SAT(tupla[0], tupla[1])) != "UNSATISFIABLE"

    print("Cuarta CNF de instancias.")
    tupla = list_minisat2list_our_sat('instancias/4-sat.cnf')
    assert (solve_SAT(tupla[0], tupla[1])) != "UNSATISFIABLE"

    print("Sexta CNF de instancias.")
    tupla = list_minisat2list_our_sat('instancias/6-unsat.cnf')
    assert (solve_SAT(tupla[0], tupla[1])) == "UNSATISFIABLE"

    print("Séptima CNF de instancias.")
    tupla = list_minisat2list_our_sat('instancias/7-unsat.cnf')
    assert (solve_SAT(tupla[0], tupla[1])) == "UNSATISFIABLE"

    print("Octava CNF de instancias.")
    tupla = list_minisat2list_our_sat('instancias/8-unsat.cnf')
    assert (solve_SAT(tupla[0], tupla[1])) == "UNSATISFIABLE"

    print("Novena CNF de ins")
    tupla = list_minisat2list_our_sat('instancias/9-unsat.cnf')
    assert (solve_SAT(tupla[0], tupla[1])) == "UNSATISFIABLE"

    print("Second test passed")
    print("____________________________")


def test3():
    # 1
    print("\n" + "Primera CNF aleatoria")
    formula1 = generate_formula(100, 50)
    # print(formula1)
    start_time = time()
    llamada_a_pysat = Solver(bootstrap_with=formula1).solve()
    elapsed_time_pysat = time() - start_time
    start_time = time()
    llamada_a_tu_satsolver = solve_SAT(50, formula1)
    elapsed_time_SATsolver = time() - start_time
    if llamada_a_tu_satsolver == "UNSATISFIABLE":
        print("Con tu SATsolver esta CNF es insatisfactible")
    else:
        print("Con tu SATsolver esta CNF es satisfactible")
    if llamada_a_pysat:
        print("Con Pysat esta CNF es satisfactible")
    else:
        print("Con Pysat esta CNF es insatisfactible")

    print("\n" + "El tiempo empleado por tu SATsolver es: ")
    print(elapsed_time_SATsolver)
    print("\n" + "El tiempo empleado por Pysat es: ")
    print(elapsed_time_pysat)
    print("===============================================" + "\n")

    # 2
    print("Segunda CNF aleatoria")
    formula2 = generate_formula(1000, 150)
    # print(formula2)
    start_time = time()
    llamada_a_pysat = Solver(bootstrap_with=formula2).solve()
    elapsed_time_pysat = time() - start_time
    start_time = time()
    llamada_a_tu_satsolver = solve_SAT(150, formula2)
    elapsed_time_SATsolver = time() - start_time
    if llamada_a_tu_satsolver == "UNSATISFIABLE":
        print("Con tu SATsolver esta CNF es insatisfactible")
    else:
        print("Con tu SATsolver esta CNF es satisfactible")
    if llamada_a_pysat:
        print("Con Pysat esta CNF es satisfactible")
    else:
        print("Con Pysat esta CNF es insatisfactible")

    print("\n" + "El tiempo empleado por tu SATsolver es: ")
    print(elapsed_time_SATsolver)
    print("\n" + "El tiempo empleado por Pysat es: ")
    print(elapsed_time_pysat)
    print("===============================================" + "\n")

    # 3
    print("Tercera CNF aleatoria")
    formula3 = generate_formula(10000, 500)
    # print(formula3)
    start_time = time()
    llamada_a_pysat = Solver(bootstrap_with=formula3).solve()
    elapsed_time_pysat = time() - start_time
    start_time = time()
    llamada_a_tu_satsolver = solve_SAT(500, formula3)
    elapsed_time_SATsolver = time() - start_time
    if llamada_a_tu_satsolver == "UNSATISFIABLE":
        print("Con tu SATsolver esta CNF es insatisfactible")
    else:
        print("Con tu SATsolver esta CNF es satisfactible")
    if llamada_a_pysat:
        print("Con Pysat esta CNF es satisfactible")
    else:
        print("Con Pysat esta CNF es insatisfactible")

    print("\n" + "El tiempo empleado por tu SATsolver es: ")
    print(elapsed_time_SATsolver)
    print("\n" + "El tiempo empleado por Pysat es: ")
    print(elapsed_time_pysat)
    print("===============================================" + "\n")


def test4():
    print("____________________________")
    print("\n" + "Mira la diferencia de tiempos con esta CNF")
    start_time = time()
    llamada_a_pysat = Solver(bootstrap_with=[[39, 40, 1], [-39, -40, 1], [39, -40, -1], [-39, 40, -1],
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
                                             [-39, -40, -38], [39, -40, 38], [-39, 40, 38]]).solve()

    elapsed_time_pysat = time() - start_time
    start_time = time()
    llamada_a_tu_satsolver = solve_SAT(60, [[39, 40, 1], [-39, -40, 1], [39, -40, -1], [-39, 40, -1],
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
                                            [-39, -40, -38], [39, -40, 38], [-39, 40, 38]])
    assert (llamada_a_tu_satsolver == "UNSATISFIABLE")
    assert (llamada_a_pysat == False)
    elapsed_time_SATsolver = time() - start_time
    if llamada_a_tu_satsolver == "UNSATISFIABLE":
        print("Con tu SATsolver esta CNF es insatisfactible")
    else:
        print("Con tu SATsolver esta CNF es satisfactible")
    if llamada_a_pysat:
        print("Con Pysat esta CNF es satisfactible")
    else:
        print("Con Pysat esta CNF es insatisfactible")

    print("\n" + "El tiempo empleado por tu SATsolver es: ")
    print(elapsed_time_SATsolver)
    print("\n" + "El tiempo empleado por Pysat es: ")
    print(elapsed_time_pysat)

test1()
#test2()
# test3()
# test4()
