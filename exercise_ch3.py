#3-1 Names
names=['John','Rey','Themba','Kat']
print(names[0])
print(names[1])
print(names[2])
print(names[3])

#3-2 Greeting
print(f"Hi {names[0]}")
print(f"Hi {names[1]}")
print(f"Hi {names[2]}")
print(f"Hi {names[3]}")


#3-3 Your own list
dream_car=['Land Rover','Mercedes','Ferarri']
print(f"I would like to own a {dream_car[0]}")
print(f"I would like to own a {dream_car[1]}")
print(f"I would like to own a {dream_car[2]}")

#3-4 Guest List
guest_list=['Whitney Houston','Mandoza','Nelson Mandela','Chris Hani','Greta Thunberg'];
print(f"\tHi, {guest_list[0]}.\n You are cordially invited to dinner.")
print(f"\tHi, {guest_list[1]}.\n You are cordially invited to dinner.")
print(f"\tHi, {guest_list[2]}.\n You are cordially invited to dinner.")
print(f"\tHi, {guest_list[3]}.\n You are cordially invited to dinner.")
print(f"\tHi, {guest_list[4]}.\n You are cordially invited to dinner.")

#3-5 Changing Guest List
print("Mandoza cannot make it to dinner")
guest_list[1]="Little Simz"
print(f"\tHi, {guest_list[0]}.\n You are cordially invited to dinner.")
print(f"\tHi, {guest_list[1]}.\n You are cordially invited to dinner.")
print(f"\tHi, {guest_list[2]}.\n You are cordially invited to dinner.")
print(f"\tHi, {guest_list[3]}.\n You are cordially invited to dinner.")
print(f"\tHi, {guest_list[4]}.\n You are cordially invited to dinner.")

#3-6 More Guests
print("We managed to find a bigger dinner table , there is more space available now!")
guest_list.insert(0,"Michael Jackson")
guest_list.insert(4,"Thembi Seete")
guest_list.append("Earl Sweatshirt")
print(f"\tHi, {guest_list[0]}.\n You are cordially invited to dinner.")
print(f"\tHi, {guest_list[1]}.\n You are cordially invited to dinner.")
print(f"\tHi, {guest_list[2]}.\n You are cordially invited to dinner.")
print(f"\tHi, {guest_list[3]}.\n You are cordially invited to dinner.")
print(f"\tHi, {guest_list[4]}.\n You are cordially invited to dinner.")
print(f"\tHi, {guest_list[5]}.\n You are cordially invited to dinner.")
print(f"\tHi, {guest_list[6]}.\n You are cordially invited to dinner.")
print(f"\tHi, {guest_list[7]}.\n You are cordially invited to dinner.")

#Shrinking Guest List
print("You can only invite two people to dinner!")
popped_guest=guest_list.pop()
popped_guest1=guest_list.pop()
popped_guest2=guest_list.pop()
popped_guest3=guest_list.pop()
popped_guest4=guest_list.pop()
popped_guest5=guest_list.pop()

print(f"\t We regret to inform that you have been removed from the guest list to for dinner \n {popped_guest}")
print(f"\t We regret to inform that you have been removed from the guest list to for dinner \n {popped_guest1}")
print(f"\t We regret to inform that you have been removed from the guest list to for dinner \n {popped_guest2}")
print(f"\t We regret to inform that you have been removed from the guest list to for dinner \n {popped_guest3}")
print(f"\t We regret to inform that you have been removed from the guest list to for dinner \n {popped_guest4}")
print(f"\t We regret to inform that you have been removed from the guest list to for dinner \n {popped_guest5}")
print(f"\t We are pleased to inform you that you are still invited Mr {guest_list[0]}")
print(f"\t We are pleased to inform you that you are still invited Mrs {guest_list[1]}")
del guest_list[1]
del guest_list[0]
print(guest_list)