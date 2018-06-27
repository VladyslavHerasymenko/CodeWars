# https://www.codewars.com/kata/55cbd4ba903825f7970000f5

def get_grade(s1, s2, s3):
    arr = sum([s1, s2, s3]) / 3
    if arr >= 90:
        return "A"
    elif arr >= 80:
        return "B"
    elif arr >= 70:
        return "C"
    elif arr >= 60:
        return "D"
    else:
        return "F"

