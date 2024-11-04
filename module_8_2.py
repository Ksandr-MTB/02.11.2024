

def personal_sum(numbers):
    global result, incorrect_data
    result = 0
    incorrect_data = 0
    try:
        for i in range(len(numbers)):
            try:
                result += numbers[i]
            except TypeError:
                incorrect_data += 1
                print(f'Некорректный тип данных для подсчёта суммы - {numbers[i]}')
        return result, incorrect_data
    except TypeError:
        return 0


def calculate_average(numbers):
    personal_sum(numbers)
    try:
        return result / (len(numbers) - incorrect_data)
    except ZeroDivisionError:
        return 0
    except  TypeError:
        return 'В numbers записан некорректный тип данных'




print(f'Результат 1: {calculate_average("1, 2, 3")}')
print(f'Результат 2: {calculate_average([1, "Строка", 3, "Ещё Строка"])}')
print(f'Результат 3: {calculate_average(567)}')
print(f'Результат 4: {calculate_average([42, 15, 36, 13])}')
print(f'Результат 5: {calculate_average([])}')