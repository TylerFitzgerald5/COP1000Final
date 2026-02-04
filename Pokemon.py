import requests
import Player as ply
import Util

#URL = input("Please input a Pokemon Showdown replay link: ")
URL = "https://replay.pokemonshowdown.com/gen9ou-2526545993"
log = requests.get(URL + ".log").text

logList = log.split("\n")

#initialize both player variables and variables to store ELO
p1, p2 = "Null", "Null"
p1Elo, p2Elo = -1, -1

# PARSE ARRAY, FIND FIRST ENTRY INCLUDING "|player|p1" TO FIND PLAYER NAME AND ELO

for i in logList:
    if i.find("|player|p1") != -1:
        p1 = Util.PCutAfter(i, 3)
        p1 = Util.PCutBefore(p1)
        p1Elo = int(i[-4:])
    elif i.find("|player|p2") != -1:
        p2 = Util.PCutAfter(i, 3)
        p2 = Util.PCutBefore(p2)
        p2Elo = int(i[-4:])

pokeNames1 = []
pokeNames2 = []


#Finds pokemon and assigns them to the correct player
for i in logList:
    if(i[0:8] == "|poke|p1"):
        pokeNames1.append(i[9:])


    if(i[0:8] == "|poke|p2"):
        pokeNames2.append(i[9:])


#Gets rid of pokemon genders and converts pokeName1/2 to only their names
for i in range(len(pokeNames2)):
    seperator = pokeNames2[i].find(',')
    if seperator == -1:
        seperator = pokeNames2[i].find('|')
    pokeNames2[i] = pokeNames2[i][0:seperator]

for i in range(len(pokeNames1)):
    seperator = pokeNames1[i].find(',')
    if seperator == -1:
        seperator = pokeNames1[i].find('|')
    pokeNames1[i] = pokeNames1[i][0:seperator]

player1 = ply.Player(p1, pokeNames1, p1Elo)
player2 = ply.Player(p2, pokeNames2, p2Elo)
print(player1)
print("\n")
print(player2)

