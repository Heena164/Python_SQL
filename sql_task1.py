import mysql.connector

conn = mysql.connector.connect(host = 'localhost', password = 'heena@164', user = 'root', database = 'stud')
cursor = conn.cursor()

# q1 = 'create table details (id INT NOT NULL UNIQUE, name VARCHAR(50) NOT NULL, age INT NOT NULL CHECK(age>=18), city VARCHAR(50))'
# cursor.execute(q1)



def add():
    r = int(input('Enter your roll no: '))
    n = input('Enter your name: ')
    a = int(input('Enter your age: '))
    c = input('Enter your city: ')
    cursor.execute('INSERT INTO details VALUES(?, ?, ?, ?)', (r, n, a, c ))
    conn.commit()

def delete():
    r = int(input('Enter your roll no to delete details: '))
    cursor.execute('DELETE FROM details WHERE id = ?', (r,))
    conn.commit()


while True:
    print('Enter a Command: ')
    print('1 - Add Details')
    print('2 - Delete Details')
    print('3 - Quit')


    command = input()

    if command == '1':
        add()

    elif command == '2':
        delete()

    elif command == '3':
        break
    else:
        print('Invalid Command') 


conn.close()
