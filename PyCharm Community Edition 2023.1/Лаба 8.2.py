import random

def addition_matrix(m1, m2):
    global m, n
    m3 = []
    for i in range(m):
        m3.append([])

    for i in range(m):
        for j in range(n):
            m3[i].append(m1[i][j] + m2[i][j])

    return m3


def subtraction_matrix(m1, m2):
    global m, n
    m3 = []
    for i in range(m):
        m3.append([])

    for i in range(m):
        for j in range(n):
            m3[i].append(m1[i][j] - m2[i][j])

    return m3


try:
    m, n = int(input('Введите кол-во строк: ')), int(input('Введите кол-во столбцов: '))
    if m < 1 or n < 1:
        raise ValueError

    A, B, C, D = [], [], [], []

    for i in range(m):
        A.append([])
        B.append([])
        C.append([])
        D.append([])

    for i in range(m):
        for j in range(n):
            A[i].append(random.randint(-100, 100))
            B[i].append(random.randint(-100, 100))
            C[i].append(random.randint(-100, 100))
            D[i].append(random.randint(-100, 100))

    print('Матрица A')
    for i in range(m):
        print(A[i])

    print('Матрица B')
    for i in range(m):
        print(B[i])

    print('Матрица C')
    for i in range(m):
        print(C[i])

    print('Матрица D')
    for i in range(m):
        print(D[i])

    new_matrix1 = addition_matrix(A, B)
    new_matrix2 = addition_matrix(C, D)
    final_matrix = subtraction_matrix(new_matrix1, new_matrix2)

    print('Сумма матриц A и B')
    for i in range(m):
        print(new_matrix1[i])

    print('Сумма матриц C и D')
    for i in range(m):
        print(new_matrix2[i])

    print('Разность предыдущих матриц')
    for i in range(m):
        print(final_matrix[i])

except:
    print('Введены неверные данные')