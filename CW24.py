# https://www.codewars.com/kata/54ff3102c1bad923760001f3

def getCount(inputStr):
    num_vowels = 0
    count = 0
    while count < len(inputStr):
        if inputStr[count] == "a":
                num_vowels += 1
                count += 1
                continue
        elif inputStr[count] == "e":
                num_vowels += 1
                count += 1
                continue
        elif inputStr[count] == "i":
                num_vowels += 1
                count += 1
                continue
        elif inputStr[count] == "o":
                num_vowels += 1
                count += 1
                continue
        elif inputStr[count] == "u":
                num_vowels += 1
                count += 1
                continue
        else: 
                count += 1
                continue
    return num_vowels