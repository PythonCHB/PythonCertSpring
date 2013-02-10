#! /usr/bin/env python
#
# An SQL demo.  This builds a simple customer database
# However, it will work with either sqlite3 or mysql
# The hierarchy of objects is
# business CONTAINS databases
# databases CONTAINS tables
# tables CONTAINS records
# records CONTAINS fields

import datetime
import sys

def print_users_by_state(state):
    cursor.execute("""SELECT first_name, last_name, city FROM customer where state="%s";"""%state)
    for row in cursor.fetchall():
        print row[0],row[1],row[2]




argv1 = str.lower(sys.argv[1])
if argv1 == "sqlite3" :
    import sqlite3
    connection = sqlite3.connect('business.db')
elif argv1 == "mysql" :
    import MySQLdb
    connection = MySQLdb.connect(host='localhost', user='test', passwd='test',
                                 db='business')
else :
    print "Usage is \npython %s sqlite3\nor\npython %s mysql\n" % ( sys.argv[0],
                                                                    sys.argv[0] )
    sys.exit(1)
    
cursor = connection.cursor()

# Since we are starting from scratch, delete the table if it already exists.
cursor.execute("""DROP TABLE IF EXISTS customer""")

cursor.execute("""CREATE TABLE customer  (
first_name VARCHAR(15) NOT NULL,
last_name VARCHAR(15) NOT NULL,
address_1 VARCHAR(30) NOT NULL,
address_2 VARCHAR(30),
city VARCHAR(20) NOT NULL,
state CHAR(2) NOT NULL,
zipcode CHAR(5) NOT NULL,
signup_date DATE ) """)

today = datetime.date.today()

customers=[\
    ("Jeff","Silverman","924 20th AVE E","","Seattle","WA","98112", today),
    ("Robin","Finch","The Aviary","1100 Nowhere st","Utopia","KS","75024", today),
    ("Felix","Felis","1103 SW 23rd st","","Chicago","IL","68123", today),
    ("Jay","Inslee","Governors Mansion","Capitol Grounds", "Olympia", "WA", "98501", today ),
    ]

try :
    for customer in customers:
        cursor.execute('''INSERT INTO customer (
    first_name, last_name, address_1, address_2, city, state, zipcode, signup_date)
    VALUES ( '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s' )''' % customer )
finally :  
    connection.commit()

print_users_by_state("WA")


connection.close()

