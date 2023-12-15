# 141 caratteri per riga
PATH = "day3/test.txt"
SYMBOLS = "=&+-@*%#/$"
NUMBERS = "0123456789"
MAXROW = 10
MAXCOLUMN = 10
def sumEngineParts():
    with open(PATH,"r") as file:
        num = ""
        tot = 0
        number_found = False
        data = file.readlines()
        for i in range(MAXROW):
            for j in range(MAXCOLUMN):
                current_element = data[i][j]
                print("leggo: ",current_element)
                if current_element in NUMBERS: # è un numero? se si mettilo in num
                    num+=current_element
                    number_found = True
                elif number_found and current_element not in NUMBERS: # non è un numero ma ne hai appena finito uno? 
                    print("Ho letto",current_element,"e l'ultimo numero e",num)
                    number_found = False
                    if i == 0:
                        top_row = ""
                    else:
                        top_row = data[i-1][max(0,j-len(num)-1):j+1]
                    if i == MAXROW-1:
                        bot_row=""
                    else:
                        bot_row = data[i+1][max(0,j-len(num)-1):j+1]

                    print("[i,j]=",i,j,"devo controllare :",top_row,"e",bot_row)
                    # se è adiacete ad un simbolo il numero è valido e lo aggiungo al totale, resettandolo
                    if data[i][j] in SYMBOLS or data[i][j-len(num)-1] in SYMBOLS or any(char in top_row for char in SYMBOLS) or any(char in bot_row for char in SYMBOLS):
                        #tot += int(num)
                        print("numero rilevato dopo  un simbolo:",num)
                    else:
                        print("numero non valido")
                    num = ""
        print("===========")            
        print("il totale e",tot)
        

sumEngineParts()