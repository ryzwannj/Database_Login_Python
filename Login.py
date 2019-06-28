import sqlite3

conn = sqlite3.connect('users.db')
cur = conn.cursor()

cur.execute('''CREATE TABLE  IF NOT EXISTS Users
    (id INTEGER PRIMARY KEY, Name TEXT, Username CHAR, Password CHAR)''')

def AddEntry(Name,Username,Password):
    cur.execute('''INSERT INTO Users (Name,Username,Password)
    VALUES (?,?,?)''',(Name,Username,Password))

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
    AddEntry(name, username, password)
    conn.commit()

def login():
    username1 = input("username: ")
    password1 = input("password: ")

menu = str(input("Login(l) or Register(r): "))

if menu == "l":
    login()

else:
    register()


