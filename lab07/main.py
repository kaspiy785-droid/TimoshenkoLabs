from functions import sum_digits, average, normalize_text, select_numbers

def main():
    num = int(input("Введите целое число для суммы цифр: "))
    print(sum_digits(num))
    
    nums_line = input("Введите числа через пробел для среднего и фильтрации: ")
    parts = nums_line.split()
    numbers = []
    for part in parts:
        numbers.append(int(part))
        
    avg_res = average(numbers)
    if avg_res is None:
        print("Нет данных")
    else:
        print(f"{avg_res:.2f}")
        
    txt = input("Введите произвольный текст: ")
    print(normalize_text(txt))
    
    threshold = int(input("Введите порог для фильтрации (threshold): "))
    filtered = select_numbers(numbers, threshold)
    print(filtered)

if __name__ == "__main__":
    main()
