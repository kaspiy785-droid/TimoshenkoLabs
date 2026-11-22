from table import row_sums, column_sums, diagonal_pattern, transform

def main():
    rows = int(input("Количество строк: "))
    columns = int(input("Количество столбцов: "))
    matrix = []
    for _ in range(rows):
        row = [int(part) for part in input("Строка таблицы: ").split()]
        while len(row) != columns:
            print(f"Нужно ровно {columns} чисел")
            row = [int(part) for part in input("Повторите строку: ").split()]
        matrix.append(row)

    print("Суммы строк:", row_sums(matrix))
    print("Суммы столбцов:", column_sums(matrix))

    size = int(input("Введите размер квадратного узора: "))
    pattern = diagonal_pattern(size)
    print("Диагональный узор:")
    for row in pattern:
        print(*row)

    transformed = transform(matrix)
    print("Исходная таблица:")
    for row in matrix:
        print(*row)
    print("Новая таблица:")
    for row in transformed:
        print(*row)

if __name__ == "__main__":
    main()
