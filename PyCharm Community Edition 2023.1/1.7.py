import random

def sort_list(num):
    global m, n, lst

    lst_1 = []
    for i in range(m):
        lst_1.append(lst[i][num])

    new_list = []
    while lst_1:
        minimum = lst_1[0]
        for x in lst_1:
            if x < minimum:
                minimum = x
        new_list.append(minimum)
        lst_1.remove(minimum)

    for i in range(m):
        lst[i][num] = new_list[i]



try:
    m, n = int(input('Введите количество строк списка: ')), int(input('Введите количество столбцов списка: '))
    lst = []
    if m <= 0 or n <= 0:
        raise ValueError

    for i in range(m):
        string = []
        for j in range(n):
            string.append(random.randint(100, 999))
        lst.append(string)

    print('Изначальный список:')

    for i in range(len(lst)):
        print(lst[i])

    print('Отсортированный список:')

    for i in range(n):
        if i % 2 == 0:
            sort_list(i)

    for i in range(len(lst)):
        print(lst[i])

except:
    print('Введено неверное значение')

