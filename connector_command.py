import mysql.connector
conn = mysql.connector.connect(host = 'localhost', password = 'heena@164', user = 'root', database = 'students' )
my_cursor = conn.cursor()
conn.commit()
conn.close()

print('Connection Successfully Created')
