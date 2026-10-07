x = float(input("Введите первое число: "))
y = float(input("Введите второе число: "))
op = input("Введите операцию (+, -, *, /): ")

if op == "+":
    print(f"{x + y:.2f}")
elif op == "-":
    print(f"{x - y:.2f}")
elif op == "*":
    print(f"{x * y:.2f}")
elif op == "/":
    if y == 0:
        print("Деление на ноль запрещено")
    else:
        print(f"{x / y:.2f}")
else:
    print("Неизвестная операция")
