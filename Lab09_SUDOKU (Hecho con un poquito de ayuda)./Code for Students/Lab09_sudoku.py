from pysat.solvers import Mergesat3

letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L',
           'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y']

digits = ['1', '2', '3', '4', '5', '6', '7', '8', '9']

mixed = ['1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E', 'F', 'G']


# Lee un sudoku de un fichero
def read_sudoku(filename):
    with open(filename) as f:
        return [list(line)[:-1] for line in f]


# Escribe la solución de un sudoku en un fichero    
def write_sol(sudoku, f):
    for file in sudoku:
        f.write(str(file) + '\n')


# Transforma los símbolos del sudoku en números
def fromText2digits(sudoku, symbols):
    for i in range(len(sudoku)):
        for j in range(len(sudoku)):
            if sudoku[i][j] != '.':
                sudoku[i][j] = symbols.index(sudoku[i][j]) + 1
    return sudoku


# Asocia un número positivo a cada posible variable
def var2positive(row, column, value, D):
    N = D * D
    return row * N * N + column * N + value


# Descodifica un número positivo en su correspondiente variable 
# identificada por (row, column, value) 
def positive2var(cnf_var, D):
    N = D * D
    row, remainder_row = cnf_var // (N * N), cnf_var % (N * N)
    if remainder_row == 0:
        row, remainder_row = row - 1, N * N
    column, remainder_column = remainder_row // N, remainder_row % N
    if remainder_column == 0:
        column, remainder_column = column - 1, N
    value = cnf_var - (row * N * N + column * N)
    return (row, column, value)


# Construye todas las cláusulas y las devuelve 
def encode(sudoku, D):
    N = D * D
    cnf = []
    # TODO

    # En cada fila están los N elementos
    for row in range(0, N):
        for value in range(1, N + 1):
            cnf.append([var2positive(row, column, value, D) for column in range(0, N)])

    # En cada columna están los N elementos
    for column in range(0, N):
        for value in range(1, N + 1):
            cnf.append([var2positive(row, column, value, D) for row in range(0, N)])

    # Los elementos inciales están
    for i in range(len(sudoku)):
        for j in range(len(sudoku)):
            if sudoku[i][j] != '.':
                cnf.append([var2positive(i, j, sudoku[i][j], D)])

    # En cada submatriz de dimensión d × d están todos los elementos:
    for iprime in range(0, D):
        for jprime in range(0, D):
            for value in range(1, N + 1):
                cnf.append([var2positive(iprime * D + i, jprime * D + j, value, D)
                            for i in range(0, D)
                            for j in range(0, D)])

    # En cada posicion de la matriz hay como mucho un elemento
    for row in range(0, N):
        for column in range(0, N):
            for value in range(1, N + 1):
                for walue in range(value + 1, N + 1):
                    cnf.append([-var2positive(row, column, value, D),
                                -var2positive(row, column, walue, D)])

    return cnf


# Con las cláusulas construidas, que están en cnf, se llama al solver
# Mergesort3 y se construye una solución
def solve_and_decode(sudoku, cnf, D, symbols):
    # crea el solver
    solver = Mergesat3(bootstrap_with=cnf)

    # llama al solver
    solver.solve()

    # obtiene una asignación
    assignment = solver.get_model()

    # construye la solución descodificacndo las variables 
    # solution = deepcopy(sudoku)
    for literal in assignment:
        if 0 < literal:
            (row, column, value) = positive2var(literal, D)
            sudoku[row][column] = symbols[value - 1]
    return sudoku


# Comprueba que una solución (lista de listas de simbolos) es correcta:
# Está completa, contiene los símbolos que corresponden y no repite símbolos 
# en las filas, columnas y matrices. 
def validate_solution(solution, D, symbols):
    # TODO

    for column in range(len(solution[0])):
        for row in range(len(solution[0])):
            if solution[column][row] == '.':
                return False
            if solution[column].count(solution[column][row]) > 1 or solution[row].count(solution[column][row]) > 1:
                return False
    return True


############ Tests for validate_solution #################################

