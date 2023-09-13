# Функция принимает список слов.
# Далее необходим пустой словарь, где ключами являются отсортированные буквы
# Для каждого слова сортируем ешо букву и приводим к нижнему регистру.
# Если отсортированныое слово уже есть, то добовляем слово в соотвестующий список.
# Возвращаем список значений.
def combine_anagrams(words_array):
    anagram_groups = {} # создаем пустой список

    for word in words_array:
        sorted_word = ''.join(sorted(word.lower())) # сортированное слово в нижнем регистре

        if sorted_word in anagram_groups:
            anagram_groups[sorted_word].append(word)
        else:
            anagram_groups[sorted_word] = [word]

    return print(list(anagram_groups.values()))

# Проверка
combine_anagrams(["cars", "for", "potatoes", "racs", "four", "scar", "creams", "scream"])
# => [ ["cars", "racs", "scar"], ["four"], ["for"], ["potatoes"], ["creams", "scream"] ]