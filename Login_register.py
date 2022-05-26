test_dict = {}
# Register button 

from random import randint, randrange
#test_dict = {}
##secret_dict = {}
def registration():
    global password_1, Member_obj 
    from random import randint, randrange
    
    name = input("Enter your Name: ")
    
    phone_number = input("Enter your phone_number: ")
    while True:
        password_1 = input("create your password for your account: ")
        password_2 = input("Re-enter your password for your account confirmation: ")
    
        if password_1==password_2:
            user_id = name+"_"+str(randint(100000, 999999)) ######################
            print("password successfully created")
            break
        else:
            print("passwords donot match, Try again!")
            continue
    print("your User_id is:",user_id)
    Member_obj = Members(user_id, name,phone_number,notifications =" ",penalty_fee = 0 ) 
    sql_stmt = "INSERT INTO Members (MemberID,Member_name,contact_number, penalty_fees, Notifications) VALUES(%s, %s,%s, %s, %s)" 
    data =  ((Member_obj.Member_ID,Member_obj.name ,Member_obj.dail_number, Member_obj.penalty_fee, Member_obj.notifications))
    cursor_object.execute(sql_stmt, data)
    cnx.commit()
    temp = {}
    temp[user_id] = password_1
    test_dict.update(temp)
    test_dict
    with open("customers_file.json",mode = "w+") as fout:
        json.dump(test_dict,fout , indent=4)
    return user_id





#registration()

import os
import json
from datetime import datetime,timedelta 

os.chdir(r"E:\MY_PYTHON_SCRIPTS\MY_LIBRARY_MANAGMENT") # working directory

def login():
    global member_obj
    import os
    import json
    from datetime import datetime,timedelta
    os.chdir(r"E:\MY_PYTHON_SCRIPTS\MY_LIBRARY_MANAGMENT")
    acc_user_name = input("Enter your UserID: ")
    acc_password = input("Enter the Password: ")
    with open("customers_file.json",mode = "r") as fout_1:
        data_dict = json.load(fout_1)
        list_keys =  []
        list_values = []
    for k,v in data_dict.items():
        list_keys.append(k)
        list_values.append(v)
    if ((acc_user_name in list_keys) and (acc_password == data_dict[acc_user_name])):
        print("Successfully logged in")
        print("Welcome to use the systems")
        # retrieve the record from the database and use the options
        sql_stmt = f"SELECT * FROM Members WHERE MemberID = '{acc_user_name}'" 
        cursor_object.execute(sql_stmt)
        test_row = cursor_object.fetchone() 
        member_obj = Members(test_row[0],test_row[1], test_row[2], test_row[4])
        menu='''
            1. Rent a book
            2. Return a book
            3. Logout
    
    
            '''
        choice = input(menu)
        i = 3
        if i > 1:
        #while choice!=4:
            #choice=view.transactions_options()
            if choice=='1':
                Members.borrow_book(member_obj)
                
            elif choice=='2':
                Members.return_book()
                

            elif choice=='3':
                print("Out of application")
                
                
                


            else:
                print("Incorrect choices")
                members_operations()
                
        
    elif (acc_user_name not in list_keys):
        print("Username is not registered, Please register")
        registration()
        
    elif ((acc_user_name in list_keys) and (acc_password != data_dict[acc_user_name])):
        print("Password is not correct, please Try again!")
        login()
        
        
        

        
        
        
    
        
        
     