def validate_solution_test():
    assert not validate_solution(
        [['8', '1', '7', '9', '2', '5', '3', '6', '4'],
         ['3', '5', '2', '7', '4', '6', '9', '1', '8'],
         ['4', '6', '.', '1', '8', '3', '2', '5', '7'],
         ['7', '4', '5', '8', '1', '2', '6', '9', '3'],
         ['9', '8', '1', '6', '3', '4', '5', '7', '2'],
         ['2', '3', '6', '5', '9', '7', '4', '8', '1'],
         ['1', '9', '3', '4', '6', '8', '7', '2', '5'],
         ['5', '2', '8', '3', '7', '9', '1', '4', '6'],
         ['6', '7', '4', '2', '5', '1', '8', '3', '9']], 3, digits)

    assert not validate_solution(
        [['8', '1', '7', '9', '2', '5', '3', '6', '4'],
         ['3', '5', '2', '7', '4', '6', '9', '1', '8'],
         ['4', '5', '.', '1', '8', '3', '2', '5', '7'],
         ['7', '4', '5', '8', '1', '2', '6', '9', '3'],
         ['9', '8', '1', '6', '3', '4', '5', '7', '2'],
         ['2', '3', '6', '5', '9', '7', '4', '8', '1'],
         ['1', '9', '3', '4', '6', '8', '7', '2', '5'],
         ['5', '2', '8', '3', '7', '9', '1', '4', '6'],
         ['6', '7', '4', '2', '5', '1', '8', '3', '9']], 3, digits)

    assert not validate_solution(
        [['8', '1', '7', '9', '2', '5', '3', '6', '4'],
         ['3', '5', '2', '7', '4', '6', '9', '1', '8'],
         ['4', '5', '.', '1', '8', '3', '2', '5', '7'],
         ['7', '4', '5', '8', '1', '2', '6', '9', '3'],
         ['9', '8', '1', '6', '3', '4', '5', '7', '2'],
         ['2', '3', '6', '5', '9', '7', '4', '8', '1'],
         ['7', '9', '3', '4', '6', '8', '7', '2', '5'],
         ['5', '2', '8', '3', '7', '9', '1', '4', '6'],
         ['6', '7', '4', '2', '5', '1', '8', '3', '9']], 3, digits)

    assert validate_solution(
        [['8', '1', '7', '9', '2', '5', '3', '6', '4'],
         ['3', '5', '2', '7', '4', '6', '9', '1', '8'],
         ['4', '6', '9', '1', '8', '3', '2', '5', '7'],
         ['7', '4', '5', '8', '1', '2', '6', '9', '3'],
         ['9', '8', '1', '6', '3', '4', '5', '7', '2'],
         ['2', '3', '6', '5', '9', '7', '4', '8', '1'],
         ['1', '9', '3', '4', '6', '8', '7', '2', '5'],
         ['5', '2', '8', '3', '7', '9', '1', '4', '6'],
         ['6', '7', '4', '2', '5', '1', '8', '3', '9']], 3, digits)


####### Test with sudoku 4x4, 9x9, 16x16, 25x25  #######################

def test4x4():
    N = 4
    # Leer un sudoku de fichero
    sudoku = read_sudoku('./inputs/data_4x4.txt')
    # Visualizar el sudoku
    for row in range(0, N):
        print(sudoku[row])

    # Convertir símbolos a números 
    sudoku = fromText2digits(sudoku, digits[:4])

    # Construir las cláusulas
    cnf = encode(sudoku, 2)

    # Resolver el sudoku
    solution = solve_and_decode(sudoku, cnf, 2, digits[:4])

    # Escribir la solución
    print('Solution: ')
    for row in range(0, N):
        print(solution[row])
        # Validar la solución
    if validate_solution(solution, 2, digits[:4]):
        print("La solución es correcta")
    else:
        print("La solución es incorrecta")


def test9x9():
    N = 9
    sudoku = read_sudoku('./inputs/data_9x9.txt')
    for row in range(0, N):
        print(sudoku[row])
    sudoku = fromText2digits(sudoku, digits)
    cnf = encode(sudoku, 3)
    solution = solve_and_decode(sudoku, cnf, 3, digits)
    print('Solution: ')
    for row in range(0, N):
        print(solution[row])
    if validate_solution(solution, 3, digits):
        print("La solución es correcta")
    else:
        print("La solución es incorrecta")


def test16x16():
    N = 16
    sudoku = read_sudoku('./inputs/data_16x16.txt')
    for row in range(0, N):
        print(sudoku[row])
    sudoku = fromText2digits(sudoku, mixed)
    cnf = encode(sudoku, 4)
    solution = solve_and_decode(sudoku, cnf, 4, mixed)
    print('Solution: ')
    for row in range(0, N):
        print(solution[row])
    for row in range(0, N):
        print(solution[row])
    if validate_solution(solution, 4, mixed):
        print("La solución es correcta")
    else:
        print("La solución es incorrecta")


def test25x25():
    N = 25
    sudoku = read_sudoku('./inputs/data_25x25.txt')
    for row in range(0, N):
        print(sudoku[row])
    sudoku = fromText2digits(sudoku, letters)
    cnf = encode(sudoku, 5)
    solution = solve_and_decode(sudoku, cnf, 5, letters)
    print('Solution: ')
    for row in range(0, N):
        print(solution[row])
    if validate_solution(solution, 5, letters):
        print("La solución es correcta")
    else:
        print("La solución es incorrecta")


### Test con 50 sudokus de 9x9 cuyas soluciones se escriben en un fichero ##        

def test_50_sudokus_9x9():
    for i in range(1, 51):
        # Leer un sudoku de 9x9
        sudoku = read_sudoku('./inputs/data_9x9_' + str(i) + '.txt')

        # Convertir símbolos a números  
        sudoku = fromText2digits(sudoku, digits)

        # Construir las cláusulas
        cnf = encode(sudoku, 3)

        # Resolver el sudoku
        solution = solve_and_decode(sudoku, cnf, 3, digits)

        # Validar la solución
        assert validate_solution(solution, 3, digits)

        # Escribir en un fichero la solución 
        f = open('./outputs/data_9x9_' + str(i) + '.txt', 'w')
        for file in solution:
            f.write(str(file) + '\n')
        f.close()

validate_solution_test()
test4x4()
test9x9()
test16x16()
test25x25()
#test_50_sudokus_9x9()
