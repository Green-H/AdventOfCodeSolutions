# 141 caratteri per riga
PATH = "day3/schematics.txt"
SYMBOLS = "=&+-@*%#/$"
NUMBERS = "0123456789"
MAXROW = 140
MAXCOLUMN = 140
def sumEngineParts():
    with open(PATH,"r") as file:
        num = ""
        tot = 0
        number_found = False
        data = file.readlines()
        for i in range(MAXROW):
            for j in range(MAXCOLUMN):
                print("provo a scegliere l'elemento in posizione:",i,j)
                current_element = data[i][j]
                print("leggo: ",current_element)
                if current_element in NUMBERS: # è un numero? se si mettilo in num
                    num+=current_element
                    number_found = True
                elif number_found and current_element not in NUMBERS: # non è un numero ma ne hai appena finito uno? 
                    print("Ho letto",current_element,"e l'ultimo numero e",num)
                    number_found = False
                    # Awkward checks ?
                    if i == 0:
                        top_row = ""
                    else:
                        top_row = data[i-1][max(0,j-len(num)-1):j+1]
                    if i == MAXROW-1:
                        bot_row=""
                    else:
                        bot_row = data[i+1][max(0,j-len(num)-1):j+1]
                    if j == MAXCOLUMN-1 and data[i][j] in NUMBERS:
                        right_side = ""
                    else:
                        right_side = data[i][j]
                    if j == 0:
                        left_side = ""
                    else:
                        left_side = data[i][j-len(num)-1]
                    print("[i,j]=",i,j,"num=",num,"\n","Check left: ",left_side,"Check right: ",right_side,"Check up: ",top_row,"Check down: ",bot_row)
                    # se è adiacete ad un simbolo il numero è valido e lo aggiungo al totale, resettandolo
                    if right_side in SYMBOLS or left_side in SYMBOLS or any(char in top_row for char in SYMBOLS) or any(char in bot_row for char in SYMBOLS):
                        tot += int(num)
                        print("============> numero rilevato dopo  un simbolo:",num)
                    else:
                        print("numero non valido")
                    num = ""
        print("===================")            
        print("il totale e",tot)
        print("===================")
        

sumEngineParts()