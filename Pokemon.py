import requests
import Player

#URL = input("Please input a Pokemon Showdown replay link: ")
URL = "https://replay.pokemonshowdown.com/gen9ou-2526545993"
log = requests.get(URL + ".log").text

logList = log.split("\n")

p1 = logList[0][4:]
p1Elo = logList[0][-4:]
p2 = logList[1][4:]
p2Elo = logList[1][-4:]

# PARSE ARRAY, FIND FIRST ENTRY INCLUDING "|player|p1" TO FIND PLAYER NAME AND ELO

#for i in logList:
 #   if i 
#p1 = logList.index("|player|p1")
#p2 = logList.index("|player|p2")

pokeNames1 = []
pokeNames2 = []



for i in logList:
    if(i[0:8] == "|poke|p1"):
        pokeNames1.append(i[9:])


    if(i[0:8] == "|poke|p2"):
        pokeNames2.append(i[9:])

#Gets rid of pokemon genders and converts pokeName2 to only their names
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

#player1 = Player(p1, )
print(p1)
print("\n")
print(p2)

