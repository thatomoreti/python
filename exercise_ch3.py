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

#3-8 Seeing the World
world=['Japan','Nigeria','Kenya','Spain','Ireland']
print(world)
print (sorted(world));
print(world);
print(sorted(world,reverse=True));
print(world);
world.reverse()
print(world);
world.reverse()
print(world);
world.sort();
print(world);
world.sort;
print(world);

#3-9 Dinner Guests
guest_list=['Whitney Houston','Mandoza','Nelson Mandela','Chris Hani','Greta Thunberg'];
print(f"{len(guest_list)} people have been invited to dinner.")


#3-10 Every Function
sports=['Soccer','Rugby','Tennis','Basketball','Netball']
print(f"These are the most popular sports {sports}")


print(f"Oops , not {sports[4]}, we'll replace it with some other sport")
sports[4]='Cricket'

print(f"Here is an updated list of the most popular sports {sports}")

print(f"Steve loves {sports[0]}")
print(f"Jeffery loves {sports[1]}")
print(f"Stella loves {sports[2]}")
print(f"Mohammed loves {sports[3]}")
print(f"James loves {sports[4]}")

print(f"Oh no we did'nt add a favourite sport for Mbali")
sports.insert(0,"Darts")

print(f"Mbali loves {sports[0]}")
print(f"Steve loves {sports[1]}")
print(f"Jeffery loves {sports[2]}")
print(f"Stella loves {sports[3]}")
print(f"Mohammed loves {sports[4]}")
print(f"James loves {sports[5]}")

print(f"Upon further investigation ,golf is also popular ")
sports.append("Golf")
print(f"Here is an updated list of the most popular sports {sorted(sports)}")
print(f"This list has {len(sports)} sports!")

print(f"Lets see the top two sports")
removed_sport=sports.pop()
removed_sport1=sports.pop()
removed_sport2=sports.pop()
removed_sport3=sports.pop()
removed_sport4=sports.pop()

print(f"{removed_sport} has been removed")
print(f"{removed_sport1} has been removed")
print(f"{removed_sport2} has been removed")
print(f"{removed_sport3} has been removed")
print(f"{removed_sport4} has been removed")
print(f"This is your top 2 {sports}")