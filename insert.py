import mysql.connector
db_config = {'host':'localhost', 'password':'heena@164', 'user':'root', 'database' : 'students'}

conn = mysql.connector.connect(**db_config)
cursor = conn.cursor()

val = [(7, 'Katrina', 35, 'Bandra', '123789', 'F'),
(8, 'Alia', 22, 'Juhu', '45321', 'F')]


query = "insert into students_details(id, name, age, address, phone_no, gender) values(%s, %s, %s, %s, %s, %s)"


cursor.executemany(query, val)
conn.commit()
conn.close()

print('Insert data successfully')