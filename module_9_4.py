from fileinput import close

first = 'Мама мыла раму'
second = 'Рамена мало было'

result = map(lambda x, y: x == y, first, second)
print(list(result))


def get_advanced_writer(file_name):
    def write_everything(*data_set):
        file = open(file_name, 'w', encoding='utf-8')
        for i in (data_set):
            file.write(f'{i}\n')
        file.close()

    return write_everything


write_1 = get_advanced_writer('example.txt')
write_1('Это строчка', ['А', 'это', 'уже', 'число', 5, 'в', 'списке'])

# with open('example.txt', 'r', encoding='utf-8') as file:
#     print(list(file))

import random
class MysticBall:
    def __init__(self, *words):
        self.words = words

    def __call__(self):
        return random.choice(self.words)


first_ball = MysticBall('Да', 'Нет', 'Наверное')
print(first_ball())
print(first_ball())
print(first_ball())