import sqlite3 as sql


def main():
    try:
        vt = sql.connect("./db/mxsoftware.db")

        im = vt.cursor()
        im.execute("CREATE TABLE IF NOT EXISTS details (tc TEXT,date_of_birth TEXT,belt_color TEXT,"
                   "veli_name TEXT,veli_number TEXT,"
                   "lisans_no TEXT,photo BLOB , hes_code TEXT,mail TEXT)")

        vt.commit()

        db = sql.connect('./db/mxsoftware.db')
        cur = db.cursor()
        tablequery = "CREATE TABLE IF NOT EXISTS ogrenciler (tc TEXT UNIQUE, isim TEXT,soyad TEXT, telefon TEXT, brans TEXT, kayit_tarihi TEXT, bitis_tarihi TEXT)"
        tablequery3 = "CREATE TABLE IF NOT EXISTS aidatlar (tc TEXT,isim TEXT,soyad TEXT , ay TEXT, yıl TEXT , ucret TEXT)"
        cur.execute(tablequery)
        cur.execute(tablequery3)
        db.commit()

    except sql.Error as e:
        print("There is a table or an error has occurred")

    finally:

        db.close()
        vt.close()


if __name__ == "__main__":
    main()