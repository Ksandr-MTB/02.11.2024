def is_prime(func):
    def wrapper(*args):  # *args можно заменить на a, b, c
        resul = func(*args)  # *args можно заменить на a, b, c
        q = 0
        if resul == 0 or resul == 1:
            return 'Число должно быть больше 0 и не равняться 1'
        else:
            for i in range(2, resul):
                if resul % i == 0:
                    q += 1
            if q > 0:
                return f'{resul}\nСоставное'

            else:
                return f'{resul}\nПростое'

    return wrapper


@is_prime
def sum_three(*args):   # *args можно заменить на a, b, c
    sum_ = sum(args)
    return sum_


result = sum_three(2, 3, 6)
print(result)
