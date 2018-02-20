import elephantSqlConnection



pom = elephantSqlConnection.elephant()

pom.insertIntoTable("insert into test(id,num) values('1','100')")

pom.selectFrom("select * from test")