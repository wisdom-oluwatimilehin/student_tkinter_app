import mysql.connector

myconn = mysql.connector.connect(
    host='localhost',
    user='root',
    passwd = '', 
    port='3308'
    )

if myconn:
    print('connection successful')
else:
    print('connection failed')