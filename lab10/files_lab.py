import csv

def read_matrix(path):
    with open(path, "r", encoding="utf-8") as file:
        content = file.read()

    if content.strip() == "":
        raise ValueError("Файл пуст")

    lines = content.splitlines()
    header_parts = lines[0].split()

    if len(header_parts) != 2:
        raise ValueError("Строка 1: ожидалось два числа в заголовке")

    try:
        rows = int(header_parts[0])
        cols = int(header_parts[1])
    except ValueError:
        raise ValueError("Строка 1: размеры таблицы должны быть целыми числами")

    if rows <= 0 or cols <= 0:
        raise ValueError("Строка 1: размеры таблицы должны быть больше нуля")

    if len(lines) - 1 != rows:
        raise ValueError(f"Ожидалось строк данных: {rows}, получено: {len(lines) - 1}")

    matrix = []
    for i in range(1, rows + 1):
        line = lines[i]
        if line.strip() == "":
            raise ValueError(f"Строка {i + 1}: пустая строка недопустима")

        parts = line.split()
        if len(parts) != cols:
            raise ValueError(f"Строка {i + 1}: ожидалось чисел: {cols}")

        row = []
        for part in parts:
            try:
                row.append(int(part))
            except ValueError:
                raise ValueError(f"Строка {i + 1}: нечисловое значение '{part}'")
        matrix.append(row)

    return matrix

def selected_sum(matrix):
    total = 0
    for row in matrix:
        for val in row:
            if val > 0:
                total += val
    return total

def export_csv(matrix, csv_path):
    with open(csv_path, "w", encoding="utf-8", newline="") as file:
        writer = csv.writer(file)
        for row in matrix:
            writer.writerow(row)
