n = int(input("Введите количество чисел n: "))

total_sum = 0
positive_count = 0

current_num = int(input("Введите число: "))
total_sum += current_num
if current_num > 0:
    positive_count += 1
max_num = current_num

for i in range(n - 1):
    current_num = int(input("Введите число: "))
    total_sum += current_num
    if current_num > 0:
        positive_count += 1
    if current_num > max_num:
        max_num = current_num

print("Сумма", total_sum, ", положительных", positive_count, ", максимум", max_num)
