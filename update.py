import mysql.connector

mysql = mysql.connector.connect(
host="localhost", 
username="root", 
password="heena@164", 
database="students"
) 
my_cursor = mysql.cursor() 
  
query = "update students_details set name='Aamir', gender='M' where id = 3 "

my_cursor.execute(query)

mysql.commit()

print("data is updated")
