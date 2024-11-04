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
        print((result, incorrect_data))
    except TypeError:
        print(0)


def calculate_average(numbers):
    personal_sum(numbers)
    try:
        print(result / (len(numbers) - incorrect_data))
    except ZeroDivisionError:
        print(0)
    except  TypeError:
        print('В numbers записан некорректный тип данных')


calculate_average("1, 2, 3")
calculate_average([1, "Строка", 3, "Ещё Строка"])
calculate_average(567)
calculate_average([42, 15, 36, 13])
calculate_average([])
