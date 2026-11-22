import json
import sys
from pathlib import Path
from logic import add_record, find_records, set_completed, delete_record, statistics
from storage import load_records, save_records

def print_records(records):
    if len(records) == 0:
        print("Нет записей")
        return
    for item in sorted(records, key=lambda x: x["id"]):
        status = "Занятие завершено" if item["completed"] else "Не завершено"
        print(f"ID: {item['id']} | {item['title']} | {item['category']} | {item['amount']} ч. | {status}")

def read_non_empty_str(prompt):
    while True:
        val = input(prompt).strip()
        if val == "":
            print("Ошибка: строка не может быть пустой. Повторите ввод.")
        else:
            return val

def read_non_negative_int(prompt):
    while True:
        raw = input(prompt).strip()
        try:
            num = int(raw)
        except ValueError:
            print("Ошибка: нужно ввести целое число.")
        else:
            if num < 0:
                print("Ошибка: число не может быть меньше нуля.")
            else:
                return num

def read_int(prompt):
    while True:
        raw = input(prompt).strip()
        try:
            return int(raw)
        except ValueError:
            print("Ошибка: нужно ввести целое число.")

def main():
    folder = Path(__file__).resolve().parent
    data_path = folder / "data.json"

    try:
        records, loaded = load_records(data_path)
    except UnicodeError:
        print("Критическая ошибка: неверная кодировка файла data.json (ожидается UTF-8).")
        sys.exit(1)
    except json.JSONDecodeError as err:
        print(f"Критическая ошибка: повреждён формат JSON ({err}).")
        sys.exit(1)
    except ValueError as err:
        print(f"Критическая ошибка структуры данных: {err}.")
        sys.exit(1)
    except OSError as err:
        print(f"Критическая ошибка доступа к файлу: {err}.")
        sys.exit(1)

    if not loaded:
        print("Файл data.json не найден. Начинаем работу с пустого списка.")

    while True:
        print("\n=== ПЛАН УЧЕБНЫХ ЗАНЯТИЙ ===")
        print("1. Показать записи")
        print("2. Добавить запись")
        print("3. Найти записи")
        print("4. Изменить статус")
        print("5. Удалить запись")
        print("6. Показать статистику")
        print("7. Сохранить данные")
        print("8. Выйти")

        choice = input("Выберите команду (1-8): ").strip()

        if choice == "1":
            print_records(records)

        elif choice == "2":
            title = read_non_empty_str("Введите название занятия: ")
            category = read_non_empty_str("Введите категорию: ")
            amount = read_non_negative_int("Введите запланированные часы (целое число >= 0): ")
            new_item = add_record(records, title, category, amount)
            print(f"Запись добавлена с ID {new_item['id']}")

        elif choice == "3":
            query = input("Введите подстроку для поиска по названию: ")
            if query.strip() == "":
                print("Ошибка: поисковый запрос не должен быть пустым.")
            else:
                found = find_records(records, query)
                if len(found) == 0:
                    print("Ничего не найдено")
                else:
                    print_records(found)

        elif choice == "4":
            rec_id = read_int("Введите ID записи для изменения статуса: ")
            status_choice = input("Установить статус (1 - выполнено, 2 - не выполнено): ").strip()
            if status_choice == "1":
                new_status = True
            elif status_choice == "2":
                new_status = False
            else:
                print("Неверный выбор статуса. Операция отменена.")
                continue

            if set_completed(records, rec_id, new_status):
                print("Статус успешно обновлён.")
            else:
                print(f"Запись с ID {rec_id} не найдена.")

        elif choice == "5":
            rec_id = read_int("Введите ID записи для удаления: ")
            exists = any(item["id"] == rec_id for item in records)
            if not exists:
                print(f"Запись с ID {rec_id} не найдена.")
            else:
                confirm = input("Вы уверены, что хотите удалить запись? Введите 'да' для подтверждения: ").strip().lower()
                if confirm == "да":
                    delete_record(records, rec_id)
                    print("Запись удалена.")
                else:
                    print("Удаление отменено.")

        elif choice == "6":
            stats = statistics(records)
            print(f"Всего записей: {stats['total']}")
            print(f"Завершено: {stats['completed']}")
            print(f"Не завершено: {stats['uncompleted']}")
            print(f"Общая сумма часов: {stats['total_amount']}")
            print("Сумма часов по категориям:")
            if len(stats["by_category"]) == 0:
                print("  Нет данных")
            else:
                for cat, total in stats["by_category"].items():
                    print(f"  {cat}: {total} ч.")

        elif choice == "7":
            try:
                save_records(data_path, records)
            except OSError as err:
                print(f"Ошибка при сохранении файла: {err}")
            else:
                print("Данные успешно сохранены в data.json.")

        elif choice == "8":
            while True:
                ans = input("Сохранить текущие данные перед выходом? (да / нет): ").strip().lower()
                if ans == "да":
                    try:
                        save_records(data_path, records)
                    except OSError as err:
                        print(f"Ошибка при сохранении: {err}. Выход отменён.")
                        break
                    else:
                        print("Данные сохранены. До свидания!")
                        return
                elif ans == "нет":
                    print("Выход без сохранения. До свидания!")
                    return
                else:
                    print("Пожалуйста, введите строго 'да' или 'нет'.")

        else:
            print("Неправильная команда. Выберите пункт от 1 до 8.")

if __name__ == "__main__":
    main()
