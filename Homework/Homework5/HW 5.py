###Basic Lambda Function
##To test odd or even
def odd_or_even(x):
    if x % 2 == 0:
        return "Even"
    else:
        return "Odd" 
print(odd_or_even(5)) 
print(odd_or_even(10))

###Advanced Lambda Function
##To sum a list
def sum_list(y):
    total = 0 
    for num in y:
        total += num
    return total
print (sum_list([2,2,2,2,2]))


###Sorting with lambda
def get_age(person):
    return person[1]
people = [("Aman", 29), ("Reet", 32), ("Singh", 35)]
print(sorted(people, key=get_age))


###Filtering with lambda
def filter_even(numbers):
    result = []
    for num in numbers:
        if num % 2 == 0:
            result.append(num)
    return result
numbers = [3,2,5,4,6,7,9,0]
print(filter_even(numbers))
 

###Mapping with lambda
def square_numbers(numbers):
    return list(map(lambda x: x**2, numbers))
print(square_numbers(numbers))


###Reducing with lambda
from functools import reduce ###learned about this from the internet. Need it to use reduce function. 
def multiply_numbers(numbers):
    return reduce(lambda x, y: x*y, numbers)
print(multiply_numbers(numbers))


###Enumerating with lambda
def enumerate_list(numbers):
    return list(enumerate(numbers, start=3))
print(enumerate_list(numbers))


###Zipping with lambda
def zip_lists(names, ages):
    return list(zip(names, ages))
names = ["Preet", "Reet", "Singh"]
ages = [29, 32, 35]
print(zip_lists(names, ages))