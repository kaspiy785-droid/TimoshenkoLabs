line = input("Введите целые числа через пробел: ")

if line.strip() == "":
    print("Нет данных")
else:
    parts = line.split()
    numbers = []
    for part in parts:
        numbers.append(int(part))
    
    count_elements = len(numbers)
    total_sum = sum(numbers)
    min_element = min(numbers)
    max_element = max(numbers)
    avg_value = total_sum / count_elements
    
    print("количество", count_elements)
    print("сумма", total_sum)
    print("минимум", min_element)
    print("максимум", max_element)
    print(f"среднее {avg_value:.2f}")
