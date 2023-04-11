import mysql.connector

conn = mysql.connector.connect(host = 'localhost', password = 'heena@164', user = 'root', database = 'students')

cursor = conn.cursor()

query = 'DELETE FROM students_details WHERE id = 8'

cursor.execute(query)

conn.commit()

conn.close()

print('Row Deleted Successfully')