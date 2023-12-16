# 141 caratteri per riga
PATH = "input/day3/schematics.txt"
SYMBOLS = "=&+-@*%#/$"
NUMBERS = "0123456789"
MAXROW = 140
MAXCOLUMN = 140
def sumEngineParts():
    with open(PATH,"r") as file:
        data = file.readlines()
        array_somma=[]
        num = ""
        tot = 0
        number_found = False
        number_finished = False
        for i in range(MAXROW):
            for j in range(MAXCOLUMN):
                current_element = data[i][j]
                print("leggo: ",current_element)

                if current_element in NUMBERS:
                    number_finished = False
                    num += current_element
                    number_found = True
                    if j == MAXCOLUMN-1:
                        number_finished=True
                if current_element not in NUMBERS and number_found:
                    number_finished = True
                if number_found and number_finished: # non è un numero ma ne hai appena finito uno? 
                    print("Ho letto",current_element,"e l'ultimo numero e",num)
                    number_found = False
                    print("controllo i bordi:")
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
                        right_side = "A" # se metto "" non funziona ma con A si??
                    else:
                        right_side = data[i][j]
                    if j == 0:
                        left_side = ""
                    else:
                        left_side = data[i][j-len(num)-1]
                    print("[i,j]=",i,j,"num=",num,"\n","Check left: ",left_side,"Check right: ",right_side,"Check up: ",top_row,"Check down: ",bot_row)
                    # se è adiacete ad un simbolo il numero è valido e lo aggiungo al totale, resettandolo
                    if left_side in SYMBOLS or right_side in SYMBOLS or any(char in top_row for char in SYMBOLS) or any(char in bot_row for char in SYMBOLS):
                        print("il totale finora e",tot)
                        array_somma.append(int(num))
                        tot += int(num)
                        print("============> numero rilevato dopo  un simbolo:",num)
                        if right_side in SYMBOLS:
                            print("simbolo a destra")
                        if left_side in SYMBOLS:
                            print("simbolo a sinistra")
                        if any(char in top_row for char in SYMBOLS):
                            print("simbolo sopra")
                        if any(char in bot_row for char in SYMBOLS):
                            print("simbolo sotto")
                        print("il totale provvisorio dopo aver aggiunto",num,"equivale a",tot)
                        
                    else:
                        print("numero non valido")
                    num = ""
        print("===================")            
        print("il totale e",tot)
        print("il totale array e",sum(array_somma))
        print(array_somma)
        print("===================")
        

sumEngineParts()