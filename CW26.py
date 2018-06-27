# https://www.codewars.com/kata/558fc85d8fd1938afb000014

numbers = [1, 2, 3, 4, 5]

def sum_two_smallest_numbers(numbers):
    numbers.sort()
    sum = numbers[0] + numbers[1]
    return sum