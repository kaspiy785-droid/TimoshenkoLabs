x = float(input("Введите координату x: "))
y = float(input("Введите координату y: "))

if 0 <= x <= 5 and 0 <= y <= 3:
    if x == 0 or x == 5 or y == 0 or y == 3:
        print("на границе")
    else:
        print("внутри")
else:
    print("снаружи")
