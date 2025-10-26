n = int(input("Введите количество строк (n): "))
m = int(input("Введите количество столбцов (m): "))
print(f"ПРЯМОУГОЛЬНИК {n}x{m}:")
for i in range(n):
    for j in range(m):
        print("#", end="")
    print()
print("ПРАВЫЙ ТРЕУГОЛЬНИК:")
for i in range(1, n + 1):
    for j in range(i):
        print("#", end="")
    print()
print(f"РАМКА {n}x{m}:")
for i in range(n):
    for j in range(m):
        if i == 0 or i == n - 1 or j == 0 or j == m - 1:
            print("#", end="")
        else:
            print(" ", end="")
    print()