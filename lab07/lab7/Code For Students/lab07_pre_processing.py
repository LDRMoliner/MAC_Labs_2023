from sat_generator import generate_formula
from pysat.solvers import Solver

def remove_trivial_clauses(clauses):
    if not clauses:
        return []
    else:
        first_clause = clauses[0]
        if any(lit in first_clause and -lit in first_clause for lit in first_clause):
            return remove_trivial_clauses(clauses[1:])
        else:
            return [first_clause] + remove_trivial_clauses(clauses[1:])


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
    clauses = remove_trivial_clauses(clauses)
    print(clauses)
    print(assignment)
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


def test1():
    def correct_pre_processing(clauses, assig):
        for var in range(1, len(assig)):
            if assig[var] != None:
                for c in clauses:
                    if var in c or -var in c:
                        return False
        return True

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




test1()
test2()
