PATH = "day1/calibration.txt"

def recalibrate():
    output = 0
    first_number = ""
    last_number = ""
    with open(PATH, "r") as file:
        for line in file:
            for i in range(len(line)-1):
                if line[i] in "123456789":
                    first_number = line[i]
                    break
            for i in range(len(line)-1, -1, -1):
                if line[i] in "123456789":
                    last_number = line[i]
                    break
            line_value = int(first_number+last_number)
            print(line_value)
            output += line_value
        print("======")
        print(output)


recalibrate()
