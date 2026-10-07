rejected_attempts = 0

while True:
    num = int(input("Введите целое число: "))
    if num > 0:
        break
    rejected_attempts += 1

print("Квадрат", num * num, ", отклонено", rejected_attempts)
