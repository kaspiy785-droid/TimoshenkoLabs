line = input("Введите целые числа через пробел: ")

parts = line.split()
original = []
for part in parts:
    original.append(int(part))

transformed = []
for x in original:
    if x < 0:
        transformed.append(-x)
    else:
        transformed.append(x)

print("исходный", original)
print("новый", transformed)
