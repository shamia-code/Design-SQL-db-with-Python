import sqlite3
from sqlite3 import Error
def create_connection(db_file):
    """create a database connection to the SQLite database
            specified by the db_file """
    
    conn=None
    try:
        conn=sqlite3.connect(db_file)
    except Error as e:
        print(e)
    return conn

#THe following delete_task() deletes a task in the tasks table 
def delete_task(conn,id):
    sql='DELETE FROM tasks WHERE id=?'
    cur=conn.cursor()
    cur.execute(sql,(id,))
    conn.commit()

def delete_all_tasks(conn):
    """Delete all rows in the tasks table """
    sql='DELETE FROM tasks'
    cur=conn.cursor()
    cur.execute(sql)
    conn.commit()


#THe main function calls the create_connection() function and the delete _task( function to delete the task with id 2 from the tasks table .)
def main():
    database=r"C:\sqlite\db\pythonsqlite.db"
    
    #create a database connection
    conn=create_connection(database)
    with conn:
        delete_task(conn,3)
        #delete_all_tasks(conn)

if __name__ == "__main__":
    main()

