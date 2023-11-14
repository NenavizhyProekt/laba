string = input('Введите строку: ')
small_letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
                 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',]
big_letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M',
               'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z',]

def replace_letter(letter):
    global small_letters, big_letters
    number = ''
    if letter in small_letters:
        for i in range(len(small_letters)):
            if letter == small_letters[i]:
                number = i
        return big_letters[number]
    return letter

new_string = ''
for i in range(len(string)):
    new_string += replace_letter(string[i])

print(string, new_string, 'Прописные буквы преобразованы в строчные')