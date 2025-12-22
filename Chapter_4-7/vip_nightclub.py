#A project simulating a VIP nighclub , to help me practice chapter 4-7
entry_queue=[{'name':'james','age':18,'has_ticket':True},{'name':'henry','age':22,'has_ticket':False},{'name':'thato','age':31,'has_ticket':True},{'name':'jacob','age':43,'has_ticket':False},{'name':'mbalenhle','age':23,'has_ticket':True}]
inside_club=[]

while entry_queue:
    person_in= entry_queue.pop(0)
    if person_in['age'] < 18:
        print(f"Access Denied:{person_in['name'].title()} you are {person_in['age']}, that is too young.")
    elif person_in['age'] > 10 and person_in['has_ticket'] == False:
        print(f"Go buy a ticket {person_in['name'].title()}")
    else: 
        inside_club.append(person_in)
        print(f"Welcome in {person_in['name'].title()}!")

for insider in inside_club:
    print(f"{insider['name'].title()} is in the club!")