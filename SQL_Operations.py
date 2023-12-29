import pymysql

def Create_Table(): #Execute only one time to create the table.
    # localhost,username,password,database name
    db_obj=pymysql.connect(host="localhost",user="root",password="root"); # to Connect to SQl server

    cursor_obj=db_obj.cursor(); # to create a cursor on sql server

    #Query for creating database and table structure.
    db_query= """create database if not exists Student;"""
    db_query_use = """use Student"""
    table_createquery="""
    create table Student(
        Studentid int not null auto_increment primary key,
        first_name varchar(30),
        last_name varchar(30),
        gender varchar(10),
        dob varchar(10),
        email varchar(50),
        phone_number varchar(20),
        address varchar(100),
        course varchar(30),
        enrollement_year varchar(30),
        is_International varchar(20)
        );"""
    

    query=cursor_obj.execute(db_query);print(query) # to execute the sql query
    query=cursor_obj.execute(db_query_use);print(query)
    query=cursor_obj.execute(table_createquery);print(query)
    db_obj.commit() # for savings the changes to database
    db_obj.close()  # to close the database connection

def Insert_Data(first_name,last_name,gender,dob,email,phone_number,address,course,enrollement_year,is_International):
    db_obj=pymysql.connect(host="localhost",user="root",password="root"); # to Connect to SQl server
    print(db_obj)
    cursor_obj=db_obj.cursor(); # to create a cursor on sql server

    show_query="""show databases"""
    cursor_obj.execute(show_query)
    query=cursor_obj.fetchall();print(query)
    databases=list(query);print(databases)
    # if("('student',)" not in databases):
    #     Create_Table()
    #     print("Table created")
    # else:
    #     print("Tables already exists")

    db_query_use = """use Student"""
    insert_query= """insert into student(first_name,last_name,gender,dob,email,phone_number,address,course,enrollement_year,is_International)
    values('"""+str(first_name)+"','"+str(last_name)+"','"+str(gender)+"','"+str(dob)+"','"+str(email)+"','"+str(phone_number)+"','"+str(address)+"',"+'"'+str(course)+'"'+",'"+str(enrollement_year)+"','"+str(is_International)+"""');"""

    query=cursor_obj.execute(db_query_use);print(query)
    query=cursor_obj.execute(insert_query);print(query)
    db_obj.commit() # for savings the changes to database
    db_obj.close()  # to close the database connection


