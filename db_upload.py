import csv
import psycopg2
import os

conn = psycopg2.connect(
    host="lallah.db.elephantsql.com",
    database="kcfdmyuk",
    user="kcfdmyuk",
    password="321lqgZs0i9aFLC1HOxjxOGMkEcQuWkZ"
)

cur = conn.cursor()
cur.execute("DROP TABLE IF EXISTS seoul_case;")
cur.execute("DROP TABLE IF EXISTS seoul;")
#cur.execute("SET datestyle TO iso, dmy;")

cur.execute("""
CREATE TABLE seoul(
    id serial primary key,
    date DATE , 
    hightemp float,
    lowtemp float,
    injured float
);
""")
conn.commit()

with open('/Users/woomin/Desktop/Section_3/project3/seoul_data.csv','r') as csvfile:
    reader = csv.reader(csvfile)
    next(reader, None) #헤더스킵
    for row in reader:
        date = (row[0])
        hightemp = (row[1])
        lowtemp = (row[2])
        injured = (row[3])

        cur.execute("INSERT INTO seoul(date, hightemp, lowtemp, injured) VALUES (%s,%s,%s,%s); ", (row[0],row[1],row[2],row[3]))
        conn.commit()


cur.execute("""
CREATE TABLE seoul_case(
    id serial primary key,
    date DATE, 
    cases int
);
""")

conn.commit()

with open('/Users/woomin/Desktop/Section_3/project3/case_data.csv','r') as csvfile:
    reader = csv.reader(csvfile)
    next(reader, None) #헤더스킵
    for row in reader:
        date = (row[0])
        cases = (row[1])
        cur.execute("INSERT INTO seoul_case(date, cases) VALUES (%s,%s); ", (row[0],row[1]))
        conn.commit()

cur.close()
conn.close()