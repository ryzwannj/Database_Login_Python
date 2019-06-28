import sqlite3

def register():
    name = str(input("What's your name? "))
    username = input("Enter a username: ")
    password = input("Enter a password: ")
    verfpassword = input("Enter your password again: ")

    while password != verfpassword:
        print("You must to enter the SAME password!")
        register()
        break
    
    print("Your account was create succefuly..")

def login():
    username1 = input("username: ")
    password1 = input("password: ")

menu = str(input("Login(l) or Register(r): "))

if menu == "l":
    login()

else:
    register()