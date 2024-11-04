

def personal_sum(numbers):
    global result, incorrect_data
    result = 0
    incorrect_data = 0

    for i in range(len(numbers)):
        try:
            result +=numbers[i]
        except TypeError:
            incorrect_data +=1
        try:
            print(result / (len(numbers) - incorrect_data))
        except ZeroDivisionError:
            print(0, 0)
        except  TypeError:
            print('В numbers записан некорректный тип данных')