import psycopg2

class elephant:




    def connect(self):
        self.conn = psycopg2.connect("postgres://nttxacmw:Y6vWv0KDbMEzuzJ9GYDRveSzIjEpe_3f@baasu.db.elephantsql.com:5432/nttxacmw")
        self.cur = self.conn.cursor()

    def close(self):
        self.conn.commit()
        self.cur.close()
        self.conn.close()

    def createTable(self):
        self.connect()
        self.cur.execute("create table test (id serial, num integer);")

        self.close()

    def insertIntoTable(self,query):
        self.connect()
        self.cur.execute(query)

        self.close()

    def selectFrom(self, query):
        self.connect()
        self.cur.execute(query)
        pom = self.cur.fetchone()
        print(pom)
        self.close()