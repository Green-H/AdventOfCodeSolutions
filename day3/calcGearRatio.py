PATH = "input/day3/schematics.txt"
NUMBERS = "0123456789"
MAXROW = 140
MAXCOLUMN = 140

def calcGearRatio():
    with open(PATH,"r")as file:
        data = file.readlines()
        for i in range(MAXROW):
            for j in range(MAXCOLUMN-1):
                current_element = data[i][j]
                if current_element == "*":
                    pass     # se leggi un asterisco devi leggere cosa??


calcGearRatio()