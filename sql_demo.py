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
import string

def print_users_by_state(state):
    cursor.execute("""SELECT first_name, last_name, city, state FROM customer where state="%s";"""%state)
    for row in cursor.fetchall():
        print row[0],row[1],row[2],row[3]

def get_credentials(db) :
    """This function opens the credentials file, which is under the control of the system
administrator.  The software engineer cannot see it"""
    credentials_file = 'credentials_file.txt'
    try :
        f = open(credentials_file,'r')
    except IOError, e:
        print """Problems opening the credentials file %s - check file protection
and EUID this database is running under"""
        sys.exit(1)
    credentials = f.readlines()
    lineno = 0
    for c in credentials :
        lineno += 1
        fields = c.split(":")
        if len(fields) != 4 :
            raise ValueError("Line %d of file %s has the wrong number of fields,\
should be 4 actually is %d" % (lineno, credentials_file, len(fields) ))
        if fields[0] == db :
            fields[3] = string.strip( fields[3] )
            f.close()
            return fields[1:4]
    else :
        raise ValueError("The credentials file %s does not contain a host/user/password tuple\
for database %s") % ( credentials, db)
    f.close()
    return

def populate_database() :
    """This subroutine populates the database.  Note that cursor and connection are passed globally"""
    today = datetime.date.today()

    customers=[\
        ("Jeff","Silverman","924 20th AVE E","","Seattle","WA","98112", today, "1"),
        ("Robin","Finch","The Aviary","1100 Nowhere st","Utopia","KS","75024", today, "2"),
        ("Felix","Felis","1103 SW 23rd st","","Chicago","IL","68123", today, "3"),
        ("Jay","Inslee","Governors Mansion","Capitol Grounds", "Olympia", "WA", "98501", today, "4" ),
        ]

    try :
        for customer in customers:
            cursor.execute('''INSERT INTO customer (
        first_name, last_name, address_1, address_2, city, state, zipcode, signup_date, customer_number)
        VALUES ( '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', %s )''' % customer )
    finally :  
        connection.commit()

   
def update_database( new_city, new_state, zipcode, customer_number ) :
    """This subroutine updates the database.  Note that cursor and connection are passed globally"""
    

    try :
        cursor.execute('''UPDATE customer SET city="%s", zipcode="%s", state="IL"
                WHERE customer_number=%s ''' % ( new_city, zipcode, customer_number ) )
    except sql.ProgrammingError,e :
        print "The update failed"
        raise
    else :
        print "The update succeeded"



def update_database_better ( new_city, new_state, zipcode, customer_number ) :
    """This subroutine updates the database.  Note that cursor and connection are passed globally
This version is better because it sanitizes the input customer_number"""
    

    try :
        customer_number = int ( customer_number ) # Guarantees that the customer number will be an integer
        cursor.execute('''UPDATE customer SET city="%s", zipcode="%s", state="IL"
                WHERE customer_number=%s ''' % ( new_city, zipcode, customer_number ) )
    except ValueError, e :
        print "Converting the customer number to an integer caused a ValueError exception.  %s" % \
        customer_number
        raise
    except sql.ProgrammingError,e :
        print "The update failed"
        raise
    else :
        print "The update succeeded"


argv1 = str.lower(sys.argv[1])
if argv1 == "sqlite3" :
    import sqlite3 as sql
    connection = sql.connect('business.db')
elif argv1 == "mysql" :
    import MySQLdb as sql
    DB = 'business'
    (host, user, password ) = get_credentials(DB)
    connection = sql.connect(host=host, user=user, passwd=password, db=DB)
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
signup_date DATE,
customer_number INT ) """)

populate_database()

print_users_by_state("WA")

new_city="Cairo"
new_state="IL"
zipcode="62914"
customer_number = "3"

update_database(new_city, new_state, zipcode, customer_number)

print_users_by_state("IL")

if len(sys.argv) == 3 and sys.argv[2]=="evil" :
    """Let's do an SQL injection attack"""
    new_city="Aurora"
    new_state="IL"
    zipcode="60503"
    customer_number = "3"
    evil = " OR 'x'='x'"
    try :
        update_database ( new_city, new_state, zipcode, customer_number + evil )
    except sql.ProgrammingError,e :
        print "The SQL injection attack failed"
    else :
        print "The SQL injection attack succeeded"

    print_users_by_state("IL")
    new_city="Miami"
    new_state="FL"
    zipcode="33101"
    customer_number = "3"
    try :
        update_database_better ( new_city, new_state, zipcode, customer_number + evil )
    except sql.ProgrammingError,e :
        print "The SQL injection attack failed"
    except ValueError,e :
        print "The SQL injection attack was prevented"
    else :
        print "The SQL injection attack succeeded"

    print_users_by_state("FL")
                       
connection.close()

