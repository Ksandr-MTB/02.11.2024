class Car:
    def __init__(self, model, __vin, numbers):
        self.model = model
        self.__vin = __vin
        self.numders = numbers
        self.__is_valid_vin(__vin)
        self.__is_valid_numbers(numbers)

    def __is_valid_vin(self, vin):
        self.vin = vin
        if not isinstance(self.vin, int):
            raise IncorrectVinNumber('Некорректный тип vin номер')
        # return True
        if self.vin < 1000000 or self.vin > 9999999:
            raise IncorrectVinNumber('Неверный диапазон для vin номера')
        return True

    def __is_valid_numbers(self, numbers):
        self.numbers = numbers
        if not isinstance(self.numders, str):
            raise IncorrectCarNumbers('Некорректный тип данных для номеров')
        # return True
        if len(self.numbers) != 6:
            raise IncorrectCarNumbers('Неверная длина номера')
        return True


class IncorrectVinNumber(Exception):
    # pass
    def __init__(self, message):
        # self.message = 'Неверная длина номера'
        self.message = message


class IncorrectCarNumbers(Exception):
    # pass
    def __init__(self, message):
        # self.message = 'Неверная длина номера'
        self.message = message


try:
    first = Car('Model1', 1000000, 'f123dj')
except IncorrectVinNumber as exc:
    print(exc.message)
except IncorrectCarNumbers as exc:
    print(exc.message)
else:
    print(f'{first.model} успешно создан')

try:
    second = Car('Model2', 300, 'т001тр')
except IncorrectVinNumber as exc:
    print(exc.message)
except IncorrectCarNumbers as exc:
    print(exc.message)
else:
    print(f'{second.model} успешно создан')

try:
    third = Car('Model3', 2020202, 'нет номера')
except IncorrectVinNumber as exc:
    print(exc.message)
except IncorrectCarNumbers as exc:
    print(exc.message)
else:
    print(f'{third.model} успешно создан')
