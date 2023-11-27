from sat_generator import generate_formula
from pysat.solvers import Solver
from collections import Counter


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
    uni_capa = [lit for sublist in clauses for lit in sublist]

    for num in range(1, num_variables + 1):
        if uni_capa.count(num) == 0 and uni_capa.count(-num) > 0:
            assignment[abs(num)] = 0
        elif uni_capa.count(num) > 0 and uni_capa.count(-num) == 0:
            assignment[abs(num)] = 1

def assign_lonely_variables(clauses, assignment):
    for clause in clauses:
        if len(clause) == 1:
            assignment[abs(clause[0])] = 0 if clause[0] < 0 else 1


def sat_preprocessing(num_variables, clauses, assignment):
    # Rule 0
    clauses = remove_trivial_clauses(clauses)
    update = True
    while update:
        # TODO
        # usa funciones auxiliares
        clauses_old = clauses
        assign_lonely_variables(clauses, assignment)
        set_only_one_variable(num_variables, clauses, assignment)
        only_one_type_set(num_variables, clauses, assignment)
        clauses = remove_true_clauses(clauses, assignment)
        remove_false_literals(clauses, assignment)
        update = not (clauses_old == clauses)
        if [] in clauses:
            return ([[1], [-1]], assignment)
        else:
            if (clauses == []) or (not update):
                return (clauses, assignment)


def test1():
    def correct_pre_processing(clauses, assig):
        for var in range(1, len(assig)):
            if assig[var] != None:
                for c in clauses:
                    if var in c or -var in c:
                        return False
        return True

    ans = sat_preprocessing(1, [[1]], [None, None])

    assert ans == ([], [None, 1])

    if not correct_pre_processing(ans[0], ans[1]):
        print("Hay variables con un valor asignado que no han sido eliminadas de las clausulas")

    assert ([[1], [-1]]) == sat_preprocessing(1, [[1], [-1]],
                                              [None, None])[0]

    ans = sat_preprocessing(4, [[4], [-3, -1], [3, -4, 2, 1], [1, -3, 4],
                                [-1, -3, -4, 2], [4, 3, 1, 2], [4, 3],
                                [1, 3, -4], [3, -4, 1], [-1]],
                            [None, None, None, None, None])

    assert ans[0] == []
    assert ans[1][1] == 0
    assert ans[1][4] == 1

    if not correct_pre_processing(ans[0], ans[1]):
        print("Hay variables con un valor asignado que no han sido eliminadas de las clausulas")

    ans = sat_preprocessing(5, [[4, -2], [-1, -2], [1], [-4],
                                [5, 1, 4, -2, 3], [-1, 2, 3, 5],
                                [-3, -1], [-4], [4, -1, 2]],
                            [None, None, None, None, None, None])
    assert ans[0] == [[1], [-1]]

    ans = sat_preprocessing(6, [[-5, 3, 2, 6, 1], [5, 6, 2, 4],
                                [3, 5, 2, -1, 4], [1], [2, 1, 4, 3, 6],
                                [-1, -5, 2, 3], [-3, 2, -5, 6, -4]],
                            [None, None, None, None, None, None, None])
    assert ans[0] == [[5, 6, 2, 4], [3, 5, 2, 4], [-5, 2, 3], [-3, 2, -5, 6, -4]]
    assert ans[1][1] == 1

    if not correct_pre_processing(ans[0], ans[1]):
        print("Hay variables con un valor asignado que no han sido eliminadas de las clausulas")

    ans = sat_preprocessing(7, [[-5, 3, 2, 6, 1], [5, 6, 2, 4],
                                [3, 5, 2, -1, 4], [1], [2, 1, 4, 3, 6],
                                [-1, -5, 2, 3], [-3, 2, -5, 6, -4, 7]],
                            [None, None, None, None, None, None, None, None])
    assert ans[0] == []
    assert ans[1][1] == 1
    assert ans[1][4] == 1
    assert ans[1][6] == 1
    assert ans[1][7] == 1

    if not correct_pre_processing(ans[0], ans[1]):
        print("Hay variables con un valor asignado que no han sido eliminadas de las clausulas")

    ans = sat_preprocessing(6, [[-6, -4, 5, -1, ], [1, 2, 3, 6, -5],
                                [4, 6], [-4, -3], [-1],
                                [1, 6, -5, -4], [3, 5, -6, -5, -1]],
                            [None, None, None, None, None, None, None])

    assert ans[0] == []
    assert ans[1][1] == 0
    assert ans[1][2] == 1
    assert ans[1][3] == 0
    assert ans[1][5] == 0

    if not correct_pre_processing(ans[0], ans[1]):
        print("Hay variables con un valor asignado que no han sido eliminadas de las clausulas")


def test2():
    print("CNF aleatoria")
    formula1 = generate_formula(5, 3)
    print(formula1)
    if Solver(bootstrap_with=formula1).solve():
        print("Esta CNF es satisfactible")
    else:
        print("Esta CNF es insatisfactible")
    print("Usando tu pre_processing se obtiene:")
    print(sat_preprocessing(3, formula1, [None] * 4))

    print("\n" + "CNF aleatoria")
    formula2 = generate_formula(10, 7)
    print(formula2)
    if Solver(bootstrap_with=formula2).solve():
        print("Esta CNF es satisfactible")
    else:
        print("Esta CNF es insatisfactible")
    print("Usando tu pre_processing se obtiene:")
    print(sat_preprocessing(7, formula2, [None] * 8))

    print("\n" + "CNF aleatoria")
    formula3 = generate_formula(15, 6)
    print(formula3)
    if Solver(bootstrap_with=formula3).solve():
        print("Esta CNF es satisfactible")
    else:
        print("Esta CNF es insatisfactible")
    print("Usando tu pre_processing se obtiene:")
    print(sat_preprocessing(6, formula3, [None] * 7))

    print("\n" + "CNF aleatoria")
    formula4 = generate_formula(25, 10)
    print(formula4)
    if Solver(bootstrap_with=formula4).solve():
        print("Esta CNF es satisfactible")
    else:
        print("Esta CNF es insatisfactible")
    print("Usando tu pre_processing se obtiene:")
    print(sat_preprocessing(10, formula4, [None] * 11))


test1()
test2()
