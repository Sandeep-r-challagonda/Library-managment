class Books:
    def __init__(self,BookID,Booktitle,author_name,publication_company, rented_user, rented_date):
        self.BookID = BookID
        self.Booktitle = Booktitle
        self.author_name = author_name
        self.publication_company = publication_company
        self.rented_user = rented_user
        self.rented_date = rented_date
        
        
    def check_and_create(table_name):
        global  x
        stmt = "SHOW TABLES LIKE %s"%table_name
        cursor_object.execute(stmt)
        result = cursor_object.fetchone()
        statement = statement_books = "CREATE TABLE books(BookID varchar(255),BookTitle varchar(255),author_name varchar(255),publication_company varchar(255),Rented_date varchar(255), Rented_user varchar(255))"
        if result:
            x = 1
            print(f"there is already table named {table_name} exists")
        else:
            x = 0
            print(f"there is no table named {table_name}")
            print("Creating the table......")
            cursor_object.execute(statement)
            print("successfully created the table")
        
    




class Librarian(Books):
    def __init__(self, name, ph_number, librarian_ID, book_object):
        self.name = name 
        self.ph_number = ph_number
        self.librarian_ID = librarian_ID
        self.BookID = book_object.BookID
        self.author_name = book_object.author_name
        self.publication_company = book_object.publication_company
        self.rented_user = book_object.rented_user

    def check_and_create(table_name):
        global  x
        stmt = "SHOW TABLES LIKE %s"%table_name
        cursor_object.execute(stmt)
        result = cursor_object.fetchone()
        statement = statement_librarian = "CREATE TABLE Librarians(Librarian_Id int,Librarian_name varchar(255),phone_number varchar(255))"
        if result:
            x = 1
            print(f"there is already table named {table_name} exists")
        else:
            x = 0
            print(f"there is no table named {table_name}")
            print("Creating the table......")
            cursor_object.execute(statement)
            print("successfully created the table")
            
            
    def add_book(self,book_object):
        #print(book_object.BookID + " "+ book_object.author_name)
        cursor_object.execute( "SHOW TABLES LIKE 'books'")
        result = cursor_object.fetchone()
        if result:
                x = 1
                print(f"there is already table named books exists")
        else:
            x = 0
            print(f"there is no table named books")
            
        sql_stmt = "INSERT INTO books (BookID,BookTitle,author_name, publication_company, Rented_date, Rented_user) VALUES(%s, %s,%s, %s, %s, %s)"
        val = ((book_object.BookID,book_object.Booktitle ,book_object.author_name, book_object.publication_company, book_object.rented_date, book_object.rented_user))
        cursor_object.execute(sql_stmt, val)
        cnx.commit()
        print("it is inserted")
        
    @staticmethod   
    def add_manybooks(books):
        sql_stmt = "INSERT INTO books (BookID, BookTitle,author_name, publication_company, Rented_date, Rented_user) VALUES(%s,%s,%s, %s, %s, %s)"
        cursor_object.executemany(sql_stmt, books)
        cnx.commit()
        print ("Suucessfully Inserted many books")
        
    def add_Librarian(self):
        sql_stmt = "INSERT INTO librarians (Librarian_Id, Librarian_name, phone_number) VALUES(%s, %s, %s)"
        val = ((self.librarian_ID, self.name,self.ph_number))
        cursor_object.execute(sql_stmt, val)
        cnx.commit()
        print("Librarian is suucessfully added")
        
    @staticmethod   
    def update_bookdetails(book_object):
        sql_stmt = "UPDATE books SET author_name = %s, BookTitle = %s,publication_company =%s, Rented_date = %s, Rented_user=%s WHERE BookID = %s"
        data = (book_object.author_name,book_object.Booktitle,book_object.publication_company, book_object.rented_date,book_object.rented_user,book_object.BookID )
        
        cursor_object.execute(sql_stmt, data)
        cnx.commit()
        print(f"Book with BookID {book_object.BookID} is updated")
        
        
    def update_user(mem_obj):
    
        sql_stmt = "UPDATE members SET Member_name = %s, contact_number = %s, Notifications = %s,penalty_fees =%s WHERE MemberID = %s"
        data = (mem_obj.name,mem_obj.dail_number,mem_obj.notifications, mem_obj.penalty_fee,mem_obj.Member_ID )

        cursor_object.execute(sql_stmt, data)
        cnx.commit()
        print(f"Book with MemberID {mem_obj.Member_ID} is updated")
        
    def delete_a_member(mem_object):
        sql_stmt = "DELETE FROM members WHERE MemberID = %s"
        cursor_object.execute(sql_stmt, (mem_object.Member_ID,))
        cnx.commit()
        print(f"Member with MemberID {mem_object.Member_ID} is deleted")
        
        
    def delete_a_book(book_object):
        sql_stmt = "DELETE FROM books WHERE BookID = %s"
        cursor_object.execute(sql_stmt, (book_object.BookID,))
        cnx.commit()
        print(f"Book with BookID {book_object.BookID} is deleted")
    
    def iter_row(cursor, size=10):
        while True:
            rows = cursor.fetchmany(size)
            if not rows:
                break
            for row in rows:
                yield row    
    
    
    def query_avail_books():
        import pandas as pd
        list_avaialble = []
        Librarian.iter_row(cursor_object)
        sql_stmt = " SELECT * FROM books WHERE Rented_user = 'available'"
        cursor_object.execute(sql_stmt)
        for row in Librarian.iter_row(cursor_object, 10):
            #print(row)
            list_avaialble.append(row)
            #print()
        df_avil_books = pd.DataFrame(data=list_avaialble, columns= cols )
        return df_avil_books
    
    def see_all_books():
        import pandas as pd
        #global cols
        List_available = []
        sql_stmt = "select * from books"
        cursor_object.execute(sql_stmt)
        row = cursor_object.fetchone()
        cols = ["BookID", "Titlename", "Title author", "Publisher","Rented Date", "status/Rented User"]
        while row is not None:
                 # In the  while loop block, display the contents of the row and move to the next row until all rows are fetched.
                #print(row)
                row = cursor_object.fetchone()
                List_available.append(row)
                #print()
                
                
        df = pd.DataFrame(data = List_available, columns=cols)
        df = df.iloc[:-1,:]
        return df
                
    
        
        
        
        
                    
        
        
        
        