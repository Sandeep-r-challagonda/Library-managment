import Books_Librarians
import Members
import Login_register
import pandas as pd
import os
import json
from datetime import datetime, date, timedelta
import requests
import time
import csv
import ast
import sys
import mysql.connector








def fetch_bookfromdb():
    global book_obj
    book_id = input("Enter the BookId to work with: ")
    cursor_object.execute(f"SELECT * FROM books WHERE BookID= '{book_id}'  ")
    results = cursor_object.fetchone()
    if results:
        #print(results)
        #result = results.pop() 
        BookTitle = results[1]
        author_name = results[2]
        publication_company = results[3]
        Rented_date = results[4]
        Rented_user = results[5]
        book_obj = Books(book_id,BookTitle,author_name,publication_company,Rented_user,Rented_date)
    return book_obj
        
def fetch_librarianfromdb():
    Librarian_id = input("Enter your Librarian ID to work with: ")
    cursor_object.execute(f"SELECT * FROM librarians WHERE Librarian_Id= '{Librarian_id}'  ")
    results = cursor_object.fetchone()
    if results:
        #print(results)
        #result = results.pop() 
        Librarian_name = results[1]
        phone_number = results[2]
        
        Librarian_obj = Librarian(Librarian_name, phone_number,Librarian_id,book_object =book_obj )
    return Librarian_obj

def fetch_memberobjfromdb():
    member_id = input("Enter the MemberID to work with: ")
    cursor_object.execute(f"SELECT * FROM members WHERE MemberID= '{member_id}'  ")
    results = cursor_object.fetchone()
    if results:
        member_id = member_id
        member_name = results[1]
        member_ph_number = results[2]
        member_penalty_fees = results[3]
        member_notifications = results[4]
        mem_obj = Members(member_id,member_name, member_ph_number,member_notifications,member_penalty_fees)
    return mem_obj
    
    
    
    
    
    
def add_new_librarian():
    #(self, name, ph_number, librarian_ID, book_object)
    name = input("Enter the New librarian name: ")
    ph_number = input("Enter the phone number: ")
    Libr_ID = input("Enter the Librarian ID (should be integer digits): ")
    book1 = Books("testID","name_unknown","unknown_writer" ,"test_company", "test_user", " ")
    lib_obj = Librarian(name, ph_number,Libr_ID, book1)
    Librarian.add_Librarian(lib_obj)
    
    
    
def lib_many_books():
    import pandas as pd
    filename = input("Enter the name of file with newbooks: ")
    books_data = pd.read_csv(f"{filename}")
    books_data.Rented_date = " "
    books_data.Rented_user = "available"
    list_int = []
    for x in books_data.BookID :
        #print(type(x))
        x =str(x)
        #print(type(x))
        list_int.append(x)

    books_data["BookID"] =list_int
    all_books_list = []
    for row in range(0,len(books_data)):

        line_books = books_data.iloc[row,:]
        all_books_list.append(tuple(line_books))
    Librarian.add_manybooks(all_books_list)
    print("Books are successfully added")    
    
    
    
def update_booksindb():
    book_id = input("Enter the BookID to update: ")
    booktitle = input("Enter the book title: ")
    author_name = input("Enter the author name: ")
    publication_company = input("Enter the Publication company: ")
    rented_date = input("Enter the rented  date (ex:01-05-2021 format):: ")
    rented_user = input("Enter the rented user:")
    Book_obj = Books(book_id, booktitle,author_name,publication_company,rented_user, rented_date)
    Librarian.update_bookdetails(Book_obj)



# Update memberdetals
def update_memdetails():
    global notifications,Fees 
    mem_id = input("Enter the member ID: ")
    mem_name = input("Enter the member name: ")
    ph_number = input("Enter the user contact number: ")
    notifications = " "
    Fees = "0"
    Mem_object = Members(mem_id, mem_name,ph_number, notifications, Fees )
    Librarian.update_user(Mem_object)


# to delete a book
def book_delete():
    book_obj = fetch_bookfromdb()
    Librarian.delete_a_book(book_obj)


# to delete a member
def delete_memberfromdb():
    mem_obj = fetch_memberobjfromdb()
    Librarian.delete_a_member(mem_obj)


def members_choice():
    
    while True:
    
        menu =  """
                1. Login 
                2.Register
                """
        choice = input(menu)
        if choice == "1":
            login()
            break

        elif choice =="2":
            registration()
            break

        else:
            print("Enter correct choice")
            continue    
    
    
    
    
def Librarian_choice():
    menu ="""
            1.add user
            2.add Librarian
            3.add books
            4.update Members details
            5.update book details
            6.delete user
            7.delete book
            8.See all books and details
            9.See only available books
        """
    operation = input(menu)
    while True:
        if operation == "1":
            registration()
            break

        elif operation == "2":
            add_new_librarian()
            break

        elif operation == "3":
            lib_many_books()
            break

        elif operation == "4":
            update_memdetails()
            break

        elif operation == "5":
            update_booksindb()
            break

        elif operation == "6":
            delete_memberfromdb()
            break
        elif operation == "7":
            book_delete()
            break
        elif operation == "8":
            df_1 =Librarian.see_all_books()
            df_1
            break
        elif operation == "9":
            df_av = Librarian.query_avail_books()
            df_av
            break
            
        else:
            print("Please enter choices only between 1 to 9 only \n"
                    f"you have entered {operation}, Try again!")
            Librarian_choice()    
    
    
    
    
    
    
def main():
    main_menu ="""
                1.for Librarians
                2. For members
                """
    mem_choice = input(main_menu)
    if mem_choice =="1":
            Librarian_choice()

    elif mem_choice=="2":
        members_choice()

    else:
        print("Make a correct entry: ")
        main()
    
    

if __name__ == "__main__":


    config = {
    'user': 'root',
    'password': ' ', # insert your password here
    'host': ' ', # Enter your host address here example: 171.1.0.0 etc.
    'port': '3306',
    "database":"library",
    'raise_on_warnings': True,}

    cnx = mysql.connector.connect(**config)    
    cursor_object = cnx.cursor(buffered= True)
    cols = ["BookID", "Titlename", "Title author", "Publisher","Rented Date", "status/Rented User"]
    main()
 
     
    
    
    
    
