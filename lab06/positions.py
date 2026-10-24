line = input("Введите целые числа через пробел: ")

if line.strip() == "":
    print("Нет данных")
else:
    parts = line.split()
    numbers = []
    for part in parts:
        numbers.append(int(part))
    
    max_val = max(numbers)
    indexes = []
    for idx, val in enumerate(numbers):
        if val == max_val:
            indexes.append(idx)
            
    print(indexes)
