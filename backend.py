import sqlite3


def connect():
    conn = sqlite3.connect("RRRhostel.db")
    cur = conn.cursor()
    cur.execute(
        "create table if not exists hostel(id integer primary key,name text ,room_no integer,phone_no text,year integer )")
    conn.commit()
    conn.close()


def insert(name, roomno, phoneno, year):
    conn = sqlite3.connect("RRRhostel.db")
    cur = conn.cursor()
    cur.execute(
        "insert into hostel values (NULL,?,?,?,?)", (name, roomno, phoneno, year))

    conn.commit()
    conn.close()


def view():
    conn = sqlite3.connect("RRRhostel.db")
    cur = conn.cursor()
    cur.execute("select * from hostel")
    rows = cur.fetchall()
    conn.close()
    return rows


def search(name="", roomno=0, phoneno="", year=0):
    conn = sqlite3.connect("RRRhostel.db")
    cur = conn.cursor()
    cur.execute("select * from hostel where name=? or room_no=? or phone_no=? or year=? ",
                (name, roomno, phoneno, year))
    rows = cur.fetchall()
    conn.close()
    return rows


def delete(id):
    conn = sqlite3.connect("RRRhostel.db")
    cur = conn.cursor()
    cur.execute("Delete from hostel where id=?", (id,))
    conn.commit()
    conn.close()


def update(id, name, roomno, phoneno, year):
    conn = sqlite3.connect("RRRhostel.db")
    cur = conn.cursor()
    cur.execute("update hostel set name=?,room_no=?,phone_no=?,year=? where id=?", (name, roomno, phoneno, year, id))
    conn.commit()
    conn.close()


connect()
