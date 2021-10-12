import os
import sqlite3
import csv

DB_FILENAME1 = 'seoul_data.db'
DB_FILENAME2 = 'seoul_case.db'

DB_FILEPATH1 = os.path.join(os.getcwd(), DB_FILENAME1)
DB_FILEPATH2= os.path.join(os.getcwd(), DB_FILENAME2)

conn = sqlite3.connect(DB_FILEPATH1)
conn.commit()
cur = conn.cursor()


delete_table1 = "DROP TABLE IF EXISTS seoul;"
cur.execute(delete_table1)
conn.commit()


cur.execute("""
CREATE TABLE seoul(
    id INTEGER PRIMARY KEY,
    date DATE , 
    hightemp float,
    lowtemp float,
    injured float
);
""")
conn.commit()

with open('/Users/woomin/Desktop/Section_3/project3/seoul_app/seoul_data.csv','r') as csvfile:
    reader = csv.reader(csvfile)
    next(reader, None) #헤더스킵
    for row in reader:
        date = (row[0])
        hightemp = (row[1])
        lowtemp = (row[2])
        injured = (row[3])

        cur.execute("INSERT INTO seoul(date, hightemp, lowtemp, injured) VALUES (?,?,?,?); ", (row[0],row[1],row[2],row[3]))
        conn.commit()



conn2 = sqlite3.connect(DB_FILEPATH2)
conn2.commit()
cur2 = conn2.cursor()

delete_table2= "DROP TABLE IF EXISTS seoul_case;"
cur2.execute(delete_table2)
conn2.commit()

cur2.execute("""
CREATE TABLE seoul_case(
    id INTEGER PRIMARY KEY,
    date DATE, 
    cases int
);
""")

conn2.commit()

with open('/Users/woomin/Desktop/Section_3/project3/seoul_app/seoul_data.csv','r') as csvfile:
    reader = csv.reader(csvfile)
    next(reader, None) #헤더스킵
    for row in reader:
        date = (row[0])
        cases = (row[1])
        cur2.execute("INSERT INTO seoul_case(date, cases) VALUES (?,?); ", (row[0],row[1]))
        conn2.commit()

cur2.close()
conn2.close()

cur.close()
conn.close()