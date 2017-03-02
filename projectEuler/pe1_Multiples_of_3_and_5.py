#Project Euler Problem 1
#https://projecteuler.net/problem=1

# If we list all the natural numbers below 10
# that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.
# Find the sum of all the multiples of 3 or 5 below 1000.

max_range = 1000

list_of_numbers_1_to_1000 = list(range(1,max_range+1,1))

#1. via list comprehension
divisible_by_3_and_5 = [i for i in list_of_numbers_1_to_1000 if (i%3==0 or i%5==0)]
print(divisible_by_3_and_5)

#2. via list comprehension with a user-defined function (that will return True or False)
def is_divisible_by_3_and_5(input):
    return if (input % 3 == 0 or input % 5 == 0)

divisible_by_3_and_5 = [i for i in list_of_numbers_1_to_1000 if is_divisible_by_3_and_5(i)]
print(divisible_by_3_and_5)


#3. via a for loop
#This doesn't work. It says invalid syntax
divisible_by_3_and_5 = list()
for i in range(list_of_numbers_1_to_1000):
    print(i)
    if is_divisible_by_3_and_5(input=list_of_numbers_1_to_1000[i])
        divisible_by_3_and_5.append(list_of_numbers_1_to_1000[i])
