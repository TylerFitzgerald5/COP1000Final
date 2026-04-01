import sqlite3
from sqlite3 import Error
import json









path = "database.db"
connection = None
try:
    connection = sqlite3.connect(path)

except Error as e:
    print("The error " + e + " occured")

cursor = connection.cursor()

tierSQL = "SELECT DISTINCT tier FROM games"
cursor.execute(tierSQL)
print("\n\nThe tiers present in the database are: ")
for i in cursor:
    print(i[0]) #Cursor is a list of single element tuples
print("\n\n")

cursor.close()



def userSearch(username):
    cursor  = connection.cursor()
    sql = "SELECT * FROM players WHERE username = ?"
    nameTuple = (username,)
    cursor.execute(sql, nameTuple)
    user = cursor.fetchone()
    if user == None:
        print("\n\n\n\n")
        print("That user does not exist in the database. Please ensure name is correct and capitalized correctly.")
    else:
        print("\n\n\n\n")
        print("User: " + user[0])
        print("wins: "+ str(user[1]))
        print("loses: " + str(user[2]))
        print("Games Played: " + str(user[3]))
        print("Current ELO: " + str(user[4]))
    cursor.close()




def usageRate(pokemon, tier):
    cursor = connection.cursor()
    sql = "SELECT player1_team, player2_team FROM games"
    cursor.execute(sql)

    SQLlist = cursor.fetchall()

    pokeUsed = 0
    pokeTotal = 0

    for poketeam in SQLlist:

        pokelist = poketeam[0].split("|")
        pokelist2 = poketeam[1].split("|")

        pokelist.extend(pokelist2)
        
        print(pokelist)
        for i in pokelist:
            if pokemon.lower() == i.lower():
                pokeUsed += 1
            pokeTotal += 1
        print(pokeTotal)
        print(pokeUsed)
    cursor.close()

def topUsageList(tier):
    cursor = connection.cursor()

    SQL = "SELECT player1_team, player2_team FROM games WHERE tier = ?"
    cursor.execute(SQL, (tier, ))
    ##################Incorrect number of bindings supplied. The current statement uses 1, and there are 10 supplied.#########################
    ###############ERROR###########ERROR################ERROR###########ERROR#########ERROR###############
    SQLlist = cursor.fetchall()
    pokeUsage = {} 
    for poketeam in SQLlist:

        pokelist = poketeam[0].split("|")
        pokelist2 = poketeam[1].split("|")

        pokelist.extend(pokelist2)
        for i in pokelist:
            if i in pokeUsage.keys():
                pokeUsage[i] += 1
            else:
                pokeUsage[i] = 1
        sortedPokes = sorted(pokeUsage, key= lambda d: pokeUsage[d], reverse=True)
        for i in sortedPokes:
            print(i + ": " + str(pokeUsage[i]))
    cursor.close()
        



################BUG################
#When printing pokemon without genders, the last letter gets cut off? Mew != Me
###################################


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
            pokemon = input("Please enter a pokemon name: ")
            tier = input("Please input a tier: ")
            usageRate(pokemon, tier)

        case "3":
            print("You entered 3")
            tier = input("Please enter a tier: ")
            topUsageList(tier)

        case _:
            print("Please input a valid number")







Search()
