# members class
#
#del Members
class Members:
    penalty_fee = 0
    notifications = "No notifications"
    def __init__(self,Member_ID, name, dail_number,notifications, penalty_fee = 0):
        self.Member_ID = Member_ID
        self.name = name
        self.notifications = notifications
        self.dail_number = dail_number
        self.penalty_fee = penalty_fee
        
        
    def check_and_create(table_name):
        global  x
        stmt = "SHOW TABLES LIKE %s"%table_name
        cursor_object.execute(stmt)
        result = cursor_object.fetchone()
        statement = statement_books = "CREATE TABLE Members(MemberID varchar(255),Member_name varchar(255),contact_number varchar(255),penalty_fees varchar(255),Notifications varchar(255))"
        if result:
            x = 1
            print(f"there is already table named {table_name} exists")
        else:
            x = 0
            print(f"there is no table named {table_name}")
            print("Creating the table......")
            cursor_object.execute(statement)
            print("successfully created the table")
        
        
    def iter_row(cursor, size=10):
        while True:
            rows = cursor.fetchmany(size)
            if not rows:
                break
            for row in rows:
                yield row    
    
    
    def available_books():
        global List_avialble_books
        import pandas as pd
        List_avialble_books = []
        cols = ["BookID", "Titlename", "Title author", "Publisher","Date", "status"]
        Librarian.iter_row(cursor_object)
        sql_stmt = " SELECT * FROM books WHERE Rented_user = 'available'"
        cursor_object.execute(sql_stmt)
        for row in Librarian.iter_row(cursor_object, 10):
            #print(row)
            List_avialble_books.append(row)
            #print()
        df = pd.DataFrame(data = List_avialble_books, columns=cols)
        df = df.iloc[:,:-2]
        print(df)
        
        
    
    def show_me_thebooks():
        import pandas as pd
        List_all = []
        sql_stmt = "select * from books"
        cursor_object.execute(sql_stmt)
        row = cursor_object.fetchone()
        cols = ["BookID", "Titlename", "Title author", "Publisher","Date", "status"]
        while row is not None:
                 # In the  while loop block, display the contents of the row and move to the next row until all rows are fetched.
                #print(row)
                row = cursor_object.fetchone()
                List_all.append(row)
                #print()
                
                
        df = pd.DataFrame(data = List_all, columns=cols)
        df = df.iloc[:-1,:-2]
        return df
        
#     def show_me_thebooks():
#         return Librarian.show_all_books()
#     def available_books():
#         avil_books = Librarian.query_avail_books()
#         return avil_books
    def BookID_from_sql():
        global bookId_sql
        sql_stmt = "SELECT DISTINCT BookID FROM books"
        cursor_object.execute(sql_stmt)
        all_sql_books =  cursor_object.fetchall()
        bookId_sql = list(list(zip(*all_sql_books))[0])
    
    
    def borrow_book(member_object):
        from datetime import datetime, date, timedelta
        global lis2_bookid
        Members.available_books()
        
        lis2_bookid = []
        for x in range(0,len(List_avialble_books)):
            ids = List_avialble_books[x][0]
            lis2_bookid.append(ids)
        while True:
            try:
        
        
                borrow_id = input("Please enter the BookID: ")
                if borrow_id in lis2_bookid:
                    wanted_index = lis2_bookid.index(borrow_id)
                    BookID = List_avialble_books[wanted_index][0] 
                    Booktitle = List_avialble_books[wanted_index][1]
                    author_name = List_avialble_books[wanted_index][2]
                    publication_company= List_avialble_books[wanted_index][3]
                    rented_user = member_object.name                            #List_avialble_books[wanted_index][4]
                    rented_date =  datetime.today().strftime('%d-%m-%Y') #List_avialble_books[wanted_index][5] 
                    book_borr = Books(BookID,Booktitle,author_name,publication_company, rented_user, rented_date )
                    Librarian.update_bookdetails(book_borr)
                    print(f"Book with title {Booktitle} is issued")
                    last_day = datetime.today() + timedelta(days = 20 )
                    print(f"return book by {last_day.day}-{last_day.month}-{last_day.year} to avoid Penalty ")
                    break
                    
            except ValueError:
                
                print("System did not accepted value, check and try again")

            else:
                print("Please check the BookID and try again")
                continue
            
    from datetime import datetime
    def penalty_or_not(borrowed_date,returned_date):
        global calculate_days
        import datetime
        from datetime import datetime
        borrowed_date  # can be fetched from the database
        returned_date # can be fetched from the database
        book_out = datetime.strptime(borrowed_date, '%d-%m-%Y')  #parsing a string into datetime object 
        book_in = datetime.strptime(returned_date, '%d-%m-%Y') 
        calculate_days = (book_in -book_out)
        total_days =  calculate_days.days
        penalty = 0
        if (total_days) <= 20:
            print("Thankyou for returning Book, No penalty")
            return penalty
        elif (total_days) > 20:
            for i in range(20,total_days,5):
                penalty = i+penalty

            print(f"Final penalty for late submission is {penalty}")
            return penalty
        
        
    def return_book():
        global borrowed_date , returned_date
        while True:
            try:
                return_id = input("Please enter the BookID: ")
                Members.BookID_from_sql()

                if return_id in bookId_sql:

                    sql_stmt = f"SELECT * FROM books WHERE BookID = '{return_id}'"
                    cursor_object.execute(sql_stmt)
                    test_row = cursor_object.fetchone()
                    #print(cursor_object.fetchone())
                    test_row = list(test_row)
                    borrowed_date = test_row[4]
                    returned_date = datetime.today().strftime('%d-%m-%Y')
                    test_row[-1] = "available"
                    test_row[-2] = " "
                    book_update = Books(test_row[0], test_row[1],test_row[2],test_row[3],test_row[5], test_row[4])
                    data = (test_row[0], test_row[1],test_row[2],test_row[3],test_row[4],test_row[5])
                    Librarian.update_bookdetails(book_update)
                    Members.penalty_or_not(borrowed_date,returned_date)
                    break

            except ValueError:
                print("Please enter bookID in digits")

            else:
                print("Please check the BookID and try again")
                continue
        