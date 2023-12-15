import sqlite3

connection = sqlite3.connect("health_analysis.db")

cursor = connection.cursor()

try:
    cursor.execute("drop table patient")
    cursor.execute("drop table doctor")
except:
    pass

cursor.execute("create table patient(pid integer,patient_name text primary key,age integer,gender text, problem text,appointment_time integer)")
cursor.execute("create table Doctor(spid integer,speciallist text primary key,appointment_time integer,foreign key(appointment_time) references patient(appointment_time))")
cursor.execute("""INSERT INTO patient values(1,'suresh',22,'male','headache', 5 )""")
cursor.execute("""INSERT INTO Doctor values(1,'neurologist',5)""")
connection.commit()
connection.close()
print("done.")
