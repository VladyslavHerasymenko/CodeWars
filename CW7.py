# https://www.codewars.com/kata/57126304cdbf63c6770012bd  

def isDigit(string):
    try:
        float(string)
    except:
        return False
    return True