# homework1.py
# --- Variables and Data Types ---
a= 10
print(a)
print(type(a))
# a is an integer, a whole number with no decimals
b= 1.5
print(b)
print(type(b))
# b is a float, a number with decimals
c= 3j
print(c)
print(type(c))
# c is a complex , a number part imaginary and part real
d= "hello"
print(d)
print(type(d))
# d is a str, textual data
e= [1, 2, 3]
print(e)
print(type(e))
# e is a list, used to store an ordered collection of items
f = {"name": "Ellen", "favorite fruit": "strawberry"}
print(f)
print(type(f))
# f is a dict, a collection of key-value pairs
g = (1, 2)
print(g)
print(type(g))
# g is a tuple, ordered immutible sequence of items
h = ["apple", "banana", "strawberry"]
print(h)
print(type(h))
# h is also a list
i = True
print(i)
print(type(i))
# i is a bool, a true or false value 
j = None
print(j)
print(type(j))
# j is a NoneType, abscence of value
k = [True, "blue", 12]
print(k)
print(type(k))
# k is a list aswell
l = str(14)
print(l)
print(type(l))
# d is a str, textual data
m = 1e4
print(m)
print(type(m))
# d is a float, it is 1^4 with a decimal zero
# Question 1: 9 datatypes
# Question 3: b and m, d and l, e h and k
# Question 2: int, float, complex, str, dict, list, tuple, bool, NoneType
print( 10 > 9)
#True, greater than 
print(10 == 9)
#False, not equal
print(10 <= 9)
# False, not equal
print(bool("abc"))
# True
print(bool(123))
#True
print(bool(["apple", "cherry", "banana"]))
 #True
print(bool(True))
#True
print(bool(False))
#False
print(bool(0))
#False
print(bool(""))
#False
print(bool(" "))
#True
print(bool(()))
#False
print(bool([]))
#False
print(bool({}))
#False
print(bool(True and False))
#False
print(bool(True and True))
#True
print(bool(False and False))
#False
print(bool(True or False))
#True
print(bool(True or True))
#True
print(bool(False or False))
#False
print(bool(not(False)))
#True
print(bool(not(True)))
#False
