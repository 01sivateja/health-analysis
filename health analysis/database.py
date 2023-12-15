import sqlite3

connection = sqlite3.connect("health_analysis.db")
def get_Doc(id=None):
    cursor = connection.cursor()

    if id is None:
        cursor.execute("SELECT * FROM Doctor")
    else:
        cursor.execute(f"SELECT * FROM Doctor WHERE spid={id}")

    rows = cursor.fetchall()
    Doctor = [{'spid': row[0], 'speciallist': row[1], 'appointment_time': row[2]} for row in rows]

    return Doctor
def get_pat(id=None):
    cursor = connection.cursor()
    if id == None:
        rows = cursor.execute("select * from patient")
    else:
        rows = cursor.execute(f"select * from books where pid={id}")
    rows = cursor.fetchall()
    rows = list(rows)
    patient = [{'pid': row[0], 'patient_name': row[1], 'age': row[2], 'gender': row[3], 'problem': row[4],'appointment_time': row[5]} for row in rows]
    return patient


def add_pat(pid,patient_name,age,gender,problem,appointment_time):
    cursor = connection.cursor()
    cursor.execute("INSERT INTO patient (pid,patient_name,age,gender,problem,appointment_time) VALUES (?, ?, ?)", (pid,patient_name,age,gender,problem,appointment_time))
    connection.commit()

def add_Doc(spid,speciallist,appointment_time):
    cursor = connection.cursor()
    cursor.execute("INSERT INTO Doctor (spid,speciallist,appointment_time) VALUES (?, ?, ?)", (spid,speciallist,appointment_time))
    connection.commit()

def delete_pat(id):
    cursor = connection.cursor()
    cursor.execute(f"delete from patient where pid={id}")
    connection.commit()
def delete_Doc(id):
    cursor = connection.cursor()
    cursor.execute(f"delete from Doctor where spid={id}")
    connection.commit()
def update_Doc(spid,speciallist,appointment_time):
    cursor = connection.cursor()
    cursor.execute(f"update Doctor set spid={spid},speciallist='{speciallist}',appointment_time='{appointment_time}' where spid={id}")
    connection.commit()    
def update_pat(pid,patient_name,age,gender,problem,appointment_time):
    cursor = connection.cursor()
    cursor.execute(f"update patient set pid='{pid}',patient_name='{patient_name}',age='{age}',gender='{gender}',problem='{problem}',appointment_time='{appointment_time} where pid={id}")
    connection.commit()
def search_pat(patient_name):
    cursor = connection.cursor()
    cursor.execute(f"SELECT Doctor.spid, Doctor.speciallist, Doctor.appointment_time,patient.patient_name,Doctor.spid FROM patient JOIN Doctor ON patient.pid = Doctor.spid WHERE patient.patient_name = '{patient_name}'")
    connection.commit()
    results = cursor.fetchhall()
    return results

