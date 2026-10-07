order_name = input("Название заказа: ")
customer = input("Имя заказчика: ")

item1 = "Тетради"
item2 = "Ручки"

q1 = int(input("Количество для Тетради: "))
p1 = float(input("Цена за одну штуку Тетради: "))

q2 = int(input("Количество для Ручки: "))
p2 = float(input("Цена за одну штуку Ручки: "))

delivery = float(input("Стоимость доставки: "))
discount_percent = float(input("Скидка на товары в процентах (0-100): "))
cash = float(input("Внесенная сумма денег: "))

cost1 = q1 * p1
cost2 = q2 * p2

total_items = cost1 + cost2
discount_money = total_items * (discount_percent / 100)
total_items_with_discount = total_items - discount_money

total_with_delivery = total_items_with_discount + delivery
change = cash - total_with_delivery

print("Заказ:", order_name)
print("Заказчик:", customer)
print(item1, "| Количество:", q1, "| Цена:", f"{p1:.2f}", "| Стоимость:", f"{cost1:.2f}")
print(item2, "| Количество:", q2, "| Цена:", f"{p2:.2f}", "| Стоимость:", f"{cost2:.2f}")
print("Стоимость товаров без скидки:", f"{total_items:.2f}")
print("Скидка:", f"{discount_percent:.1f}%", "(", f"{discount_money:.2f}", "руб. )")
print("Стоимость товаров со скидкой:", f"{total_items_with_discount:.2f}")
print("Доставка:", f"{delivery:.2f}")
print("ИТОГО К ОПЛАТЕ:", f"{total_with_delivery:.2f}")
print("Внесено:", f"{cash:.2f}")
print("СДАЧА:", f"{change:.2f}")
