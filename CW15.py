# https://www.codewars.com/kata/54edbc7200b811e956000556

def count_sheeps(arrayOfSheeps):
    return sum(1 for n in arrayOfSheeps if n == True)