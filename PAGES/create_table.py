import sqlite3 as sql

def main():
    try: 
        db = sql.connect('./db/mxsoftware.db')
        cur = db.cursor()
        tablequery = "CREATE TABLE IF NOT EXISTS ogrenciler (tc TEXT, isim_soyad TEXT, telefon TEXT, brans TEXT, kayit_tarihi TEXT, bitis_tarihi TEXT)"
        tablequery3 = "CREATE TABLE IF NOT EXISTS aidatlar (tc TEXT,isim_soyad TEXT , ay TEXT, yıl TEXT , ucret TEXT)"
        cur.execute(tablequery)
        cur.execute(tablequery3)
        db.commit()
        print("Table Created Succesfully")

    except sql.Error as e:
        print("There is a table or an error has occurred")

    finally:

        db.close()
        
if __name__ == "__main__":
    main()