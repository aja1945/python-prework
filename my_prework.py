# Question 1:
# Write a function to print "hello_USERNAME!" USERNAME is the input of the function. The first line of the code has been defined below.

def hello_name(aja1945):
   print("hello_name")
name =("Hello aja1945")
print(name)

# Question 2:
# Write a python function, first_odds that prints the odd numbers from 1-100 and returns nothing.

def first_odds(odd_numbers):
    odd_numbers = range(1,101,1)
    for value in (range(1,101,1)):
       odd_numbers =list(range(1,101,1))
    value.append(odd_numbers)

# Question 3: 
#  Please write a Python function, max_num_in_list to return the max number of a given list.

def max_num_in_list(list):
   max = list[0]
   for a in list:
      if a > max:
         max = a
         return max
print(max_num_in_list([0,5,20]))

# Question 4
# Write a function to return if the given year is a leap year. A leap year is divisible by 4, but not by 100, unless divisible by 400. the return should be boolean Type(true/false).

def is_leap_year(a_year):
  if(a_year % 4 ==0):
     if(a_year % 100 == 0):
        if(a_year % 400 == 0):
           leap =True
        else:
           leap=False
        return leap
     

# Question 5
# Write a function to check to see if all numbers in list are consecutive numbers.

        check = [1,2,4,6]
def is_consecutive(a_list):
   total = 2 
   while total> 1:
      test = a_list.pop(0)
      if test == a_list[0] -1:
         total = len(a_list)
         return True
      else:
         return False
         break
works = is_consecutive("check2")
print(works)


