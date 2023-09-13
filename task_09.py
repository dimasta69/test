# Функция connect_dicts объединяет два словаря dict1 и dict2, выбирает словарь с большей суммой значений в качестве
# основного, добавляет в него пары ключ-значение из другого словаря, если значение больше или равно 10, и возвращает
# полученный словарь, отсортированный по значениям.
def connect_dicts(dict1, dict2):
    sum1 = sum(dict1.values()) # вычисляется сумма значений в dict1 и сохраняется в переменной
    sum2 = sum(dict2.values())

    # Проверяется условие: если sum1 больше sum2, то переменной priority_dict присваивается значение dict1, а переменной
    # other_dict - значение dict2. Если sum1 меньше sum2, то переменной priority_dict присваивается значение dict2, а
    # переменной other_dict - значение dict1. Если sum1 равно sum2, то переменной priority_dict присваивается значение
    # dict2, а переменной other_dict - значение dict1.
    if sum1 > sum2:
        priority_dict = dict1
        other_dict = dict2
    elif sum1 < sum2:
        priority_dict = dict2
        other_dict = dict1
    else:
        priority_dict = dict2
        other_dict = dict1

    final_dict = {} # cоздается пустой словарь
    for key, value in priority_dict.items():
        if value >= 10: # если значение больше или равно 10, то пара ключ-значение добавляется в словарь
            final_dict[key] = value

    for key, value in other_dict.items():
        if value >= 10 and key not in final_dict:
            final_dict[key] = value

    return dict(sorted(final_dict.items(), key=lambda x: x[1]))


# Примеры

print(connect_dicts({ "a": 2, "b": 12 }, { "c": 11, "e": 5 })) # => { "c": 11, "b": 12 }
print(connect_dicts({ "a": 13, "b": 9, "d": 11 }, { "c": 12, "a": 15 })) # => { "d": 11, "c": 12, "a": 13 }
print(connect_dicts({ "a": 14, "b": 12 }, { "c": 11, "a": 15 })) # => { "c": 11, "b": 12, "a": 15 }
