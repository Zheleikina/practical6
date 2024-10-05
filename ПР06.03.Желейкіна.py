def f(x):
    return 1 / (x**2 + 1) + x**2

a = float(input("Введіть початок відрізка a: "))
b = float(input("Введіть кінець відрізка b: "))
h = float(input("Введіть крок h: "))

x = a

values = []

while x <= b:
    y = f(x)
    values.append([x, y])  
    x += h

print(f"{'x':<10} {'f(x)':<10}")
print("-" * 20)
for row in values:
    print(f"{row[0]:<10.2f} {row[1]:<10.4f}")

max_row = max(values, key=lambda item: item[1])

print("\nРядок з найбільшим значенням функції:")
print(f"x = {max_row[0]:.2f}, f(x) = {max_row[1]:.4f}")