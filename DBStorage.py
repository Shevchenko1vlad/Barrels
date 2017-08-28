import sqlite3


class DBBarrels:
    def __init__(self):
        self.filename = 'barrel_db'

    def create_table(self):
        conn = sqlite3.connect(self.filename)
        curs = conn.cursor()
        curs.execute('''CREATE TABLE barrels_info (Номер_п_п INTEGER,
                                                   ID_бочки INTEGER,
                                                   Позиция_X INTEGER,
                                                   Позиция_Y INTEGER,
                                                   Номер_ячейки INTEGER,
                                                   Номер_сектора INTEGER,
                                                   Номер_отсека INTEGER,
                                                   Номер_паспорта INTEGER,
                                                   Классификация_РАО VARCHAR(100),
                                                   Категория_РАО VARCHAR(100),
                                                   Вес_упаковки INTEGER,
                                                   Нуклид VARCHAR(100),
                                                   Удельная_активность VARCHAR(100),
                                                   Сумарная_удельная_активность VARCHAR(100),
                                                   Дата VARCHAR(50))''')
        conn.commit()
        conn.close()

    def add_info(self):
        conn = sqlite3.connect(self.filename)
        curs = conn.cursor()
        curs.execute(''' ''')
        conn.commit()
        conn.close()

    def add_smth(self, n):
        conn = sqlite3.connect(self.filename)
        curs = conn.cursor()
        curs.execute('''INSERT INTO barrels_info (Номер_ячейки) VALUES(%d)''' % n)
        conn.commit()
        conn.close()

if __name__ == '__main__':
    dbb = DBBarrels()
    for i in range(1, 254):
        dbb.add_smth(i)


