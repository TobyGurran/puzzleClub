#Project Euler Problem 4
#https://projecteuler.net/problem=4

#A palindromic number reads the same both ways.
#The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.
#Find the largest palindrome made from the product of two 3-digit numbers.

import numpy

all_three_digit_numbers = list(numpy.arange(1,1000,1))

def create_all_possible_products(list_of_numbers):
    products = list()
    for i in range(len(list_of_numbers)):
        for j in range(len(list_of_numbers)):
            products.append(list_of_numbers[i] * list_of_numbers[j])
    return(products)

all_products = create_all_possible_products(list_of_numbers=all_three_digit_numbers)
#Make unique by converting to a set (loses ordering)
all_products = set(all_products)
#Convert back to list and sort
all_products = list(all_products)
all_products.sort(reverse=True)


def is_number_palindromic(input_number):
    #Make input number a string, then when you do list comprehension it will take each character. And make each an integer.
    number_list = [i for i in str(input_number)]
    number_list_reversed=list(reversed(number_list))
    #Because each index is now a string, they can be joined with the join() method
    number_string_reversed="".join(number_list_reversed)
    if number_string_reversed == str(input_number):
        return True
    else:
        return False

for i in range(len(all_products)):
    if is_number_palindromic(input_number=all_products[i]):
        print(all_products[i])
        break
