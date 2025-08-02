order = {"apple": 2, "banana": 3, "pear": 1, "watermelon": 10, "chocolate": 5}

incomes = {
    "apple": 5600.20,
    "orange": 3500.45,
    "banana": 5000.00,
    "bergamot": 3700.56,
    "durian": 5987.23,
    "grapefruit": 300.40,
    "peach": 10000.50,
    "pear": 1020.00,
    "persimmon": 310.00,
}
summa = 0

chek_dikt = {}
chek_list = []
summa = 0

"""Инициализация чека в виде структуры данных словарь(dict) с присвоением ключа"""
for i_num, (key, value) in enumerate(order.items(), start=1):
    name = key
    quantyty = order.get(key, 0)
    price = incomes.get(key, 0)
    total = order.get(key, 0) * incomes.get(key, 0)
    chek_dikt[i_num] = {
        "наименование": name,
        "количество": quantyty,
        "стоимость": price,
        "общая стоимость": total,
    }
total_summa = sum([item["общая стоимость"] for item in chek_dikt.values()])

# print(chek_dikt)  # Вывод получившегося словаря/проверка
# print()

# Вывод цикл
for i_key in chek_dikt:
    print()
    for j_key, value in chek_dikt[i_key].items():
        print(f"{j_key} - {value}")
print()
print("Сумма чека:", total_summa)

# Вывод с использованием генератора
print()
print(
    "\n\n".join(
        "\n".join(f"{j_key} - {value}" for j_key, value in chek_dikt[i_key].items())
        for i_key in chek_dikt
    )
)


"""Список с вложенными списками словарей"""
for i, (key, value) in enumerate(order.items()):
    chek_list.append([])
    name = key
    quantyty = order.get(key, 0)
    price = incomes.get(key, 0)
    total = order.get(key, 0) * incomes.get(key, 0)
    chek_list[i].append(
        {
            "наименование": name,
            "количество": quantyty,
            "стоимость": price,
            "общая стоимость": total,
        }
    )
# print(chek_list)  # Вывод полученног спсика/проверка
print()

# Вывод цикл
for ind in chek_list:
    print()
    for elem in ind:
        for key, value in elem.items():
            print(key, value)

# Вывод с использованием генератора
print(
    "\n\n".join(for ind in chek_list)
        "\n".join(f"{key} - {value}" 
                  for elem in ind 
                  for key, value in elem.items())
        
    )


# Список словарей
chek_list = []
for key, value in order.items():
    name = key
    quantyty = order.get(value, 0)
    price = incomes.get(key, 0)
    total = order.get(key, 0) * incomes.get(key, 0)
    chek_list.append(
        {
            "наименование": name,
            "количество": quantyty,
            "стоимость": price,
            "общая стоимость": total,
        }
    )
print(chek_list)

