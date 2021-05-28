#!C:/python/python383/python
print("Content-Type:text/html")
print()
import cgi
data=cgi.FieldStorage()
test1=data.getvalue('test1')
test2=data.getvalue('test2')
test3=data.getvalue('test3')

import cx_Oracle
connection = cx_Oracle.connect("testdb/testdb@172.16.206.81:1521/histest")
dsn = cx_Oracle.makedsn('172.16.206.81', '1521', service_name='histest')
conn = cx_Oracle.connect(user='testdb', password='testdb', dsn=dsn)
c = conn.cursor()
query="insert into message(test1,test2,test3)values(:1,:2,:3)"
val=[test1,test2,test3]
c.execute(query,val)
conn.commit()
c.close()
conn.close()
print('<br><center><h2>Welcome data is added in database<br>')
print("<style>a:hover {color: green;} </style> ")    
print("<a href='http://localhost/dashboard/message.html' style='text-decoration: none'><h3><center>GO To Entry field</h1></a>")