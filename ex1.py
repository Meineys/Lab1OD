import time
import random
import matplotlib.pyplot as plt


def foo(s):
    val = 0
    for c in s:
        if c.isdigit():
            val += int(c)
    return val


sizes = [10000, 50000, 100000, 500000, 1000000]
times = []

for n in sizes:
    test_str = "".join(random.choices("abcde12345", k=n))

    start_time = time.perf_counter()
    foo(test_str)
    end_time = time.perf_counter()

    times.append(end_time - start_time)

plt.figure(figsize=(8, 5))
plt.plot(sizes, times, marker='o', color='b', label='O(N)')
plt.title('Зависимость времени выполнения foo(s) от длины строки N')
plt.xlabel('Длина строки (N)')
plt.ylabel('Время выполнения (секунды)')
plt.grid(True)
plt.legend()
plt.show()