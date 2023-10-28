#To create data in an SQLite database, 
#1.Establish a connection to the database 
#2.Create a cursor object 
#3.Execute a Select Statement 
#4.Call the  fetchall() method of the cursor object to fetch the data 
#5.Finally loop the cursor and process each row individually 
import sqlite3
from sqlite3 import Error 

def create_connection(db_file):
    conn=None 
    try:
        conn=sqlite3.connect (db_file)
        return conn
    except Error as e:
        print(e)
    return conn

def select_all_tasks(conn):
    """Query all rows in the tasks table 
    :param conn: the connection object 
    :return:
    """
    cur=conn.cursor()
    cur.execute("SELECT * FROM tasks")
    rows=cur.fetchall()
    for row in rows:
        print(row)

#This function querries tasks by priority
def select_task_by_priority(conn,priority):
    """Query tasks by priority"""
    cur=conn.cursor()
    cur.execute("SELECT * FROM tasks WHERE priority=?",(priority))
    rows=cur.fetchall()
    for row in rows:
        print(row)

def main():
    database=r"C:\sqlite\db\pythonsqlite.db"
    conn=create_connection(database)
    with conn:
        print("1.Query task by priority: ")
        select_task_by_priority(conn,1)

        print("2.Query all tasks")
        select_all_tasks(conn)

if __name__=="__main__":
    main()
    