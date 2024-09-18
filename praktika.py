import random
import sqlite3

# первое задание
# first_task = sqlite3.connect('first_task.db')
# cursor_first = first_task.cursor()
# cursor_first.execute('''CREATE TABLE IF NOT EXISTS tab_1(number Integer, col_1 TEXT, col_2 TEXT)''')
# number = int(input("введите число"))
# cursor_first.execute('''insert into tab_1(number, col_1, col_2) values (?, 'kdbs', 'ksjdksj')''',
#                      (number, ))
# first_task.commit()
# cursor_first.execute('''select * from tab_1''')
# rows = cursor_first.fetchall()
# for row in rows:
#     print(row)


# второе задание (посчитать среднее арифметическое полей без уечта id
# conn = sqlite3.connect('second_task.db')
# cursor = conn.cursor()
# cursor.execute('''create table if not exists tab_1(id integer primary key autoincrement,
#                                                     col_1 integer, col_2 integer)''')
# number = int(input("Введите число записей: "))
# for i in range(number):
#     cursor.execute('''INSERT INTO tab_1(col_1, col_2) VALUES (?, ?)''',
#                    (random.randint(0, 10), random.randint(0, 10)))
#     conn.commit()
#
# cursor.execute('''SELECT col_1, col_2 FROM tab_1''')
# rows = cursor.fetchall()
# total_sum = sum(row[0] + row[1] for row in rows)
# record_count = len(rows)
# print(rows, record_count)
# average = total_sum / (2 * record_count)
# if average > record_count:
#     cursor.execute('''DELETE FROM tab_1 WHERE id = 4''')
#     conn.commit()
#
# conn.close()


# третье задание
#                                                     col_1 integer, col_2 integer)''')
# number = int(input("Введите число записей: "))
# for i in range(number):
#     cursor.execute('''INSERT INTO tab_1(col_1, col_2) VALUES (?, ?)''',
#                    (random.randint(0, 9), random.randint(0, 9)))
#     conn.commit()
#
# cursor.execute('''SELECT id, col_1, col_2 FROM tab_1''')
# rows = cursor.fetchall()
# chosen_row = rows[random.randint(0, len(rows) - 1)]
# print("Выбранная строка:", chosen_row)
# if chosen_row[1] % 2 == 0 and chosen_row[2] % 2 == 0:
#     cursor.execute('''DELETE FROM tab_1 WHERE id = ?''', (chosen_row[0],))
#     conn.commit()
#     print("Строка удалена")
# else:
#     cursor.execute('''UPDATE tab_1 SET col_1 = 2, col_2 = 2 WHERE id = ?''', (chosen_row[0],))
#     conn.commit()
#     print("Строка обновлена до col_1 = 2 и col_2 = 2")
#
# conn.close()

# Четвертое задание

# conn = sqlite3.connect('fourth_task.db')
# cursor = conn.cursor()
# cursor.execute('''create table if not exists tab_1(id integer primary key autoincrement, col_1 integer)''')
# conn.commit()
# k = cursor.fetchall()
# print(k)
#
#
# class Database:
#     def one_task(self, a=None, b=None, c=None):
#         if a is not None and b is None and c is None:
#             cursor.execute('''insert into tab_1(col_1) values (3)''')
#             conn.commit()
#         elif a is not None and b is not None and c is None:
#             if type(b) is int:
#                 cursor.execute('''delete from tab_1 where id = 1''')
#                 conn.commit()
#         elif a is not None and b is not None and type(c) is int:
#             cursor.execute('''update tab_1 set col_1 = 77 where id = 3''')
#             conn.commit()
#
#
# qwe = Database()
# qwe.one_task('1')
# cursor.execute('''select * from tab_1''')
# k = cursor.fetchall()
# print(k)


# пятое задание

conn = sqlite3.connect('fifth_task.db')
cursor = conn.cursor()
cursor.execute('''create table if not exists tab_1(id integer primary key autoincrement, col_1 text, col_2 text)''')
conn.commit()
for i in range(3):
    cursor.execute('''insert into tab_1 (col_1, col_2) values ('sdf', 'sdfsdfsdf')''')
    conn.commit()
# for i in range(2):
#     cursor.execute('''delete from tab_1 where id in (1, 2)''')
#     conn.commit()
cursor.execute('''update tab_1 set col_1='hello', col_2='world' where id = 3''')
conn.commit()
cursor.execute('''select * from tab_1''')
k = cursor.fetchall()
print(k)
