import sqlite3

conn = sqlite3.connect('test.db')
print("Opened database successfully")

conn.execute("INSERT INTO EMPLOYEES VALUES (11,'FAITH',23,13400.00)")
conn.execute("INSERT INTO EMPLOYEES VALUES (12,'MARK',33,134000.00)")
conn.execute("INSERT INTO EMPLOYEES VALUES (13,'JANE',43,300500.00)")
conn.execute("INSERT INTO EMPLOYEES VALUES (14,'JOB',53,135000.00)")
conn.execute("INSERT INTO EMPLOYEES VALUES (15,'ALLAN',37,89000.00)")

conn.commit()#save changes

print('Records inserted successfully')

conn.close()