def f(x):
    return 1 / (x**2 + 1) + x**2

a = float(input("Введіть початок відрізка a: "))
b = float(input("Введіть кінець відрізка b: "))
h = float(input("Введіть крок h: "))

x = a

print(f"{'x':<10} {'f(x)':<10}")
print("-" * 20)

while x <= b:
    y = f(x)
    print(f"{x:<10.2f} {y:<10.4f}")
    x += h