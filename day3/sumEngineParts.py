# 141 caratteri per riga
PATH = "day3/test.txt"
SYMBOLS = "=&+-@*%#/$"
NUMBERS = "0123456789"
def sumEngineParts():
    with open(PATH,"r") as file:
        num = ""
        tot = 0
        number_found = False
        valid_number = False
        data = file.readlines()
        for i in range(10):
            for j in range(10):
                current_element = data[i][j]
                if current_element in NUMBERS:
                    num+=current_element
                    number_found = True
                if number_found and current_element not in NUMBERS:
                    top_row = data[i-1][j-len(num)-1:j]
                    bot_row = data[i+1][j-len(num)-1:j]
                    if data[i][j] in SYMBOLS or data[i][j-len(num)] in SYMBOLS or any(char in top_row for char in SYMBOLS) or any(char in bot_row for char in SYMBOLS):
                            valid_number = True
                            tot += int(num)
                    
        print(tot)
        

sumEngineParts()