def validate_records(records):
    if not isinstance(records, list):
        raise ValueError("Корень JSON должен быть списком")

    seen_ids = set()
    for i, item in enumerate(records):
        if not isinstance(item, dict):
            raise ValueError(f"Запись {i} должна быть словарём")

        for key in ("id", "title", "category", "amount", "completed"):
            if key not in item:
                raise ValueError(f"Запись {i}: отсутствует поле '{key}'")

        rec_id = item["id"]
        title = item["title"]
        category = item["category"]
        amount = item["amount"]
        completed = item["completed"]

        if type(rec_id) is not int or rec_id <= 0:
            raise ValueError(f"Запись {i}: id должен быть положительным целым числом")
        if rec_id in seen_ids:
            raise ValueError(f"Запись {i}: повторяющийся id {rec_id}")
        seen_ids.add(rec_id)

        if type(title) is not str or title.strip() == "":
            raise ValueError(f"Запись {i}: title должен быть непустой строкой")
        if type(category) is not str or category.strip() == "":
            raise ValueError(f"Запись {i}: category должен быть непустой строкой")
        if type(amount) is not int or amount < 0:
            raise ValueError(f"Запись {i}: amount должен быть целым числом >= 0")
        if type(completed) is not bool:
            raise ValueError(f"Запись {i}: completed должен быть логическим значением")

def add_record(records, title, category, amount):
    clean_title = title.strip()
    clean_category = category.strip()

    if clean_title == "":
        raise ValueError("Название не должно быть пустым")
    if clean_category == "":
        raise ValueError("Категория не должна быть пустой")
    if type(amount) is not int or amount < 0:
        raise ValueError("Количество часов должно быть целым числом >= 0")

    if len(records) == 0:
        new_id = 1
    else:
        new_id = max(item["id"] for item in records) + 1

    new_item = {
        "id": new_id,
        "title": clean_title,
        "category": clean_category,
        "amount": amount,
        "completed": False
    }
    records.append(new_item)
    return new_item

def find_records(records, query):
    clean_query = query.strip().lower()
    if clean_query == "":
        return []
    found = []
    for item in records:
        if clean_query in item["title"].lower():
            found.append(item.copy())
    return found

def set_completed(records, record_id, completed):
    for item in records:
        if item["id"] == record_id:
            item["completed"] = completed
            return True
    return False

def delete_record(records, record_id):
    for i, item in enumerate(records):
        if item["id"] == record_id:
            records.pop(i)
            return True
    return False

def statistics(records):
    total_count = len(records)
    completed_count = 0
    uncompleted_count = 0
    total_amount = 0
    by_category = {}

    for item in records:
        if item["completed"]:
            completed_count += 1
        else:
            uncompleted_count += 1
        total_amount += item["amount"]
        cat = item["category"].strip()
        by_category[cat] = by_category.get(cat, 0) + item["amount"]

    sorted_categories = {}
    for cat in sorted(by_category):
        sorted_categories[cat] = by_category[cat]

    return {
        "total": total_count,
        "completed": completed_count,
        "uncompleted": uncompleted_count,
        "total_amount": total_amount,
        "by_category": sorted_categories
    }
