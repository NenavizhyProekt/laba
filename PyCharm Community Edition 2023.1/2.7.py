try:
    m, n = int(input('Введите количество строк списка: ')), int(input('Введите количество столбцов списка: '))
    lst = []
    if m <= 0 or n <= 0:
        raise ValueError

    for i in range(m):
        string = []
        for j in range(1, n+1):
            string.append(j*5)
        lst.append(string)


    for i in range(len(lst)):
        print(lst[i])

except:
    print('Введено неверное значение')