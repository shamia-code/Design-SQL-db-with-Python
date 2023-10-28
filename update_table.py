#To update data in a table from a Python program,
#1.create a database connection 
#2.Create a cursor object of that connection 
#3.Execute the UPDATE statement

import sqlite3
from sqlite3 import Error 

def create_connection(db_file):
    conn=None
    try:
        conn=sqlite3.connect(db_file)
    except Error as e:
        print(e)
    return conn
    
def update_task(conn,task):
    sql="""
            UPDATE tasks
            SET priority=?,
            begin_date=?,
            end_date=?
            WHERE id =?
        """
    cur=conn.cursor()
    cur.execute(sql,task)
    conn.commit()

def main():
    database=r"C:\sqlite\db\pythonsqlite.db"

    #create a database connection 
    conn=create_connection(database)
    with conn:
        update_task(conn,(3, '2023-12-07','2023-12-08', 2))

if __name__=="__main__":
    main()

 