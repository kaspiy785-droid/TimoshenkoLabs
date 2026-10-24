line = input("Введите целые числа через пробел: ")

parts = line.split()
numbers = []
for part in parts:
    numbers.append(int(part))

filtered = []
for x in numbers:
    if x % 2 == 0:
        filtered.append(x)

count_res = len(filtered)
sum_res = sum(filtered)
sorted_res = sorted(filtered)

print("исходном", numbers)
print("количество", count_res)
print("сумма", sum_res)
print("отсортированная копия", sorted_res)

print("\n--- Дополнительное задание (Удаление повторов) ---")
unique_list = []
for item in numbers:
    if item not in unique_list:
        unique_list.append(item)

print(unique_list)
