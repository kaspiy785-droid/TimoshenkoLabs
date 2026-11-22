from pathlib import Path
from files_lab import read_matrix, selected_sum, export_csv
from table import row_sums, column_sums

def read_positive_integer():
    while True:
        raw = input("Введите целое число больше нуля: ")
        try:
            num = int(raw)
        except ValueError:
            print("не целое число")
        else:
            if num <= 0:
                print("должно быть больше нуля")
            else:
                return num

def main():
    size = read_positive_integer()
    print("Принят размер:", size)

    folder = Path(__file__).resolve().parent
    matrix_path = folder / "matrix.txt"
    report_path = folder / "report.txt"
    csv_path = folder / "matrix.csv"

    try:
        matrix = read_matrix(matrix_path)
    except FileNotFoundError:
        print("Ошибка: входной файл matrix.txt не найден")
    except UnicodeError:
        print("Ошибка: неверная кодировка файла (ожидается UTF-8)")
    except ValueError as err:
        print("Ошибка формата данных:", err)
    except OSError as err:
        print("Ошибка файлового доступа:", err)
    else:
        r_sums = row_sums(matrix)
        c_sums = column_sums(matrix)
        var_sum = selected_sum(matrix)

        r_str = " ".join(str(x) for x in r_sums)
        c_str = " ".join(str(x) for x in c_sums)

        report_text = (
            f"Суммы строк: {r_str}\n"
            f"Суммы столбцов: {c_str}\n"
            f"Результат варианта: {var_sum}\n"
        )

        try:
            with open(report_path, "w", encoding="utf-8") as report_file:
                report_file.write(report_text)
            export_csv(matrix, csv_path)
        except OSError as err:
            print("Ошибка записи отчёта:", err)
        else:
            print("Отчёт успешно записан в report.txt и matrix.csv")

if __name__ == "__main__":
    main()
