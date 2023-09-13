import re
# Функция принимает строку, в которой для начала происходит процесс удаление всей пунктуации, далее перевод в нижний
# регистр и разбиение на слова.
# Так же требуется цикл для подсчета количесвта повторений слов в строке.
def count_words(string):
    string_pun = re.sub(r'[.,"\'-?:!;]', '', string) # удаление знаков препинания
    word_list = string_pun.lower().split() # перевод в нижний регистр и разбиение на отдельные слова
    word_dict = {}
    for word in word_list:
        if word.isalpha() :
            if word in word_dict:
                word_dict[word] += 1
            else:
                word_dict[word] = 1
    return word_dict

# Проверка

print(count_words("A man, a plan, a canal -- Panama"))
#  {"a": 3, "man": 1, "canal": 1, "panama": 1, "plan": 1}

print(count_words("Doo bee doo bee doo"))
#  {"doo": 3, "bee": 2}