import json
import socket
from pathlib import Path
from urllib.error import HTTPError, URLError
from urllib.parse import quote
from urllib.request import Request, urlopen

def fetch_profile(login):
    if not login.strip():
        raise ValueError("Логин не должен быть пустым")
    url = "https://api.github.com/users/" + quote(login.strip(), safe="")
    request = Request(url, headers={
        "Accept": "application/vnd.github+json",
        "User-Agent": "python-course-lab11",
    })
    with urlopen(request, timeout=10) as response:
        data = json.loads(response.read().decode("utf-8"))
    if not isinstance(data, dict) or not isinstance(data.get("login"), str):
        raise ValueError("Ответ не похож на профиль пользователя")
    return data

def print_profile_info(data):
    login = data.get("login")
    user_id = data.get("id")
    name = data.get("name")
    print("Логин:", login)
    print("ID:", user_id)
    if name is None:
        print("Имя: не указано")
    else:
        print("Имя:", name)

def main():
    folder = Path(__file__).resolve().parent
    choice = input("Источник профиля (1 - сеть GitHub, 2 - локальный пример): ").strip()

    if choice == "2":
        sample_path = folder / "profile_sample.json"
        try:
            with open(sample_path, "r", encoding="utf-8") as file:
                data = json.load(file)
            print_profile_info(data)
        except (OSError, ValueError, UnicodeError) as error:
            print(f"Ошибка чтения локального примера: {error}")
    else:
        try:
            data = fetch_profile(input("Логин GitHub: "))
            output = folder / "profile.json"
            with open(output, "w", encoding="utf-8") as file:
                json.dump(data, file, ensure_ascii=False, indent=2)
            print_profile_info(data)
            print(f"Профиль сохранён: {data['login']}")
        except HTTPError as error:
            print(f"Сервер вернул HTTP {error.code}")
        except (URLError, TimeoutError, socket.timeout):
            print("Не удалось получить ответ по сети")
        except (ValueError, UnicodeError) as error:
            print(f"Ошибка данных: {error}")
        except OSError as error:
            print(f"Ошибка доступа: {error}")

if __name__ == "__main__":
    main()
