#3.1
fav_foods= ["Cioppino","Chicken Pot Pie", "Shrimp and Gritts","Uni","Sushi", ]
print(fav_foods[1])
print(fav_foods[-1])
fav_foods.append("Lasagna")
print(fav_foods)
fav_foods.insert(0,"Tea and Biscuts")
# I had an error here since i typed fav_foods.insert("Tea and Biscuts",0. TypeError: 'str' object cannot be interpreted as an integer
# I relized I had the the elment in the wrong spot
fav_foods.remove("Lasagna")
print(fav_foods)
print(len(fav_foods))
for item in fav_foods:
    print (item.upper())
# I kept recieving <built-in method upper of str object at 0x1018813b0>
# This was because I left out the () and had  print (item.upper)
# After looking on line for how to print lists in different ways I found where I went wrong. 
print(fav_foods[0:6:5])
for item in fav_foods:
    e=0
    if item is "potato":
        e+=1
    else:
        e+=0
if e>=1:  
        print("A Potato!")
else:
        print("No Potato!")
#3.2
numbers=list(range(0,20))
print (numbers)
def get_first_15(numbers):
    return numbers[0:15]
print(get_first_15(numbers))
def get_every_5th(numbers):
    return numbers[0:20:5]
print(get_every_5th(numbers))
def get_every_3rd_from_reveresd(numbers):
    reversify = numbers[-1:0:-5]
    return reversify[0:3:3]
print(get_every_3rd_from_reveresd(numbers))
numbers = [
[1, 2, 3],
[4, 5, 6],
[7, 8, 9]
]
print(numbers[2])
print(numbers[1][1])
numbers.append([10,11,12])
print(numbers)
def sum_nested(numbers):
    x=0
    for item in numbers:
        i=item
        for item in i:
            if isinstance(item,int):
                x = x+item
    return x
print(sum_nested(numbers))
#This is where I learned about the isinstance(item,int) feature of python which allows you to check if the item is an integer.
#I was really struggling here until I figured oput how to determine if an item was an integer. 
#I originally had for item in i: x=x+item, but now with the code bove the whole function works. 
#3.4 
def grid_maker():
    five_by_five=[]
    count=1
    for y in range (5):
        row=[]
        for f in range(5):
            row.append(count)
            count += 1
        five_by_five.append(row)
    return five_by_five
g=grid_maker()
print(g)
def question_marks(g):
    for item in g:
        j=item
        for item in j:
            if isinstance(item,int):
                if item == 3 or item == 6 or item == 9 or item == 12 or item == 15 or item == 18 or item == 21 or item == 24 :
                    j.append("?")
                

    return g
print(question_marks(g))
def add_it(g):
    sum=0
    for item in g:
        j=item
        for item in j:
            if isinstance(item,int):
                sum +=item
    return sum
print (add_it(question_marks(g)))

ages = {
"Katie": 30,
"Mariam": 42,
"Safia": 25,
"Mira": 48
}
print (ages["Katie"])
ages["Mira"]=100
print (ages["Mira"])
ages["Milana"]=52
del ages["Mariam"]
def keys(ages):
    for key in ages:
        print (key)
keys(ages)


