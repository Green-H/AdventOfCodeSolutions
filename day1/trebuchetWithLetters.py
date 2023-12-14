# -*- coding: utf-8 -*-
"""
Created on Thu Dec 14 10:50:14 2023

@author: Luca
"""

PATH = "day1\calibration.txt"
d = {'one': "1",
     'two': "2",
     'three': "3",
     'four': "4",
     'five': "5",
     'six': "6",
     'seven': "7",
     'eight': "8",
     'nine': "9"
     }


def recalibrate():
    output = 0
    k = 1

    with open(PATH, "r") as file:
        for line in file:
            first_number = ""
            last_number = ""
            first_found = False
            print("---------------------")
            print(k)
            k += 1
            for i in range(len(line)-1):
                if line[i] in "123456789":
                    if not first_found:
                        first_number = line[i]
                        first_found = True
                        print("Il primo numero è:", first_number)
                    else:
                        last_number = line[i]
                        print("Il secondo numero è:", last_number)

                else:
                    for j in range(i, i+5):
                        if line[i:j+1] in d:
                            if not first_found:
                                first_number = d[line[i:j+1]]
                                first_found = True
                                print("Il primo numero è:", first_number)
                                break
                            else:
                                last_number = d[line[i:j+1]]
                                print("Il secondo numero è:", last_number)
                                break
            if last_number == "":
                last_number = first_number
            stringalinea = first_number + last_number
            line_value = int(stringalinea)
            print("la linea vale: ", line_value)
            output += line_value
        print("======")
        print(output)


recalibrate()
