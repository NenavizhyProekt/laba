string = input('Введите строку: ')
numbers = '0123456789'
count_numbers = 0

for i in range(len(string)):
    if string[i] in numbers:
        count_numbers += 1


print(string, count_numbers, '- число цифр в строке')