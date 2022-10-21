# Question 1: Write a function to print "hello_USERNAME!" USERNAME is the input of the function. The first line of the code has been defined as below.

def hello_name(user_name):
    print("Welcome back " + user_name + " it has been 90 days since your last sign on we missed you!") 
user_name = input("What is your User ID? ")
hello_name(user_name)

# Question 2: Write a python function, first_odds that prints the odd numbers from 1-100 and returns nothing.

def first_odds():
    for x in range(1,100):
        if x % 2 != 0:
            print(x)
first_odds()

# Question 3: Please write a Python function, max_num_in_list to return the max number of a given list. The first line of the code has been defined as below.

def max_num_in_list(a_list):
    max_list = max(a_list)
    return max_list
a_list = [4654, 654652, 41213216, 651, 54542, 123, 3, 2, 54316584, 5461233]
print(max_num_in_list(a_list))

# Question 4: Write a function to return if the given year is a leap year. A leap year is divisible by 4, but not divisible by 100, unless it is also divisible by 400. The return should be boolean Type (true/false).

def is_a_leap_year(a_year):
    if a_year % 4 == 0:
        return True 
    if a_year % 4 != 0:
        return False
    if a_year % 400 and 100 == 0:
        return True
    if a_year % 100 != 0:
        return False
print(is_a_leap_year(3044))

# Question 5: Write a function to check to see if all numbers in list are consecutive numbers. For example, [2,3,4,5,6,7] are consecutive numbers, but [1,2,4,5] are not consecutive numbers. The return should be boolean Type.
    
def is_consecutive(a_list):
    return sorted(a_list) == list(range(min(a_list), max(a_list) +1))
a_list = [6,9,8,5,2,3,4] 
def is_consecutive(b_list):
    return sorted(b_list) == list(range(min(b_list), max(b_list) +1))
b_list = [1,2,3,4,5,6,7,8,9] 
print(is_consecutive(a_list))
print(is_consecutive(b_list))
