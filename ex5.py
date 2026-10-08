import time
import random
import matplotlib.pyplot as plt

sizes = [100000, 300000, 500000, 700000, 1000000]
times_list = []
times_set = []

for N in sizes:
    test_list = list(range(N))
    test_set = set(range(N))

    target = -1

    t_start = time.perf_counter()
    _ = target in test_list
    times_list.append(time.perf_counter() - t_start)

    t_start = time.perf_counter()
    _ = target in test_set
    times_set.append(time.perf_counter() - t_start)

plt.figure(figsize=(8, 5))
plt.plot(sizes, times_list, marker='o', color='r', label='Список (list): O(N)')
plt.plot(sizes, times_set, marker='s', color='g', label='Множество (set): O(1)')
plt.title('Сравнение скорости работы оператора in для списка и множества')
plt.xlabel('Размер структуры данных (N)')
plt.ylabel('Время (секунды)')
plt.grid(True)
plt.legend()
plt.show()