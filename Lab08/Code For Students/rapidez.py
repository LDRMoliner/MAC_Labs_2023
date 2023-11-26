from time import time
from sat_generator import generate_formula
from tools import list_minisat2list_our_sat
from collections import defaultdict

def eval_clause(clause, assignment):
    return any(assignment[abs(lit)] is not None and (
            (lit < 0 and not assignment[abs(lit)]) or (lit > 0 and assignment[abs(lit)])) for lit in clause)


def remove_trivial_clauses(clauses):
    return [clause for clause in clauses if not any(lit in clause and -lit in clause for lit in clause)]


def remove_false(clause, assignment):
    return [lit for lit in clause if assignment[abs(lit)] is None or (lit > 0 and assignment[abs(lit)] == 1) or (
                lit < 0 and assignment[abs(lit)] == 0)]


def remove_false_literals(clauses, assignment):
    for i in range(len(clauses)):
        clauses[i] = remove_false(clauses[i], assignment)


def search(clauses, assignment):
    uni_capa = [lit for sublist in clauses for lit in sublist]
    freq = defaultdict(int)

    # Count the frequency of each literal
    for i in uni_capa:
        freq[i] += 1

    # Identify unique literals with frequency 1
    unicos = {literal for literal, freq in freq.items() if freq == 1}

    unicos_absolutos = set()
    for unico in unicos:
        if -unico not in unicos:
            unicos_absolutos.add(unico)
    # Update assignment based on unique literals
    for unico in unicos_absolutos:
        if unico < 0:
            assignment[abs(unico)] = 0
        else:
            assignment[abs(unico)] = 1

def remove_true_clauses(clauses, assignment):
    clauses_new = []
    for clause in clauses:
        if not eval_clause(clause, assignment):
            clauses_new.append(clause)
    return clauses_new


def set_only_one_variable(num_variables, clauses, assignment):
    literal_appearances = [set() for _ in range(num_variables + 1)]

    for clause in clauses:
        for literal in clause:
            variable = abs(literal)
            literal_appearances[variable].add(variable if literal > 0 else -variable)

    for variable, appearances in enumerate(literal_appearances[1:], start=1):
        if len(appearances) == 1:
            assignment[variable] = 1 if appearances.pop() > 0 else 0


def assign_lonely_variables(clauses, assignment):
    for clause in clauses:
        if len(clause) == 1:
            assignment[abs(clause[0])] = 0 if clause[0] < 0 else 1


def sat_preprocessing(num_variables, clauses, assignment):
    # Rule 0
    update = True
    while update:
        # TODO
        # usa funciones auxiliares
        clauses_old = clauses
        assign_lonely_variables(clauses, assignment)
        set_only_one_variable(num_variables, clauses, assignment)
        clauses = remove_true_clauses(list(clauses), assignment)
        remove_false_literals(clauses, assignment)
        update = not (clauses_old == clauses)
        if [] in clauses:
            return [[1], [-1]], assignment
        else:
            if (clauses == []) or (not update):
                return clauses, assignment


def test1():
    """"
    print("Séptima CNF de instancias.")
    tupla = list_minisat2list_our_sat('instancias/7-unsat.cnf')
    asig = [None] * (tupla[0] + 1)
    start_time = time()
    sat_preprocessing(tupla[0], tupla[1], asig)
    elapsed_time = time() - start_time
    print("He tardado:")
    print(elapsed_time)
    start_time = time()
    asig = [None] * (60 + 1)
    
    sat_preprocessing(60, [[39, 40, 1], [-39, -40, 1], [39, -40, -1], [-39, 40, -1],
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
                           [-39, -40, -38], [39, -40, 38], [-39, 40, 38]], asig)
    """""
    asig = [None] * (104 + 1)
    search([[-70, 69, 103], [-39, -40, -69, 1], [39, -40, -1], [-39, 40, -1],
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
            [-39, -40, -38], [39, -40, 38], [-39, 40, 38]], asig)
    print(asig)
    print("He tardado:")


test1()
