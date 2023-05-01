import sqlite3 as sql


cnxn = sql.connect('my_db.db')
crsor = cnxn.cursor()

crsor.execute("create table userlist if not exists (id integer primary key, name text, designation text, salary real, department text)")
crsor.execute("create table vhm  if not exists (id integer primary key, name text, designation text, salary real, department text)")

def insert_Value(id, name, designation, salary, department):
    crsor.execute("insert into vhm values (?,?,?,?,?)", (id, name, designation,salary, department))
    cnxn.commit()

def update_department(id, department):
    crsor.execute("update userlist set department=? where id=?", (department,  id))
    cnxn.commit()

def sql_fetch():
    print(crsor.execute("select * from userlist").fetchall())

def delete_all():
    crsor.execute("delete from userlist")
    cnxn.commit()

def delete_id(id):
    crsor.execute("delete from userlist where id=?", (id) )
    cnxn.commit()

# crsor.execute("alter table column salary text")
crsor.close()
cnxn.close()

