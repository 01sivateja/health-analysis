import sqlite3

connection = sqlite3.connect("health_analysis.db")

cursor = connection.cursor()

patient = cursor.execute("select * from patient")
print(patient.fetchall())
Doctor = cursor.execute("select * from Doctor")
print(Doctor.fetchall())