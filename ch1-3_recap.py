#To practices the concepts covered in Chapters 1 to 3, this script will be simulating contact book to demonstrate use fo a list , adding to a list and deleting a contact from a list.
phonebook=['Jeniffer','John','Kilua','Lana Bell','Kgotso','Karabo']
print(f"\t Phone Book: You have {len(phonebook)} contacts \n\t {phonebook}")

phonebook.append("Obakeng")
print(f"You have added {phonebook[6]} successfully to your phonebook!")
print(f"\t Phone Book: You have {len(phonebook)} contacts \n\t {phonebook}")

phonebook.insert(0,"Freddy")
print(f"You have added {phonebook[0]} successfully to your phonebook!")
print(f"\t Phone Book: You have {len(phonebook)} contacts \n\t {phonebook}")

removed_contact=phonebook.pop(-3)
print(f"You have removed {removed_contact} successfully from your phonebook!")
print(f"\t Phone Book: You have {len(phonebook)} contacts \n\t {phonebook}")

del phonebook[4]
print(f"\t Phone Book: You have {len(phonebook)} contacts \n\t {phonebook}")

print(f"You have opted to order your contacts in alphabetical order \n{sorted(phonebook)}")
print(f"You have opted to order your contacts in reverse order \n{sorted(phonebook,reverse=True)}");

print(f"Final Phone book list:{phonebook}")

probability=len(phonebook)/10*100

print(f"You have a {probability}% likelihood of deleting your next contact")