# Данный метод принимает список значений в либом формате.
# Так как в примере указанно, что он должен перемножать как и значение flaot ,
# так и строки, то первым действием будет перевод тип данных в строку.
# Далее, игнорируя все второстепенные знаки (препинаия, пробелы и т.д) произволиться перемножение.
def  multiply_numbers(inputs = None):
    if inputs is None:
        return "None"
    string = str(inputs) # входящие данные переводим в тип данных строка

    numbers = []
    for char in string:
        if char.isnumeric(): # поэлементная проверка, являестя ли символ числом
            numbers.append(int(char)) # если является, то добавляем в массив

    numbers_clear = numbers == []

    if numbers_clear:
        return "None"

    multiplay = 1 # необходимая нам переменная, для сохранения полученных вычислений
    for number in numbers:
        multiplay *= number

    return multiplay

# Проверка
multiply_numbers() # => None
multiply_numbers('ss') # => None
multiply_numbers('1234') # => 24
multiply_numbers('sssdd34') # => 12
multiply_numbers(2.3) # => 6
multiply_numbers([5, 6, 4]) # => 120