import sqlite3

conn = sqlite3.connect('users.db')
cur = conn.cursor()

cur.execute('''CREATE TABLE  IF NOT EXISTS Users
    (id INTEGER PRIMARY KEY, Name TEXT, Username CHAR, Email CHAR, Password CHAR)''')

tables = cur.fetchall()

def AddEntry(Name,Username,Email,Password):
    cur.execute('''INSERT INTO Users (Name,Username,Email,Password)
    VALUES (?,?,?,?)''',(Name,Username,Email,Password))

def register():
    name = str(input("What's your name? "))
    username = input("Enter a username: ")
    email = input("Enter your email: ")
    password = input("Enter a password: ")
    verfpassword = input("Enter your password again: ")

    while password != verfpassword:
        print("You must to enter the SAME password!")
        register()
        break
    
    print("Your account was create succefuly..")
    AddEntry(name, username, email, password)
    conn.commit()

def login():
    username1 = input("username: ")
    email1 = input("email: ")
    password1 = input("password: ") 

menu = str(input("Login(l) or Register(r): "))

if menu == "l":
    login()

else:
    register()
