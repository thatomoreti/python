#7-1 Rental Car
rental_type=input("What kind of rental car would you like?")
print(f"Let me see if I can find you a {rental_type}.")

#7-2 Restaurant Seating
dinner_group=input("How many people are in your dinner group?")
group_num=int(dinner_group)

if group_num > 8:
    print("You'll have to wait for a table.")
else:
    print("Your table is ready.")
    

#7-3 Multiples of Ten
number=int(input("Hey , give me a number , any number\n"))

if number % 10 == 0:
    print(f"{number} is a multiple of 10.")
else:
    print(f"{number} is NOT a multiple of 10.")

#7-4 Pizza Topping
prompt=''
while prompt != 'quit':
    prompt=input('What topping do you want?')
    if prompt != 'quit':
        print(f"{prompt} will be added to your pizza.")
    
#7-5 Movie Tickets
hasTicket=False
cost=''
done='n'
#Version 1-->Conditional Test
while done!='y':
    age=int(input("What is your age?"))
    if age >= 3 and age <= 12:
        cost=10
        
        print(f"The ticket will cost ${cost}.")
    elif age <3 :
        cost=0
        print(f"The ticket will cost ${cost}")
    else:
        cost=15
        print(f"The ticket will cost ${cost}")
    done= input("Are you done?")

# #Version 2-->Active Variable
is_done=False
while is_done==False:
    age=int(input("What is your age?"))
    if age >= 3 and age <= 12:
        cost=10
        print(f"The ticket will cost ${cost}.")
    elif age <3 :
        cost=0
        print(f"The ticket will cost ${cost}")
    else:
        cost=15
        print(f"The ticket will cost ${cost}")
    done= input("Are you done?")
    if done=='y'or done=='Y':
        is_done=True
        
#Version 3-->Break Statement
is_done=False
while is_done==False:
    age=int(input("What is your age?"))
    if age >= 3 and age <= 12:
        cost=10
        print(f"The ticket will cost ${cost}.")
    elif age <3 :
        cost=0
        print(f"The ticket will cost ${cost}")
    else:
        cost=15
        print(f"The ticket will cost ${cost}")
    done= input("Are you done?")
    if done=='y'or done=='Y':
        break

#7-7 Infinity
isInfinite=True
while isInfinite==True:
    print("This Loop Will never stop.")


#7-8 Deli
sandwich_orders=['burger','sub','wraps','open-faced','pocket','deep-fried','tea']
finished_sandwiches=[]

while sandwich_orders:
    sandwich=sandwich_orders.pop()
    print(f"I made your {sandwich} sandwich.")
    finished_sandwiches.append(sandwich)
for sw in finished_sandwiches:
    print(f"{sw.title()} sandwich was made.")
    
#7-9 No Pastrami
sandwich_orders=['burger','pastrami','wraps','open-faced','pastrami','deep-fried','tea','pastrami']
finished_sandwiches=[]

print("Sorry everyone , pastrami has run out.")
while 'pastrami' in sandwich_orders:
    sandwich_orders.remove('pastrami')
print(sandwich_orders)
while sandwich_orders:
    sandwich=sandwich_orders.pop()
    print(f"I made your {sandwich} sandwich.")
    finished_sandwiches.append(sandwich)
for sw in finished_sandwiches:
    print(f"{sw.title()} sandwich was made.")
    
#7-10 Dream Vacation 
isFinished=False
total_poll={}

while isFinished==False:
    dream_place=input(f"If you could visit a place in the world , where would you go ?\n")
    name=input(f"What is your name?\n")
    total_poll[name]=dream_place
    pass_on=input(f"Would you like to pass on the poll?Y/N\n")
    if pass_on=='n' or pass_on=='N':
        isFinished=True
for participant,response in total_poll.items():
    print(f"-{participant.title()} would like to go to {response}")