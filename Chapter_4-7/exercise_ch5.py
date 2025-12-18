#5-1 Conditional Test
player='Messi'
print("Is player == 'Messi'? I predict false")
print(player == 'Messi')


print("\nIs player == 'Ronaldo'? I predict false")
print(player == 'Ronaldo')

wrestler='John Cena'
print("\nIs wrestler == 'John Cena'? I predict True")
print(wrestler == 'John Cena')

print("\nIs wrestler == 'Randy Orton'? I predict false")
print(wrestler == 'Randy Orton')

food='Egg'
print("\nIs food == 'Egg'? I predict True")
print(food == 'Egg')

print("\nIs food == 'Apple'? I predict false")
print(food == 'Apply')

song='What Now?'
print("\nIs song == 'What Now?'? I predict true")
print(song == 'What Now?')

print("\nIs song == 'Sense'? I predict false")
print(song == 'Sense')

shoe='Nike'
print("\nIs shoe == 'Nike'? I predict true")
print(shoe == 'Nike')

print("\nIs shoe == 'Adidas'? I predict false")
print(shoe == 'Adidas')


#5-2 More Conditional Tests

print("\nIs the player != 'Ronaldo'? I predict true")
print(player != 'Ronaldo')

print("\nIs the player != 'Messi'? I predict false")
print(player != 'Messi')

print("\nIs the player == 'messi'? I predict true")
print(player.lower() == 'messi')

print("\nIs the player == 'MESSI'? I predict false")
print(player == 'MESSI')

senior=50
young=20

print('Is young less than senior?I predict true')
print(young < senior)

print('\nIs young greater than senior?I predict false')
print(young > senior)

print('\nIs young equal to senior?I predict false')
print(young == senior)
print('\nIs young unequal to senior?I predict true')
print(young != senior)

print('\nIs both young and senior greater than or equal to 20?I predict true')
print(young >= 0 and senior >= 20)

print('\nIs  young or senior less than or equal to 18?I predict false')
print(young <= 18 or senior <= 18)

groceries=['tuna','cheese','milk']
print("\nIs water included in the groceries?I predict False")
print('water' in groceries)

print("\nIs cheese included in the groceries?I predict true")
print('cheese' in groceries)

print("\nIs cheese not included in the groceries?I predict false")
print('cheese' not in groceries)

print("\nAre grapes not included in the groceries?I predict true")
print('grapes' not in groceries)

#5-3 Alien Colors #1
alien_color = 'red'

if alien_color == 'green':
    print('You just earned 5 points!')
    
#5-4,5 Alien Colors #2-3
if alien_color == 'green':
    print('You just earned 5 points!')
elif alien_color == 'yellow':
    print('You just earned 10 points!')
elif alien_color == 'red':
    print('You just earned 15 points!')


#5-6 Stages of Life
age = 19

if age < 2:
    print("This person is a baby!")
elif age >= 2 and age<4:
    print("This person is a toddler!")
elif age >= 4 and age<14:
    print("This person is a kid!")
elif age >= 13 and age<20:
    print("This person is a teenager!")
elif age >= 20 and age<65:
    print("This person is an adult!")
elif age >= 65:
    print("This person is an elder!")

#5-7 Favorite Fruit
favorite_fruit = ['watermelon','banana','apple','lemon','mango']
if 'watermelon' in favorite_fruit:
    print("You really love watermelon huh?")

if 'lemon' in favorite_fruit:
    print("You really love lemon huh?")

if 'pawpaw' in favorite_fruit:
    print("You really love pawpaw huh?")
    
if 'banana' in favorite_fruit:
    print("You really love banana huh?")
    
if 'kiwi' in favorite_fruit:
    print("You really love kiwi huh?")
    
#5-8 Hello Admin and 5-9 No-Users 
usernames = []
#usernames=['jamewiseman','lebronisthegoat','stepchef','kdslimreeper','SGAissmooth']
if usernames:
    for username in usernames:
        if username =='lebronisthegoat':
            print("Hey G.O.A.T, thank you for logging in! Please score 60 points")
        elif username =='stepchef':
            print("Hey Chef, thank you for logging in! Please cook for us tonight")
        else:
            print(f"Hi {username}, thanks for logging in ")
else:
    print("We need to find some users!")
    
#5-10 Checking Usernames
current_users = ['jamewiseman','lebronisthegoat','stepchef','kdslimreeper','SGAissmooth']
lower_cu = [current_user.lower() for current_user in current_users]
new_users = ['harden-j','wemby','lebronisthegoat','stephchef','tatum']
lower_nu = [new_user.lower() for new_user in new_users]

for new_user in lower_nu:
    for current_user in lower_cu:
        if new_user == current_user:
            print({f"{new_user} is taken , use another username."})


#5-11 Ordinal Numbers
numbers = []
for number in range(1,10):
    numbers.append(number)
    if number == 1:
        print("1st")
    elif number==2:
        print("2nd")
    elif number==3:
        print("3rd")
    elif number==4:
        print("4th")
    elif number==5:
        print("5th")
    elif number==6:
        print("6th")
    elif number==7:
        print("7th")
    elif number==8:
        print("8th")
    else:
        print("9th")