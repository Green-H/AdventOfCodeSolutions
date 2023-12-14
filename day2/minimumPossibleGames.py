PATH = "day2/test.txt"
def minimumPossibleGames():
    with open(PATH,"r")as file:
        for line in file:
            d = {"red":0,"green":0,"blue":0}
            line=line.strip()
            games = line.split(": ")[1]
            extracted = games.split(";")
            for partita in extracted:
                partita=partita.replace(", ",",")
                singole_estrazioni = partita.split(",")
                for singola in singole_estrazioni:
                    singola.split(" ")
                d[singole_estrazioni[1]]=int(singole_estrazioni[0])
                print(d)





minimumPossibleGames()
