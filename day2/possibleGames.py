PATH = "day2/games.txt"

def sumPossibleGames():

    tot = 0
    with open(PATH,"r") as file:
        for line in file:
            line = line.strip()
            
            id = int(line.split(":")[0].split(" ")[1])
            games = line.split(":")[1]
            games=games.replace(";",",")
            extracions = games.split(",")     # [" 2 red",...]
            possible = True
            for i in extracions:
                i = i[1:]                     # "2 red"
                tester = i.split(" ")    # ["2","red"]
                if int(tester[0])>14:
                    possible = False
                elif int(tester[0])>12 and tester[1]=="red":
                    possible = False
                elif int(tester[0])>13 and tester [1] == "green":
                    possible = False
            if possible:
                tot+=id
            

                        
    print(tot)


sumPossibleGames()