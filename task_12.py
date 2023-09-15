class Dessert:
    def __init__(self, name="", calories=0):
        self._name = name
        self._calories = calories

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        self._name = name

    @property
    def calories(self):
        return self._calories

    @calories.setter
    def calories(self, calories):
        if isinstance(calories, (int, float)):
            self._calories = calories
        elif isinstance(self, str):
            if calories.isdigit():
                self._calories = calories
            else:
                raise ValueError("Строка содержит символы, помимо чисел")
        else:
             raise ValueError("Неверный формат вводимых данных")

    def is_healthy(self):
        if self._calories > 200:
            return False
        else:
            return True

    def is_delicious(self):
        return True


class JellyBean(Dessert):
    def __init__(self, name="", calories=0, flavor=""):
        super().__init__(name, calories)
        self._flavor = flavor

    def get_flavor(self):
        return self._flavor

    def set_flavor(self, flavor):
        self._flavor = flavor

    def is_delicious(self):
        if self._flavor == "black licorice":
            return False
        else:
            return True