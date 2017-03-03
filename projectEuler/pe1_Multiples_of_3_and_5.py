#Project Euler Problem 1
#https://projecteuler.net/problem=1

# If we list all the natural numbers below 10
# that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.
# Find the sum of all the multiples of 3 or 5 below 1000.

max_range = 1000

list_of_numbers_1_to_1000 = list(range(1,max_range+1,1))

#Solution 1. via list comprehension
divisible_by_3_and_5 = [i for i in list_of_numbers_1_to_1000 if (i%3==0 or i%5==0)]
print(sum(divisible_by_3_and_5))
#234168

#Solution 2. via list comprehension with a user-defined function (that will return True or False)
def is_divisible_by_3_and_5(input):
    if (input % 3 == 0 or input % 5 == 0):
        return True
    else:
        return False

divisible_by_3_and_5 = [i for i in list_of_numbers_1_to_1000 if is_divisible_by_3_and_5(i)]
print(sum(divisible_by_3_and_5))


#Solution 3. via a for loop
divisible_by_3_and_5 = list()
for i in range(len(list_of_numbers_1_to_1000)):
    if (list_of_numbers_1_to_1000[i] % 3 == 0 or list_of_numbers_1_to_1000[i] % 5 == 0):
        divisible_by_3_and_5.append(list_of_numbers_1_to_1000[i])
    else:
        continue

print(sum(divisible_by_3_and_5))
