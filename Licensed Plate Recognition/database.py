import datetime
import sqlite3

title ="license"

def create( plate_number, owner_name,  car_name ):
    con = sqlite3.connect(title+'.db')
    with con:
        cursor = con.cursor()
    cursor.execute("CREATE TABLE IF NOT EXISTS details(plate_number TEXT, owner_name TEXT, car_name TEXT, date_created TEXT)")

    cursor.execute("SELECT * FROM DETAILS WHERE plate_number = ? ", (plate_number,))
    if(cursor.fetchone()):
        con.commit()
        con.close()
        return "Plate Number already exist"

    else:
        cursor.execute("CREATE TABLE IF NOT EXISTS "+plate_number+"( views TEXT)",)
        cursor.execute("INSERT INTO DETAILS(plate_number, owner_name, car_name, date_created) VALUES(?,?,?,?)",
                       (plate_number, owner_name, car_name, datetime.datetime.now().strftime("%d-%m-%Y %H:%M:%S"),))
        con.commit()
        con.close()
        return("Done")



def search(plate_number):
    con = sqlite3.connect(title + '.db')
    with con:
        cursor = con.cursor()

    cursor.execute("SELECT * FROM DETAILS WHERE plate_number = ? ", (plate_number,))

    value = cursor.fetchall()
    # U8NTBAD
    if (value):
        cursor.execute("INSERT INTO "+plate_number+"(views) VALUES(?)",
                       (datetime.datetime.now().strftime("%d-%m-%Y %H:%M:%S"),))
        cursor.execute("SELECT * FROM "+plate_number,)
        value2= cursor.fetchall()
        con.commit()
        con.close()
        return value, value2
    else:
        con.commit()
        con.close()
        return None

if __name__ == "__main__":
    print(create("gggggg", "Olamide", "BMW"))
    print( search('gggggg'))

    # for values in result:
    #     for v in values:
    #         print(v)