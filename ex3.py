import math

a = 1
b = -5
c = -50

discriminant = b**2 - 4 * a * c

if discriminant > 0:
    x1 = (-b + math.sqrt(discriminant)) / (2 * a)
    x2 = (-b - math.sqrt(discriminant)) / (2 * a)
    n_res = max(x1, x2)
    print(f"Размер массива N = {int(n_res)}")