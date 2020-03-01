from firebase import Firebase

config = {
   "apiKey": "AIzaSyD14k9cwnVbCt7bNcFcB8S9E3LsHs-hhSI",
   "authDomain": "agendaai-e8d58.firebaseapp.com",
   "databaseURL": "https://agendaai-e8d58.firebaseio.com",
   "storageBucket": "agendaai-e8d58.appspot.com",
}

firebase = Firebase(config)
auth = firebase.auth()

def register():
    name = str(input("What's your name? "))
    username = input("Enter a username: ")
    email = input("Enter your email: ")
    password = input("Enter your password: ")
    verfpassword = input("Enter your password again: ")
    
    while password != verfpassword:
        print("You must to enter the SAME password!")
        register()
        break
        
    auth.create_user_with_email_and_password(email, password)
    print("Your account was create succefuly...")
    menu()


def login():
    username1 = input("username: ")
    password1 = ("password: ")

def menu():
    response = str(input("Login(l) or Register(r): "))

    if response == "l":
        login()

    elif response == "r":
        register()

    else:
        print("Please enter either Login(l) or Register(r): ")
        menu()
menu()


