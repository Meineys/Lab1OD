import time
import random
import matplotlib.pyplot as plt

#1варик
def alg1_find_three_max(nums):
    nums_copy = list(nums)
    three_max = []
    for _ in range(3):
        m = max(nums_copy)
        three_max.append(m)
        nums_copy.remove(m)
    return three_max

#2варик
def alg2_find_three_max(nums):
    return sorted(nums)[-3:]


sizes = [100, 1000, 5000, 10000, 20000, 50000]
times_alg1 = []
times_alg2 = []

for N in sizes:
    data = [random.randint(1, 1000000) for _ in range(N)]

    t1_start = time.perf_counter()
    alg1_find_three_max(data)
    t1_end = time.perf_counter()
    times_alg1.append(t1_end - t1_start)

    t2_start = time.perf_counter()
    alg2_find_three_max(data)
    t2_end = time.perf_counter()
    times_alg2.append(t2_end - t2_start)

plt.figure(figsize=(8, 5))
plt.plot(sizes, times_alg1, marker='o', label='Алгоритм 1: O(N)')
plt.plot(sizes, times_alg2, marker='s', label='Алгоритм 2: O(N log N)')
plt.title('Сравнение алгоритмов поиска 3 максимальных элементов')
plt.xlabel('Количество элементов (N)')
plt.ylabel('Время (секунды)')
plt.grid(True)
plt.legend()
plt.show()