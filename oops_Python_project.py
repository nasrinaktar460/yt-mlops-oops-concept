class Chapbook:
     def __init__(self):
        self.username = ''
        self.password = '' 
        self. loggedin= False
        self.menu()
        
        


        def menu(self):
            user_input = input( """"Welcome to the Chatbook  How would you like to proceed? 
                                1. press 1 to signup
                                2. press 2 to signin
                                3. press 3 to write a post
                                4. press 4 to message to friend
                                5. press any key to exit""")
            if user_input == "1":
                self.signup()
            elif user_input == "2":
                self.signin()
            elif user_input ==  "3":
                 self.my_post()
            elif user_input == "4":
                self.sendmsg()
            else:
                exit()



        def signup(self):
                email = input("enter your email here - ")
                pwd = input("setup your password here - ")
                self.username = email
                self.password = pwd
                print("you have signed up succesfull !!") 
                print("\n")
                self.menu()



        def signin(self):
            if self.username== '' and self.password== '':
                 print("Pleace signup first by pressing 1 in the menu")
            else:
                 unmae = input("enter your emain or username here - ")
                 pwd = input("Enter your password here - ")
            if self.username==uname and self.password==pwd:
                 print("you have signed in suncessfully !!")
                 self.loggedin = True
            else:
                 print("Please input correct credentials..")
               
                 self.menu()
                   




        def my_post(self):
             if self.loggedin==True:
                txt = input("Enter your message here -> ")
                print(f"Following content has been posted -> {text}")
             else:
                  print("you need to signin first to post something.....")
                  print("\n")
                  self.menu()


        
        def sendmsg(self):
            if self.loggedin==True:
                 txt = input("Enter your massage here -> ")
                 frnd = input("Whomw to send the msg -> ")
                 print(f"your masage has been sanded to {frnd}")
            else:
                 print("your need to signin first to post something......")
                 print("\n")
                 self.menu() 



user1  = Chapbook()



