import requests

import Util
import sqlite3
from sqlite3 import Error

URL = input("Please input a Pokemon Showdown replay link: ")


def connection_create(path):
    connection = None
    try:
        connection = sqlite3.connect(path)
        print("Connected to Database")
    except Error as e:
        print("The error " + e + " occured")
    
    return connection


def matchFind(URL):
    index = URL.find(".com") + 5
    matchID = URL[index:]

    log = requests.get(URL + ".log").text

    logList = log.split("\n")

    #initialize both player variables and variables to store ELO
    p1, p2 = "Null", "Null"
    p1Elo, p2Elo = -1, -1

    # PARSE ARRAY, FIND FIRST ENTRY INCLUDING "|player|p1" TO FIND PLAYER NAME AND ELO
    p1Found = False
    p2Found = False

    for i in logList:
        if not p1Found and i.find("|player|p1") != -1:
            print(i)
            try:
                p1Elo = int(i[-5:])
            except:
                try:
                    p1Elo = int(i[-4:])
                except:
                    try:
                        p1Elo = int(i[-3:])
                    except:
                        print(i + " DID NOT FIND ELO")
                        p1Elo = None



            p1 = Util.PCutAfter(i, 3)
            p1 = Util.PCutBefore(p1)
            p1Found = True

        elif not p2Found and i.find("|player|p2") != -1:
            print(i)
            try:
                p2Elo = int(i[-5:])
            except:
                try:
                    p2Elo = int(i[-4:])
                except:
                    try:
                        p2Elo = int(i[-3:])
                    except:
                        print(i + " DID NOT FIND ELO")
                        p2Elo = None
            p2 = Util.PCutAfter(i, 3)
            p2 = Util.PCutBefore(p2)
            p2Found = True
        
        elif p1Found and p2Found:
            break

    pokeNames1 = []
    pokeNames2 = []


    #Finds pokemon and assigns them to the correct player
    for i in logList:
        if(i[0:8] == "|poke|p1"):
            pokeNames1.append(i[9:])


        if(i[0:8] == "|poke|p2"):
            pokeNames2.append(i[9:])
    
        if(i[0:5] == "|win|"):
            winnerName = i[5:]
            print("Winner Name = " + winnerName)
        if(i[0:6] == "|tier|"):
            tier = i[6:]
            print("Current tier: " + tier)


    #Gets rid of pokemon genders and converts pokeName1/2 to only their names
    print(pokeNames2)
    for i in range(len(pokeNames2)):

        seperator = pokeNames2[i].find(',')
        if seperator == -1:
            seperator = pokeNames2[i].find('|')

        if seperator != -1:
            pokeNames2[i] = pokeNames2[i][0:seperator]
    print(pokeNames2) 
    print(pokeNames1)
    for i in range(len(pokeNames1)):
        seperator = pokeNames1[i].find(',')
        if seperator == -1:
            seperator = pokeNames1[i].find('|')

        if seperator != -1:
            pokeNames1[i] = pokeNames1[i][0:seperator]
    print(pokeNames1)  








##----------------##
##SQLITE3 DATABASE##
##----------------##




    connection = connection_create("database.db")
    cursor = connection.cursor()




    try:
        cursor.execute("""
                   CREATE TABLE IF NOT EXISTS players(
                   username TEXT PRIMARY KEY,
                   wins INTEGER NOT NULL,
                   loses INTEGER NOT NULL,
                   games_played INTEGER NOT NULL,
                   current_elo INTEGER
                   )
                   
                   """)
        connection.commit()
        cursor.execute("""
                   CREATE TABLE IF NOT EXISTS games(
                   player1_name TEXT NOT NULL,
                   player2_name TEXT NOT NULL,
                   player1_team TEXT NOT NULL,
                   player2_team TEXT NOT NULL,
                   player1_elo INTEGER,
                   player2_elo INTEGER,
                   winner_name TEXT NOT NULL,
                   tier TEXT NOT NULL,
                   match_id TEXT PRIMARY KEY
                   )
                   """)
        connection.commit()

    except Error as e:
        print("The error " + e + " occured")
        print("Database Creation")




    #TRY-EXCEPT tries to add the current match into the games table
    try:
        pokeNames1 = '|'.join(pokeNames1)
        pokeNames2 = '|'.join(pokeNames2)
    
        Sql = ''' INSERT INTO games(player1_name, player2_name, player1_team, player2_team, player1_elo, player2_elo, winner_name, tier, match_id) 
    VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?) '''
        cursor.execute(Sql, (p1, p2, pokeNames1, pokeNames2, p1Elo, p2Elo, winnerName, tier, matchID))
    
        connection.commit()

        print("INSERT executed")
    except Error as e:
        if(str(e) == "UNIQUE constraint failed: games.match_id"):
            print(matchID + ": MATCH ALREADY IN THE DATABASE")
        else: 
            print(e)
    #TRY-EXCEPT tries to add the current match into the games table



    #TRY-EXCEPT Tries to add the the players to the database if they don't already exist. Also updates the win/loss counter
    try:    
        Sql = '''SELECT username FROM players'''
        cursor.execute(Sql)

        NeedToAddP1 = True
        NeedToAddP2 = True
        for i in cursor.fetchall():
            if i == p1 or i == p2:
                if i == winnerName and i == p1:
                
                    cursor.execute("UPDATE players SET wins = wins + 1, games_played = games_played + 1, current_elo = ? WHERE username = ?", p1Elo, i)
                    NeedtoAddP1 = False
                elif i == winnerName and i == p2:
                    cursor.execute("UPDATE players SET wins = wins + 1, games_played = games_played + 1, current_elo = ? WHERE username = ?", p2Elo, i)
                    NeedToAddP2 = False
                elif i == p1: #IF i == p1, but not "i == p1 and i = winnerName" then p1 is the loser
                    cursor.execute("UPDATE players SET loses = loses + 1, games_played = games_played + 1, current_elo = ? WHERE username = ?", p1Elo, i)
                    NeedtoAddP1 = False
                elif i == p2: #IF i == p2, but not "i == p2 and i = winnerName" then p2 is the loser
                    cursor.execute("UPDATE players SET loses = loses + 1, games_played = games_played + 1, current_elo = ? WHERE username = ?", p2Elo, i)
                    NeedToAddP2 = False
                else:
                    print(i + " is not a current player in the match")
            
        if NeedToAddP1 and p1 == winnerName:
            cursor.execute("INSERT INTO players(username, wins, loses, games_played, current_elo) VALUES(?,?,?,?,?)", (p1, 1, 0, 1, p1Elo))
        elif NeedToAddP1:
            cursor.execute("INSERT INTO players(username, wins, loses, games_played, current_elo) VALUES(?,?,?,?,?)", (p1, 0, 1, 1, p1Elo))


        if NeedToAddP2 and p2 == winnerName:
            cursor.execute("INSERT INTO players(username, wins, loses, games_played, current_elo) VALUES(?,?,?,?,?)", (p2, 1, 0, 1, p2Elo))
        elif NeedToAddP2:
            cursor.execute("INSERT INTO players(username, wins, loses, games_played, current_elo) VALUES(?,?,?,?,?)", (p2, 0, 1, 1, p2Elo))


        connection.commit()

    except Error as e:
        print(e)
