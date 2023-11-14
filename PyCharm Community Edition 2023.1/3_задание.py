import random, math

def absolute(negative_lst):
    global n, lst
    negative_lst = []
    for i in range(n):
        negative_lst += [abs(lst[i])]
    return negative_lst


lst = []
num = 100000
num_min = 0
new_lst = []
elements_sum = 0
try:
    n = int(input('Введите количество элементов списка: '))
except:
    print('Нужно ввести целое число')


for i in range(n):
    lst.append(random.randint(-1000, 1000))


for i in range(len(lst)):
    if lst[i] < num:
        num = lst[i]
        num_min = i


for i in range(num_min + 1, len(lst)):
    elements_sum += lst[i]

lst2 = absolute(lst)
nums2 = []

while len(lst) != len(new_lst):
    mn = 100000
    nums1 = 0
    for i in range(len(lst)):
        if i not in nums2:
            if lst2[i] < mn:
                mn = lst2[i]
                nums1 = i
        else:
            continue
    new_lst += [lst[nums1]]
    nums2 += [nums1]


print(lst,'- изначальный список')
print(elements_sum,'- сумма элементов списка после минимального элемента')
print(new_lst,'- элементы списка по возрастанию модулей элементов')