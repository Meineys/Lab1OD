import time
import random
import matplotlib.pyplot as plt

sizes = [100000, 300000, 500000, 700000, 1000000]
times_list = []
times_dict = []

for N in sizes:
    test_list = list(range(N))
    test_dict = {i: i for i in range(N)}

    target_index = N // 2

    t_start = time.perf_counter()
    del test_list[target_index]
    times_list.append(time.perf_counter() - t_start)

    t_start = time.perf_counter()
    del test_dict[target_index]
    times_dict.append(time.perf_counter() - t_start)

plt.figure(figsize=(8, 5))
plt.plot(sizes, times_list, marker='o', color='r', label='Список (list): O(N)')
plt.plot(sizes, times_dict, marker='s', color='g', label='Словарь (dict): O(1)')
plt.title('Сравнение скорости работы оператора del для списка и словаря')
plt.xlabel('Размер структуры данных (N)')
plt.ylabel('Время (секунды)')
plt.grid(True)
plt.legend()
plt.show()