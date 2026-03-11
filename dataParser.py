import sqlite3
from sqlite3 import Error










path = "database.db"
connection = None
try:
    connection = sqlite3.connect(path)
    print("Connected to Database")
except Error as e:
    print("The error " + e + " occured")

cursor = connection.cursor()



def userSearch(username):
    sql = "SELECT * FROM players WHERE username = ?"
    nameTuple = (username,)
    cursor.execute(sql, nameTuple)
    print(cursor.fetchall())




def Search():
    print("What do you want to search for?")
    print("1: user search")
    print("2: pokemon usage rate")
    print("3: pokemon top usage list")
    inputNum = input("Your Decision: ")


    match inputNum:
        case "1":
            name = input("Please enter a username: ")
            userSearch(name)
        case "2":
            print("You entered 2")
        case "3":
            print("You entered 3")
        case _:
            print("Please input a valid number")







Search()
