# https://www.codewars.com/kata/563b74ddd19a3ad462000054 

    def stringy(size):
    string = ""
    count = 0
    while count != size:
        if count % 2 == 0:
            string = string + "1"
            count += 1   
            continue
        else:
            string = string + "0"
            count += 1
            continue
    return string