import psycopg2

class User:
    def connect(self):
        self.conn = psycopg2.connect("postgres://kkozcyga:NLOs-dR_bc0wFy_fqX7tJlVSTmn92vg5@baasu.db.elephantsql.com:5432/kkozcyga")
        self.cur = self.conn.cursor()

    def close(self):
        self.conn.commit()
        self.cur.close()
        self.conn.close()

    def createNewUser(self,login,password):
        check = self.checkUser(login)

        if(check == True):
            self.connect()
            self.cur.execute("insert into users (login,password) values('%s','%s');" % (login,password))
            self.close()
            return print("Udało się dodać nowego użytkownika")
        else:
            return print("Niestety użytkownik po podanym loginie już istnieje")


    def checkUser(self,login):
        self.connect()
        self.cur.execute("select * from users")

        pom = self.cur.fetchall()
        self.close()
        for x in pom:
            if(x[0] == login):
                return False
        return True

    def login(self,login,password):
        self.connect()
        self.cur.execute("select * from users")
        pom = self.cur.fetchall()
        for x in pom:
            if(x[0] == login and x[1] == password):
                print("Udało ci się zalogować!")
            else:
                print("niestety nie udało ci się zalogować")
        self.close()
