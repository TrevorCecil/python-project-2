import sqlite3

conn = sqlite3.connect('test.db')
print("Opened database successfully")

conn.execute("DELETE FROM EMPLOYEES WHERE ID=15")
conn.commit()

cursor = conn.execute("SELECT ID,NAME,AGE,SALARY FROM EMPLOYEES")

for row in cursor:
    print('ID', row[0],' ',end='')
    print('NAME', row[1],' ',end='')
    print('AGE', row[2],' ',end='')
    print('SALARY', row[3])

print('Records found')
conn.close()