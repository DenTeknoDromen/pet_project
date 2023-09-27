import mysql.connector


def loadpersons(person):
    mydb = mysql.connector.connect(
        host="localhost",
        port="3306",
        user="root",
        password="root",
        database="person"
    )
    mycursor = mydb.cursor()
    mycursor.execute(f"INSERT INTO persons (name, surname, personal_number, "
                     f"phone, email, adress, postal_code, city) "
                     f"VALUES ('{person.name}', '{person.surname}', "
                     f"'{person.personal_num}', '{person.phone}', "
                     f"'{person.email}', '{person.adress}', "
                     f"'{person.postal_code}', '{person.city}')")
    print("Row added")
    mydb.commit()
    mycursor.close()
    mydb.close()
