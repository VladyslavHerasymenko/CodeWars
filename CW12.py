# https://www.codewars.com/kata/565f5825379664a26b00007c

def get_size(w,h,d):
    arr = []
    arr.append(2 * (w * h + h * d + w * d))
    arr.append(w * h * d)
    return arr