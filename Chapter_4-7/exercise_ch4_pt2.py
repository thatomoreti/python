#4-3 Counting to Twenty
for val in range(1,21):
    print(val)
    
#4-4 One Million
millions=[]
for million in range(1,1000001):
     millions.append(million)
print(millions)

#4-5 Summing a Million
millions=[]
for million in range(1,1000001):
     millions.append(million)
print(min(millions))
print(max(millions))
print(sum(millions))

#4-6 Odd Numbers
odd=[]
for number in range(1,21,2):
    odd.append(number)
print(odd)

#4-7 Threes 
threes=[]
for three in range(3,31,3):
    threes.append(three)
print(threes)

#4-8 Cubes
for cube in range(1,11):
    print(cube**3)
    
#4-9 Cube Comprehension
cubes=[cube**3 for cube in range(1,11)]
print(cubes)

#Slicing Demonstration 
print(cubes[:2])

#4-10 Slices
artist=['Earl Swearthshirt','Queen','Lauryn Hill','Bob Marley','Rihanna']
print(f"The first three artists in my list are:{artist[:3]}")
print(f"The middle three artists in my list are:{artist[1:4]}")
print(f"The last three artists in my list are:{artist[2:]}")    

#4-11 My Pizzas , Your Pizzas
my_pizzas=['Pepperoni','Tuna','Hawaiian','Double-Cheese']
friends_pizzas=my_pizzas[:]

# idk any other pizza flavour :(
my_pizzas.append("Turkish Delight")
friends_pizzas.append("French Mess")

print("My favourite pizzas are:")
for pizza in my_pizzas:
    print(f" -{pizza}")
    
print("\nMy friend's favourite pizzas are:")
for pizza in friends_pizzas:
    print(f" -{pizza}")
    
#4-12 More Loops
my_foods = ['pizza', 'falafel', 'carrot cake']
friend_foods = my_foods[:]

my_foods.append("burger")
friend_foods.append("steak")

print("My favorite foods are:")
for food in my_foods:
    print(f"{food}")

print("\nMy friend's favorite foods are:")
for food in friend_foods:
    print(f"{food}")
    
#4-13 Buffet
buffet=('Juice','Chicken','Turkey','Beef','Burgers')
for food in buffet:
    print(f"+{food}")
    
buffet=('\nLamb','Chicken','Turkey','Beef','Ham')
for food in buffet:
    print(f"+{food}")