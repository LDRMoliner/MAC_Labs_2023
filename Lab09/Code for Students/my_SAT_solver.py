from collections import Counter
from random import choice


def remove_trivial_clauses(clauses):
    return [clause for clause in clauses if not any(lit in clause and -lit in clause for lit in clause)]


def eval_3CNF_random(assignment, clauses):
    for i in range(len(clauses)):
        if not eval_clause(clauses[i], assignment):
            return i, False
    return None, True


def eval_3CNF(assignment, clauses):
    return all(eval_clause(clause, assignment) for clause in clauses)


def eval_clause(clause, assignment):
    return any(assignment[abs(lit)] is not None and (
            (lit < 0 and not assignment[abs(lit)]) or (lit > 0 and assignment[abs(lit)])) for lit in clause)


def remove_false(clause, assignment):
    return [lit for lit in clause if assignment[abs(lit)] is None or (lit > 0 and assignment[abs(lit)] == 1) or (
            lit < 0 and assignment[abs(lit)] == 0)]


def remove_false_literals(clauses, assignment):
    return [remove_false(clause, assignment) for clause in clauses]


def remove_true_clauses(clauses, assignment):
    return [clause for clause in clauses if not eval_clause(clause, assignment)]


def set_only_one_variable_type(num_variables, clauses, assignment):
    uni_capa = [lit for sublist in clauses for lit in sublist]
    frecuencias = Counter(uni_capa)

    assignment_values = [
        0 if frecuencias[num] == 0 and frecuencias[-num] > 0 else 1 if frecuencias[num] > 0 and frecuencias[
            -num] == 0 else assignment[num] for num in range(1, num_variables + 1)]
    assignment[1:] = assignment_values


def assign_lonely_variables(clauses, assignment):
    for clause in clauses:
        if len(clause) == 1:
            assignment[abs(clause[0])] = 0 if clause[0] < 0 else 1


def eliminar_iguales(clauses):
    unique_lists = []

    for clause in clauses:
        sorted_clause = sorted(clause)

        if sorted_clause not in unique_lists:
            unique_lists.append(sorted_clause)

    return unique_lists


def sat_preprocessing(num_variables, clauses, assignment):
    # Rule 0
    clauses = remove_trivial_clauses(clauses)
    update = True
    while update:
        # TODO
        # usa funciones auxiliares
        clauses_old = list(clauses)
        assign_lonely_variables(clauses, assignment)
        set_only_one_variable_type(num_variables, clauses, assignment)
        clauses = remove_true_clauses(clauses, assignment)
        clauses = remove_false_literals(clauses, assignment)
        clauses = eliminar_iguales(clauses)
        update = not (clauses_old == clauses)
        if [] in clauses:
            return ([[1], [-1]], assignment)
        else:
            if (clauses == []) or (not update):
                return (clauses, assignment)


def solve_SAT(num_variables, clauses):
    asig = [None] * (num_variables + 1)
    clauses, asig = sat_preprocessing(num_variables, clauses, asig)
    if clauses == [[1], [-1]]:
        return "UNSATISFIABLE"
    return solve_SAT_rec(num_variables, clauses, asig)


def choose_variable(clauses, assignment):
    # Choose the variable with the most occurrences in the remaining clauses
    unassigned_variables = [var for var in range(1, len(assignment)) if assignment[var] is None]
    occurrences = Counter(lit for clause in clauses for lit in clause if abs(lit) in unassigned_variables)
    return max(unassigned_variables, key=lambda var: occurrences.get(var, 0))


def solve_SAT_rec(num_variables, clauses, asig):
    clauses, asig = sat_preprocessing(num_variables, clauses, asig)
    if clauses == [[1], [-1]]:
        return "UNSATISFIABLE"
    elif not clauses:
        return asig
    else:
        var_to_assign = choose_variable(clauses, asig)
        index_to_change = asig.index(None, var_to_assign)
        copy_asig = list(asig)
        asig[index_to_change] = 0
        asig1 = solve_SAT_rec(num_variables, clauses, asig)
        if asig1 != "UNSATISFIABLE":
            return asig1
        asig = list(copy_asig)
        asig[index_to_change] = 1
        return solve_SAT_rec(num_variables, clauses, asig)


def solve_SAT_r(num_variables, clauses):
    assignment = [None] + [choice([0, 1]) for b in range(num_variables)]
    # TODO
    for i in range(1, len(assignment) + 1):
        clause_to_change, satisfied = eval_3CNF_random(assignment, clauses)
        if not satisfied:
            num_to_change = abs(choice(clauses[clause_to_change]))
            assignment[num_to_change] = 1 if assignment[num_to_change] == 0 else 0
            continue
        return assignment
    return "UNSATISFIABLE"

