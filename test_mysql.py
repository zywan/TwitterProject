import mysql.connector
mydb = mysql.connector.connect(
		host="localhost",
		user="root",
		passwd="12345678",
		database='twitter_mysql'
	)
mycursor = mydb.cursor()
mycursor.execute("SELECT * FROM user")
myresult = mycursor.fetchall()
for x in myresult:
	print(x)
mycursor.execute("SELECT * FROM activity")
myresult = mycursor.fetchall()
for x in myresult:
	print(x)
