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
# True,filled string
print(bool(123))
#True, argument is true
print(bool(["apple", "cherry", "banana"]))
 #True, complete list
print(bool(True))
#True, true returs true
print(bool(False))
#False, false because directly false
print(bool(0))
#False, zero equates to false
print(bool(""))
#False, empty string creating falsy value
print(bool(" "))
#True string contains a space, therefor true 
print(bool(()))
#False, empty creating a falsy value
print(bool([]))
#False, empty creating a falsy value
print(bool({}))
#False, empty creating a falsy value
print(bool(True and False))
#False, essentialy print false
print(bool(True and True))
#True, true is only argument
print(bool(False and False))
#False, false is only argument
print(bool(True or False))
#True, essentially print true
print(bool(True or True))
#True, only option is true
print(bool(False or False))
#False, false is only argument
print(bool(not(False)))
#True, only other optio is true
print(bool(not(True)))
#False, only other option is false
# Question 1: When an argument is true, a true is returend, which includes when strings are filled or an answer is objectivley true. 
# Question 2: The space counted as a string which yeilded a true value. 
# Question 3: bool("Hello") Returns true since a string is present
# Question 4: bool ("water", "") Incomplete list so false
print(10+5) # 15, + performs addition  
print(10-5) # 5, - performs subtraction
print(2*4) # 8, * performs multiplication
print(6/3) # 2, / performs division
print(5%2) # 1, Returns remainder
print(3**2) # ** is three to the power of 2
print(15//2) # // preforms division then rounds
print(5==2) # == determines equality
print(10!=10) # returns false 
print(2<5) # true since 2 is less than 5
print(12>5) # true since 12 is greatger than 5
print(5<=6) # true, 5 is less than or equal to six
print(1>=10) # 1 is less than or equal to 10
x=5
x += 5
print(x) # added five
x-=4
print (x) #subtracted four
x*=3
print (x) # multiplied by three
# 1) an and operand returns true only if both conditions are true, 2=5 and 5=5 would return false but 2=2 and 5=5 would be true
# 2) or checks if at least one condition is true so 2=5 or 5=5 would be true and 2=5 or 2=3 would be false
# 3) the not operator inverts a true to false so 5=10 is true and 10=10 is false
# More Questions:
# 1: / divides and // rounds the answer
# 2: % gives remainder and // gives answer rounded
# 3: % so 4%5 would give the remainder of 4/5
# 4: assignment operators stor values given to vairables
my_string="hello"
print(my_string) # Prints: hello
print (my_string[0])# prints h 
print (my_string[1])# prints e
print (my_string[2])#prints l
print (my_string[3])#prints l
print (my_string[4])#prints o
print (my_string[-1])# prints o
print (my_string[1:3])# prints el
print (my_string[0:5:2])# prints hlo
print(len(my_string))# pritns 5
print (my_string+"goodbye")#prints hellogoodbye
print (7*my_string)# prints hello seven times 
# slicing extracs a specific portion of a string, any manipulations where specific parts of the string were separated
name="Oski"
print ("Hello my name is", name)
print(f"Hello, my name is {name}")
# and f string is inerted into the second manipulation wich is a more conscise formatiting way to embed expressions into a string
# cd is change directory and it allows you to switch into a file such as cd nolan
#ls lists everything in a file, when in file nolan, call ls to list 
# ls -a shows hidden files, call ls -a to list all files and hidden files in a directory
#  mkdir makes a directrory, mkdir nolan
# cat prints a file, cat nolan.txt
#pwd prints the working directory and tells you where you are, just type pwd in terminal
# 
# 
# cd ∼ returnst to home directory, ex cd ∼
# cp copys a file, ex: cp nolan 
# mv moves a file mv nolan desktop ex: 
# rm removes files or directories ex: rm nolan
# clear clears the terminal, ex: clear
# grep stands for global regular expression print ex: grep [options] pattern [file...]
# git add, adds a file to the worktree, git add [file]
# git status, tells status of worktree when in git folder git status
# git commit, saves file to external cloud after on worktree, git commit [file]
# ls -a shows even hidden files
# a hidden file is not shown under a rgular list
# -l shows detailed information, git --version shows installed version, wc -l counts number of lines in a file
# flags are add ons to base commands
