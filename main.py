import elephantSqlConnection
import elephantSqlUser
import elephantSqlExercises


#pom = elephantSqlConnection.elephant()

#pom.insertIntoTable("insert into test(id,num) values('1','100')")

#pom.selectFrom("select * from test")

user = elephantSqlUser.User()
user.createNewUser(str(input("Podaj swój login ")),str(input("Podaj swoje haslo ")))
#user.login(str(input("Podaj swój login ")),str(input("Podaj swoje haslo ")))


