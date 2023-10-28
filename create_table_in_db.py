#To create a new table in an SQLite database from a Python program;
#1. Create a connection object using the connect()fucntion to the SQLite3 module.
#2. Create a cursor object by calling the cursor() method of the connection object
#3. pass the CREATE TABLE statement to the execute() method of the cursor object and execute this method.

#Let's see how to create new tables in Python 
import sqlite3
from sqlite3 import Error
#First we create a connection to the database file where the tables are to be stored.
def create_connection(db_file):
    """Create a database connection to the  SQlite database specified by db_file
    :param db_file: database file
    : return : connection object or None"""
    conn=None 
    try:
        conn=sqlite3.connect(db_file)
        return conn
    except Error as e :
        print(e)
    return conn

# second, develop a function named  create_table()that accepts a connection object 
# and an SQL statement. Inside the function, we call the execute() method of the cursor object
# #to execute the CREATE TABLE statement 
def create_table(conn,create_table_sql):
    try:
        c=conn.cursor() #creating a cursor object 
        c.execute(create_table_sql)
    except Error as e:
        print(e)

# third, create a main() function to create the projects and tasks tables.
def main():
    database=r"c:\sqlite\db\pythonsqlite.db"

    sql_create_projects_table="""CREATE TABLE IF NOT EXISTS projects(
                                id integer PRIMARY KEY,
                                name text NOT NULL,
                                begin_date text,
                                end_date text                       
                            );"""
    
    sql_create_tasks_table="""CREATE TABLE IF NOT EXISTS tasks (
                            id  integer PRIMARY KEY,
                            name text NOT NULL,
                            priority integer,
                            status_id integer NOT NULL, 
                            project_id integer NOT NULL,
                            begin_date text NOT NULL,
                            end_date text NOT NULL,
                            FOREIGN KEY (project_id) REFERENCES projects(id)
                        );"""
    #create a database connection 
    conn=create_connection(database)

    #create tables
    if conn is not None:
        #create projects table
        create_table(conn,sql_create_projects_table)
        #create tasks table 
        create_table(conn,sql_create_tasks_table)
    else:
        print("Error! I cannot create a  database connection.")

#Fourth , execute the main() function
if __name__=="__main__":
    main()
    