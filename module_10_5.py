import time
from multiprocessing import Pool


def read_info(name):
        all_data = []

        file = open(name)
        for line in file:
            if len(line) > 0:
                all_data.append(line)
            else:
                break
        file.close()
        print('функция выполнена') #Для проверки как происходит обработка файлов (последовательно или паралельно
        return all_data


# file_names = ['file 1.txt', 'file 2.txt', 'file 3.txt', 'file 4.txt']
# start_time = time.time()
# for i in file_names:
#     start_ = read_info(i)
# parallel_time = time.time() - start_time
# print(f"Время выполнения линейного чтения: {parallel_time:.4f} секунд")


if __name__ == '__main__':
    file_names = ['file 1.txt', 'file 2.txt', 'file 3.txt', 'file 4.txt']
    start_time = time.time()
    with Pool() as pool:
        all_data_parallel = pool.map(read_info, file_names)
    parallel_time = time.time() - start_time
    print(f"Время выполнения многопроцессного чтения: {parallel_time:.4f} секунд")