class ChatBook:
    
    def __init__(self):
        self.uname = '' 
        self.pwd = ''
        self.is_logged_in = False
        self.menu()

    
    def menu(self):
        user_input = '''
        Select what you wanna do.
            1. Signup
            2. Signin
            3. Post
            4. Message a friend
            Press any other key to quit. 
        
        --> 
        '''

        x = input(user_input)
        
        if x == '1':
            self.signup()

        elif x == '2':
            self.signin()

        elif x == '3':
            self.post()

        elif x == '4':
            self.message()

        else:
            exit()


    def signup(self):
        uname = input("Enter the uname :- ")
        pwd = input("Enter the pwd :- ")

        self.uname = uname
        self.pwd = pwd

        print("Signup Successful!!")
        self.menu()

    def signin(self):
        if self.uname != '' and self.pwd != '':
            uname = input("Enter the uname to signin :- ")
            pwd = input("Enter the pwd to signin :- ")

            if self.uname == uname and self.pwd == pwd:
                print("Login Successful")
                self.is_logged_in = True
                self.menu()

            else:
                print("Wrong credentials. Please login again")
                self.signin()
            
        else:
            print("You did not signup. Please signup first!")
            self.signup()
    
    def message(self):
        if self.is_logged_in == True:
            fname = input("Enter the friends name :- ")
            msg = input("Enter the message")

            print(f"{msg} sent to {fname}")
            self.menu()

        else:
            print("You havent signed in yet! Please signin....")
            self.signin()


    def post(self):
        if self.is_logged_in == True:
            post = input("Enter the text")

            print(f"Post posted")
            self.menu()

        else:
            print("You havent signed in yet! Please signin....")
            self.signin()


obj = ChatBook()