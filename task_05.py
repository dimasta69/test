from datetime import datetime, timedelta

# Функция принимает целое число.
# В начале функции проволиться првоерка на  то, является ли число целым
# Если нет, то выводим текущую дату.
# При выполнении  всех требований к текущей дате прибавляется
def date_in_future(char = None):
    date_now = datetime.now() # текущая дата
    if char is None:
        return date_now.strftime("%d-%m-%Y %H:%M:%S")

    number_or_not = isinstance(char, int)  # является ли вводимый символ числом
    if number_or_not:
        future_date = date_now + timedelta(days=char)
        return future_date.strftime("%d-%m-%Y %H:%M:%S")

    return date_now.strftime("%d-%m-%Y %H:%M:%S")


#Проверка
print(date_in_future([])) # => текущая дата
print(date_in_future(2)) # => текущая дата + 2 дня