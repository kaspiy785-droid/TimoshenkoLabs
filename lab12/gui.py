import tkinter as tk
from tkinter import ttk
from pathlib import Path
from logic import find_records
from storage import load_records

def main():
    folder = Path(__file__).resolve().parent
    data_path = folder / "data.json"
    try:
        records, _ = load_records(data_path)
    except Exception:
        records = []

    root = tk.Tk()
    root.title("Поиск учебных занятий")
    root.geometry("450x300")

    query_var = tk.StringVar()
    info_var = tk.StringVar(value="Введите часть названия для поиска")

    def on_search():
        q = query_var.get().strip()
        listbox.delete(0, tk.END)
        if q == "":
            info_var.set("Ошибка: поисковый запрос не должен быть пустым")
            return
        found = find_records(records, q)
        if len(found) == 0:
            info_var.set("Ничего не найдено")
        else:
            info_var.set(f"Найдено записей: {len(found)}")
            for item in found:
                status = "Завершено" if item["completed"] else "В работе"
                listbox.insert(tk.END, f"[{item['id']}] {item['title']} ({item['category']}) - {item['amount']} ч. [{status}]")

    ttk.Label(root, text="Поисковый запрос:").pack(pady=5)
    ttk.Entry(root, textvariable=query_var, width=40).pack(pady=5)
    ttk.Button(root, text="Найти", command=on_search).pack(pady=5)
    ttk.Label(root, textvariable=info_var).pack(pady=5)

    listbox = tk.Listbox(root, width=60, height=8)
    listbox.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)

    root.mainloop()

if __name__ == "__main__":
    main()
