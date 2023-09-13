class Dessert:
    def __init__(self, name="", calories=0):
        self._name = name
        self._calories = calories

    def get_name(self):
        return self._name

    def set_name(self, name):
        self._name = name

    def get_calories(self):
        return self._calories

    def set_calories(self, calories):
        self._calories = calories

    def is_healthy(self):
        return self._calories < 200

    def is_delicious(self):
        return True
