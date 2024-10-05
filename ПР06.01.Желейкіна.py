a = float(input("Введіть початкову точку a: "))
b = float(input("Введіть кінцеву точку b: "))
h = float(input("Введіть крок h: "))

def f(x):
    return 1 / (x**2 + 1) + x**2

print(f"{'x':<10} {'f(x)':<10}")
print("-" * 20)

for i in range(int((b - a) / h) + 1):
    x = a + i * h
    print(f"{x:<10.2f} {f(x):<10.4f}")