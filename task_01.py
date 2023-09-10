# Функция предназначенная для определения, является ли строка палиндромом или нет.
# В строке учитываются только некоторые символы (буквы, цифры).
def is_palindrome(data):
    line = ""  # cоздаем пустую строку для сохранения символов

    string = str(data) #перобразуем  наши данные в формат str
    for char in string:  # в этом цикле мы проходимся по каждому символу этой строки
        if char.isalnum():  # проверяем, является ли наш символ цифрой или буквой
            line += char  # при true добавялем символ к строке

    line = line.lower()  # переводим все символы в нижний регистр

    for i in range(len(line)):
        if line[i] != line[-1 - i]:
            return print(False)
    return print(True)

#примеры
is_palindrome("A man, a plan, a canal -- Panama") # => True
is_palindrome("Madam, I'm Adam!") # => True
is_palindrome(333) # => True
is_palindrome(None) # => False
is_palindrome("Abracadabra") # => False