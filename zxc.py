import math
import random
import sqlite3
import paramiko

sshclient = paramiko.SSHClient()
sshclient.set_missing_host_key_policy(paramiko.AutoAddPolicy())
sshclient.connect(hostname="89.223.66.96", username="root", password="kt+Kkm8WHJM.DV")

# lst = ['люкс', 'стандарт', 'апартамент', 'стандарт', 'стандарт', 'стандарт', 'стандарт', 'стандарт', 'стандарт', 'сьют']
# db = sqlite3.connect("data.db")
# cursor = db.cursor()
# # Стоимость номера = 1500 * тип (1 - стандарт, 1.5 - люкс, апартамент - 1,75, 2 - сьют) * ((площадь / 10) / 2) + (кол-во комнат - 1) * 500 + кол-во двуместных кроватей * 750 + количество одноместных кроватей * 500
# print(lst)
# for i in range(1, 51):
#     if i % 10 == 0:
#         random.shuffle(lst)
#         print(lst)
#     index = (i) % 10
#     if lst[index] == "сьют":
#         koef = 2
#         pl = random.choice([75, 80, 85, 90, 95, 100])
#         rooms = random.randint(3, 5)
#     elif lst[index] == "апартамент":
#         pl = random.choice([40, 45, 50, 55, 60])
#         koef = 1.75
#         rooms = random.randint(2, 3)
#     elif lst[index] == "люкс":
#         koef = 1.5
#         pl = random.choice([35, 40, 45, 50])
#         rooms = 2
#     else:
#         pl = random.choice([15, 20, 25])
#         rooms = 1
#         koef = 1
#     onePlace = random.randint(0, 2)
#     twoPlace = random.randint(0, 1)
    
#     if i in range(1, 11):
#         floor = 1
#     elif i in range(11, 21):
#         floor = 2
#     elif i in range(21, 31):
#         floor = 3
#     elif i in range(31, 41):
#         floor = 4
#     elif i in range(41, 51):
#         floor = 5

#     price = 1500 * koef * (pl / 15) / 2 + (rooms - 1) * 500 + onePlace * 500 + twoPlace * 750
#     print(math.ceil(price / 200) * 200)

#     info = f"""
# Этаж: {floor}
# Тип: {lst[index]}
# Количество одноместных кроватей: {onePlace}
# Количество двуместных кроватей: {twoPlace}
# Количество комнат: {rooms}
# Площадь: {pl} кв.м
# Даты бронирования:
# """
#     cursor.execute(f'INSERT INTO RoomDescriptions (number, floor, type, onePlace, twoPlace, rooms, area, price, checkinout) VALUES ({i}, {floor}, "{lst[index]}", {onePlace}, {twoPlace}, {rooms}, {pl}, {price}, "")')

# db.commit()

# на вход подается два промежутка дат типа строки (["30.05.2024", "15.06.2024"] и ["10.06.2024", "28.06.2024"]). Нужно вывести True, если эти даты пересекают друг друга, иначе False. Напиши на Python
ftp = sshclient.open_sftp()


# ftp.get("/home/fletbot/bron/data.db", "data.db")
ftp.put("data.db", "/home/fletbot/bron/data.db")