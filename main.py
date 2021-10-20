import os
import sqlite3 as db
#from tkinter import *
#from tkinter import messagebox

def add_cantact(id,name,number):
    conn = db.connect('phone_book.db')
    cursor = conn.cursor()
    insert_query = f'insert into cantact values({id},"{name}",{number})'
    cursor.execute(insert_query)
    conn.commit()
    print('add cantact')
    conn.close()


def show_cantact ( ):
    conn=db.connect('phone_book.db')
    cursor=conn.cursor()
    select_query=f'select * from cantact'
    cursor.execute(select_query)
    result=cursor.fetchall()
    for row in result:
        print(row)
    #print(result)
    #conn.commit()
    conn.close()
    print('all cantact')

def delete_cantact(name):
    conn=db.connect('phone_book.db')
    cursor=conn.cursor()
    select_query=f'delete from cantact where name="{name}"  '
    cursor.execute(select_query)
    conn.commit()
    conn.close()
    print('delete cantact')

def edite_cantact(name):
    newname=input('enter a new name:\n')
    #newnumber=input('enter a new number:\n')
    conn=db.connect('phone_book.db')
    cursor=conn.cursor()
    update_query=f'update  cantact set name="{newname}" where name="{name}" '
    cursor.execute(update_query)
    conn.commit()
    conn.close()
    print('update cantact')

# #start
ch=1
while ch!=0:


    print("1-Add_cantact \n 2-show_cantact \n 3-delete_cantact\n 4-edite_cantact\n 5-exit ")
    ch=int(input("enter a choise pleaze:\n"))
    #os.system('cls')
    if ch==1:
        name=input('enter name pleaze:\n')
        id=int(input('enter key:\n'))

        number=int(input('enter number pleaze:\n'))
        add_cantact(id,name, number)



    elif ch==2:
        show_cantact()

    # name = input('enter name pleaze:\n')


    elif ch==3:
        name = input('pleaze enter a name that should be delete :\n')
        delete_cantact(name)

    elif ch==4:
        name = input('enter name pleaze:\n')

        edite_cantact(name)

    else:
        break



