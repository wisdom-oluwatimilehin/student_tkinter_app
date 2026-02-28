from functools import reduce
x = lambda a,b:a+b
print(x(3,4))

# MAP FUNCTION
numlist = [2,4,5,6]
# def summer(i):
#     return i + 10
e = lambda a:  a + 10

r = map(e,numlist)
# a = map(summer ,numlist)
print(list(r))

# REDUCE FUNCTION
def add(val1,val2):
    return val1*val2


# product = reduce(lambda x,y: x * y , numlist)
product = reduce(add , numlist)
print(product)

# FILTER FUNCTION
fruits = ['mango','apple','grape','orange']
# check = filter(lambda x:x.islower(),fruits)
# check = filter(lambda x:x>5,numlist)
# 
# def look(a):
#         return a[0] == "a"

a = lambda s: s[0] == "a"
check = filter(a,fruits)
print(list(check))

# LOCAL VARIABLE AND GLOBAL VARIABLE
# local - inside a function and works only within the function
# global can be accessible any where 


# GENERATOR FUNCTION
# uses yield instead of return in generator
# returns a list
# use next to see the values
# shows just one value
# enables us to control values

# def display(num):
#     for i in num:
#         print(i)

# display([90,45,23,12])

def gen_display(num):
    for i in num:
        yield i

output = gen_display([90,45,23,12])
print(next(output))
print(next(output))
print(next(output))

# scores = [98,67,34,56]
# values = [for a in scores]
# print(values)

# file input and output
# binary mode
# tk interface 

# write a python program that takes the name of a user and displays it in reverse order
# writa a python program to find those numbers which are divisible by 7 and multiple of 5 between 1500 and 2700


def score(x):
        return x + 10

ss = lambda x: x + 10

