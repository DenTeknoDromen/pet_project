import mysql.connector


mydb = mysql.connector.connect(
    host="localhost",
    port="3306",
    user="root",
    password="root",
    database="person"
    )

def load_persons(person):
        mycursor = mydb.cursor()
        mycursor.execute(f"INSERT INTO persons (name, surname, personal_number, "
                        f"phone, email, adress, postal_code, city) "
                        f"VALUES ('{person.name}', '{person.surname}', "
                        f"'{person.personal_num}', '{person.phone}', "
                        f"'{person.email}', '{person.adress}', "
                        f"'{person.postal_code}', '{person.city}')")
        print("Row added")
        mydb.commit()

def load_activity(activity):
        mycursor = mydb.cursor()
        mycursor.execute(f"INSERT INTO activities (name, space, "
                        f"members, date, start_time, stop_time) "
                        f"VALUES ('{activity.name}', '{activity.space}', "
                        f"'{activity.get_jsonmembers()}', '{activity.date}', '{activity.time}', "
                        f"'{activity.until}')")
        print(f"Row added: {activity.name}")
        mydb.commit()

def nice_row(row):
        row = (f"{row[1]} i {row[2]}\n"
                    f"{row[4].strftime('%b %e %Y')}\n"
                    f"kl {row[5].strftime('%H:%M')} - "
                    f"{row[6].strftime('%H:%M')}\n")   
        
def list_space(space):
        mycursor = mydb.cursor()
        mycursor.execute(f"SELECT * FROM activities WHERE space = '{space}'")
        result = mycursor.fetchall()
        for x in result:
               print(nice_row(x))  

def list_date(date):
        mycursor = mydb.cursor()
        mycursor.execute(f"SELECT * FROM activities WHERE date = '{date}'")
        result = mycursor.fetchall()
        for x in result:
               print(nice_row(x))

def closedb(self):       
    self.mydb.commit()
    self.mycursor.close()
    self.mydb.close()
