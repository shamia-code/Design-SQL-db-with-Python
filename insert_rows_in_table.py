#To insert rows into a table in a SQLite database, you use the following steps 
#1. connect to the SQLite database by creating a connection object 
#2. create a cursor object by calling the cursor method of the connection object 
#3. Execute an INSERT statement 
#Note:If you want to pass arguments to the INSERT statement, you use the question mark(?) as a place holder for each argument
import  sqlite3
from sqlite3 import Error 

#creating a function to establish a connection to the database 
def create_connection(db_file):
    conn=None 
    try:
        conn=sqlite3.connect (db_file)
        return conn
    except Error as e:
        print(e)
    return conn
# creating a function to insert a new project into the projects table 
def create_project(conn,project):
    """Create a new project into the projects table
    :param conn :
    param project:
    return:project id"""

    sql="""INSERT INTO projects(name,begin_date,end_date)
                                VALUES(?,?,?)"""
    cur=conn.cursor()
    cur.execute(sql,project)
    conn.commit()
    #We use the lastrowid attribute of the cursor to object to get the generated id .
    return cur.lastrowid

#We develop another function for inserting rows into the tasks table
def create_task(conn,task):
    sql= """INSERT INTO tasks (name,priority,status_id, project_id,begin_date,end_date)
                                VALUES(?,?,?,?,?,?)"""
    cur=conn.cursor()
    cur.execute(sql,task)
    conn.commit()
    return cur.lastrowid

def main():
    database = r"c:\sqlite\db\pythonsqlite.db"

    #create the database connection
    conn=create_connection(database)
    if conn is None:
        print("Error! cannot create the database connection")
        return 
    with conn:
        #create a new project 
        project=('Cool App with SQLite & Python', '2025-01-01','2025-01-30')
        project_id=create_project(conn,project)

        task_1=('Analyze the requirements of the App',1,1,project_id,'2025-01-01','2025-01-02')
        task_2=('Confirm with the user about the top requirements',1,1,project_id,'2025-01-01','2025-01-03')

        #create tasks 
        create_task(conn,task_1)
        create_task(conn,task_2)

if __name__=='__main__':
    main()

