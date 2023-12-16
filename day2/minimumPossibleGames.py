PATH = "input/day2/games.txt"
def minimumPossibleGames():
    tot = 0
    with open(PATH,"r")as file:
        for line in file:
            d = {"red":0,"green":0,"blue":0}
            line=line.strip()
            games = line.split(": ")[1]
            extracted = games.split("; ")
            for partita in extracted:
                partita=partita.replace(", ",",")
                singole_estrazioni = partita.split(",")
                for singola in singole_estrazioni:
                    singola = singola.split(" ")
                    if int(singola[0])>d[singola[1]]:
                        d[singola[1]]=int(singola[0])
            id = d["red"]*d["green"]*d["blue"]
            tot += id
        print(tot)





minimumPossibleGames()
