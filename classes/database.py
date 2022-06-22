import sqlite3


class Database:
    def __init__(self):
        db_name = "database.db"

        self.conn = sqlite3.connect(db_name)
        self.cur = self.conn.cursor()
        self.cur.execute("CREATE TABLE IF NOT EXISTS legends (id INTEGER PRIMARY KEY)")
        self.cur.execute("CREATE TABLE IF NOT EXISTS token (token TEXT PRIMARY KEY)")
        self.cur.execute("CREATE TABLE IF NOT EXISTS levels (id INTEGER PRIMARY KEY, level INTEGER)")
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

    def get_levels(self):
        self.cur.execute("SELECT * FROM levels")
        levels_list = self.cur.fetchall()
        levels_ids = list()
        for level in levels_list:
            levels_ids.append(level[0])
        return levels_ids

    def get_level(self, user_id):
        self.cur.execute("SELECT * FROM levels WHERE id=?", (user_id,))
        level_value = self.cur.fetchone()
        return level_value[1]

    def set_level(self, user_id, level):
        self.cur.execute("INSERT OR REPLACE INTO levels (id, level) VALUES (?, ?)", (user_id, level))
        self.conn.commit()
