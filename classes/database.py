import sqlite3


class Database:
    def __init__(self):
        db_name = "database.db"

        self.conn = sqlite3.connect(db_name)
        self.cur = self.conn.cursor()
        self.cur.execute("CREATE TABLE IF NOT EXISTS legends (id INTEGER PRIMARY KEY, name TEXT)")
        self.cur.execute("CREATE TABLE IF NOT EXISTS token (token TEXT PRIMARY KEY)")
        self.conn.commit()

    def get_token(self):
        self.cur.execute("SELECT * FROM token")
        token_value = self.cur.fetchone()
        return token_value[0]

    def get_legends(self):
        self.cur.execute("SELECT * FROM legends")
        legends_list = self.cur.fetchall()
        legends_ids = list()
        for legend in legends_list:
            legends_ids.append(legend[0])
        return legends_ids
