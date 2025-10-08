def say_goodbye(name):
    print("Goodbye,",name)

name= "Nolan"
say_goodbye(name)

def area_of_circle(r):
    print((r**2)*3.14)

r=1
area_of_circle(r)

a=2 
b=4
def devide(a,b):
    return a/b
print(devide(a,b))
def subtract(a,b):
    return a-b
print(subtract(a,b))
def multiply(a,b):
    return a*b
print(multiply(a,b))
def temp_range(list):
    return (min(list), max(list))
list=[15, 14, 17, 20, 23, 28, 20]

print(temp_range(list))

def is_weekend(day):
    if day == 6 or day == 7:
        return "It’s the weekend!"
    else:
        return "It’s not the weekend."
day=1
print(is_weekend(day))


def car_efficiency(a,b):
    return a/b 
#a=miles, b=gallons
print(car_efficiency(a,b))
def encrypt(data):
    ne=data<0
    data=abs(data)
    if data<10:
        return -data if ne else data
    last_num= data%10
    others=data//10
    while others>0:
        others//=10
    enc= last_num + others
    return -enc if ne else enc

data= (2478)
print(encrypt(data))

def raise_to_power(x,y):
   for _ in range((y)):
    return x*x
x=2
y=2
print(raise_to_power(x,y))


def minimum_val(numbers):
  min_val= numbers[0]
  for num in numbers:
    if num < min_val:
      min_val=num
numbers= [5,6,9]
print(min(numbers))
def maximum_val(numbers):
  max_val= numbers[0]
  for num in numbers:
    if num< max_val:
      max_val=num
print(max(numbers))

def min(numbers):
    x=1
    min=numbers[0]
    while x<len(numbers):
        if numbers[x]<min:
            min=numbers[x]
        x +=1
    return min
numbers=[5,6,7]
print (min(numbers))

# def max(numbers):
#     x=1
#     max=numbers[0]
#     while x<len(numbers):
#         if numbers[x]>max:
#             max=numbers[x]
#         x +=1
#     return max
# numbers=[5,6,7]
# print (max(numbers))

def sum_of_digits(numberhere):
    counter=0
    for digit in str(abs(numberhere)):
       counter += int(digit)
    return counter
           

numberhere=2468
print(sum_of_digits(numberhere))

def max(numbers):
    x=1
    max=numbers[0]
    while x<len(numbers):
        if numbers[x]>max:
            max=numbers[x]
        x +=1
    return max
numbers=[5,6,7]
print (max(numbers))