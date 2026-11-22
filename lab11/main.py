import json
from pathlib import Path
from analysis import validate_todos, completion_counts, top_users, select_tasks

def read_positive_user_id():
    while True:
        raw = input("Введите положительный целый user_id: ")
        try:
            uid = int(raw)
        except ValueError:
            print("Ошибка: нужно ввести целое число")
        else:
            if uid <= 0:
                print("Ошибка: user_id должен быть больше нуля")
            else:
                return uid

def main():
    folder = Path(__file__).resolve().parent
    todos_path = folder / "todos.json"
    leaders_path = folder / "leaders.json"
    selected_path = folder / "selected.json"

    try:
        with open(todos_path, "r", encoding="utf-8") as file:
            todos = json.load(file)
        validate_todos(todos)
    except FileNotFoundError:
        print("Ошибка: файл todos.json не найден")
    except UnicodeError:
        print("Ошибка: неверная кодировка файла (ожидается UTF-8)")
    except json.JSONDecodeError as error:
        print(f"Ошибка синтаксиса JSON: {error}")
    except ValueError as error:
        print(f"Ошибка структуры данных: {error}")
    except OSError as error:
        print(f"Ошибка файлового доступа: {error}")
    else:
        counts = completion_counts(todos)
        leaders = top_users(counts)

        leader_tasks = []
        for item in todos:
            if item["userId"] in leaders and item["completed"]:
                leader_tasks.append(item.copy())

        print("Выполненные задачи по пользователям:", counts)
        print("Лидеры:", leaders)

        user_id = read_positive_user_id()
        selected = select_tasks(todos, user_id)

        try:
            with open(leaders_path, "w", encoding="utf-8") as file:
                json.dump(leader_tasks, file, ensure_ascii=False, indent=2)
            with open(selected_path, "w", encoding="utf-8") as file:
                json.dump(selected, file, ensure_ascii=False, indent=2)
        except OSError as error:
            print(f"Ошибка сохранения результатов: {error}")
        else:
            print("Файлы leaders.json и selected.json успешно сохранены")

if __name__ == "__main__":
    main()
