# Метод определяет наибольший элемент массива
# и наименьший элемент массива, после этого меняет их местами.
# Если максимальные элементы повторяются, то мы заменяем их все.
# После этого добавляем минимальное в конец.
# По умолчанию оставляем переменную равную пустому списку.
def sort_list(list = []):
    list_copy = list

    if list == []:
        return []

    max_number = max(list_copy) # находим максимальное значение
    min_number = min(list_copy) # находим минимальное значение

    for i in range(len(list_copy)):
        if list_copy[i] == max_number:
            list_copy[i] = min_number
        elif list_copy[i] == min_number:
            list_copy[i] = max_number

    list_copy.append(min_number) # добавляем в конец списка минимальное значение
    return list_copy

# Примеры
sort_list([]) # => []
sort_list([2, 4, 6, 8]) # => [8, 4, 6, 2, 2]
sort_list([1]) # => [1, 1]
sort_list([1, 2, 1, 3]) # => [3, 2, 3, 1, 1]
