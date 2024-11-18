import threading
import time


class Knight(threading.Thread):
    def __init__(self, name, power):
        threading.Thread.__init__(self)
        self.name = name
        self.power = power

    def run(self):
        print(f'{self.name}, на нас напали!')
        count_q = 100
        days = 0
        while count_q != 0 and count_q > 0:

            count_q -= self.power
            days += 1
            if count_q > 0:
                print(f'{self.name}, сражается {days} день(дня)..., осталось {count_q} воинов.')
            else:
                print(f'{self.name}, сражается {days} день(дня)..., осталось 0 воинов.')
            time.sleep(1)
        print(f'{self.name} одержал победу спустя {days} дней(дня)!')


first_knight = Knight('Sir Lancelot', 10)
second_knight = Knight("Sir Galahad", 20)

first_knight.start()
second_knight.start()

first_knight.join()
second_knight.join()
