#sqlite database
import sqlite
conn=sqlite.connect("user.db")
cursor=conn.cursor()
cursor.execute("CREATE TABLE IF NOT EXISTS users(id INTEGER PRIMARY KEY,name TEXT,age INTEGER)")
cursor.execute("users (name,age) VALUES(?,?)",("tarunika",19))
cursor.execute("users(name,age) VALUES(?,?)", ("nikhil",18))
conn.commit()
print("all users: ")
cursor.execute("SELECT * FROM users")
rows=cursor.fetchall()
for row in rows:
    print (row)

cursor.execute("UPDATE users SET age = ? WHERE name = ?",(20,"tarunika"))
conn.commit()
cursor.execute('DELETE FROM users WHERE name = ?', ("tarunika",))
conn.commit()
cursor.execute("SELECT * FROM users")
rows=cursor.fetchall()
for row in rows:
    print(row)

conn.close()

