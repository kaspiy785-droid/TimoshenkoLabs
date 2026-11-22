def validate_todos(data):
    if not isinstance(data, list):
        raise ValueError("Корень JSON должен быть списком")

    seen_ids = set()
    for i, item in enumerate(data):
        if not isinstance(item, dict):
            raise ValueError(f"Элемент {i} должен быть словарём")

        for key in ("id", "userId", "title", "completed"):
            if key not in item:
                raise ValueError(f"Элемент {i}: отсутствует поле '{key}'")

        item_id = item["id"]
        user_id = item["userId"]
        title = item["title"]
        completed = item["completed"]

        if type(item_id) is not int or item_id <= 0:
            raise ValueError(f"Элемент {i}: id должен быть положительным целым числом")

        if item_id in seen_ids:
            raise ValueError(f"Элемент {i}: повторяющийся id {item_id}")
        seen_ids.add(item_id)

        if type(user_id) is not int or user_id <= 0:
            raise ValueError(f"Элемент {i}: userId должен быть положительным целым числом")

        if type(title) is not str or title.strip() == "":
            raise ValueError(f"Элемент {i}: title должен быть непустой строкой")

        if type(completed) is not bool:
            raise ValueError(f"Элемент {i}: completed должен быть логическим значением")

def completion_counts(todos):
    counts = {}
    for item in todos:
        uid = item["userId"]
        if uid not in counts:
            counts[uid] = 0
        if item["completed"]:
            counts[uid] += 1
    return counts

def top_users(counts):
    if len(counts) == 0:
        return []
    max_val = max(counts.values())
    if max_val == 0:
        return []
    leaders = []
    for uid, count in counts.items():
        if count == max_val:
            leaders.append(uid)
    return sorted(leaders)

def select_tasks(todos, user_id, parameter=None):
    selected = []
    for item in todos:
        if item["userId"] == user_id:
            selected.append(item.copy())
    return selected
