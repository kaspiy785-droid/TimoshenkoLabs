import json
from pathlib import Path
from tempfile import TemporaryDirectory
from storage import load_records, save_records

with TemporaryDirectory() as tmp:
    missing = Path(tmp) / "missing.json"
    recs, loaded = load_records(missing)
    assert recs == []
    assert loaded is False

    test_file = Path(tmp) / "data.json"
    sample = [
        {"id": 1, "title": "Лекция", "category": "теория", "amount": 2, "completed": True},
        {"id": 2, "title": "Лаба 12", "category": "практика", "amount": 5, "completed": False}
    ]
    save_records(test_file, sample)

    restored, loaded = load_records(test_file)
    assert loaded is True
    assert restored == sample

    broken_file = Path(tmp) / "broken.json"
    broken_file.write_text("{broken json", encoding="utf-8")
    try:
        load_records(broken_file)
    except json.JSONDecodeError:
        pass
    else:
        assert False, "JSONDecodeError не вызван"

print("Все тесты хранилища пройдены успешно")
