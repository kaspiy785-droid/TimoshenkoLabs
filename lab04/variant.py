n = int(input("Введите количество чисел n: "))

count_matches = 0
sum_matches = 0

for i in range(n):
    num = int(input("Введите число: "))
    if num % 2 == 0:
        count_matches += 1
        sum_matches += num

print("Количество", count_matches, ", сумма", sum_matches)

print("\n--- Дополнительное задание ---")
check_num = int(input("Введите число для проверки на простоту: "))

if check_num < 2:
    is_prime = False
else:
    is_prime = True
    divisor = 2
    while divisor * divisor <= check_num:
        if check_num % divisor == 0:
            is_prime = False
            break
        divisor += 1

if is_prime:
    print("да")
else:
    print("нет")
