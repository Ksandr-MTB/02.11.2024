import random
import time
import threading

class Bank:

    def __init__(self):
        self.balance = 0
        self.lock = threading.Lock()

    def deposit(self):
        for i in range(100):
            a = random.randint(50, 500)
            if self.balance <= 500 and self.lock.locked():
                self.lock.release()
                self.balance += a
                print(f"Пополнение: {a}. Баланс: {self.balance}")
                # print(f"Пополнение: {a}. Баланс: {self.balance}, итерация {i}  \n {(self.lock.locked())}")
            else:
                self.lock.acquire()
            time.sleep(0.001)

    def take(self):
        for i in range(100):
            b = random.randint(50, 500)
            print(f"Запрос на {b}")
            if b <= self.balance:
                self.balance -= b
                print(f"Снятие: {b}. Баланс: {self.balance} ")
                # print(f"Снятие: {b}. Баланс: {self.balance} итерация {i}  \n {(self.lock.locked())}")
                # time.sleep(0.001)

            else:
                print(f'Запрос отклонён, недостаточно средств')
                # time.sleep(0.001)
                # print(f'Запрос отклонён, недостаточно средств, итерация {i}  \n {(self.lock.locked())}')
                self.lock.acquire()
    # time.sleep(0.001)


bk = Bank()
th1 = threading.Thread(target=Bank.deposit, args=(bk,))
th2 = threading.Thread(target=Bank.take, args=(bk,))
th1.start()
th2.start()
th1.join()
th2.join()
print(f'Итоговый баланс: {bk.balance}')