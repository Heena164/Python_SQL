import mysql.connector
conn = mysql.connector.connect(host = 'localhost', user = 'root', password = 'heena@164', database = 'stud')
cursor = conn.cursor()



def add():
    r = int(input("Enter your roll no: "))
    n = input("Enter Your name: ")
    a = int(input("Enter your age: "))
    c = input('Enter your city: ')
    query = "select * from details where name = '{}'".format(n)
    cursor.execute(query)
    
    result = cursor.fetchone()

    if result:
        print('A record with the same name already exits in a database')
    else:
        query = "Insert into details values({}, '{}', {}, '{}')".format(r, n, a, c)
        cursor.execute(query)
        conn.commit()
        print('Data Inserted Successfully..')
        
def show():
    query = 'Select * from details'
    cursor.execute(query)
    result = cursor.fetchall()
    for i in result:
        print(i) 

def delete():
    r = int(input("Enter your roll no to delete your data: "))
    query = "select * from details where id = {}".format(r)
    cursor.execute(query)
    
    result = cursor.fetchone()

    if not result:
        print('Data is not available')
    else:
        query = "Delete from details where id =({})".format(r)
        cursor.execute(query)
        conn.commit()
        print("You data deleted successfully")


    
while True:
    print('-----------------------------')
    print("1 - Add Detail")
    print("2 - Delete Detail")
    print("3 - Exit")
    choice = int(input('Enter Your Choice: '))
    print('-------------------------------')


    if choice == 1:
        add()
        show()
    elif choice == 2:
        delete()
        show()
    elif choice == 3:
        break
    else:
        print("Enter valid Input")



