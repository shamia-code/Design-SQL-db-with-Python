
# To create a new database ,
#you have to create a connection object that represents the database using the connect() fuction 
#the connect() function takes the database you are trying to connect to as its parameter.
#note:If the database doesnot exist already, it is autoamatically created by sqlite module 
#The connect() opens a connection to the SQLite database and returns a connection object that represents the databas e.
#THe connection object can be used to perform various database operations.

#The following Python program creates a new database file  pythonsqlite.db in the c:\sqlite\db folder 
import  sqlite3
from sqlite3 import Error 

def create_connection(db_file):
    """create a database connection to a  SQLite database """
    conn=None
    try:
        #trying to initialize a connection object
        conn=sqlite3.connect(db_file)
        print(sqlite3.version)
    except Error as e:
        print(e)
    finally:
        #It is good practice to close the database connection when you are complete with it.
        if conn:
            conn.close()

if __name__=='__main__':
    #we then pass the database file to the connection function
    #THe 'r' instructions python that we are passing a raw string.
    create_connection(r"C:\sqlite\db\pythonsqlite.db")

#Note: If you pass the file name as :memory: to the connect() function , it will create a new function 
#that resides in the memory(RAM) instead of a database file on disk.
#Forexample the following program creates an SQLite database in the memory.
import sqlite3
from sqlite3 import Error

def create_connection():
    """create a database connection to a database that resides in memory """
    conn=None 
    try:
        conn=sqlite3.connect(':memory:')
        print(sqlite3.version_info)
    except Error as e:
        print(e)
    finally:
        if conn:
            conn.close()

if __name__=='__main__':
    create_connection()

