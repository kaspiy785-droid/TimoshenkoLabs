price = int(input("Цена одной тетради: "))
count = int(input("Количество тетрадий: "))
paid = int(input("Переданная сумма: "))

# Считаем стоимость и сдачу
cost = price * count
change = paid - cost

print("стоимость", cost, ", сдача", change)
