import json
#10-1 Learning Python
with open('p_ttxt.txt') as prac_file:
    content=prac_file.read()
print(content)
    
with open('p_ttxt.txt') as prac_files:
    for x in prac_files:
        print(x)
        
# sentences=[]

# with open('p_ttxt.txt') as prac_files:
#     for x in prac_files:
#         sentences.append(x)
        
# for s in sentences:
#     print(s)

with open('p_ttxt.txt') as prac_file:
    sentence=prac_file.readlines()
    
for s in sentence:
    print(s.rstrip())
    
    
#10-2 Learning C
# mod_line=[]

# with open('p_ttxt.txt') as file:
#     line=file.readlines()
#     for l in line:
#        mod= l.replace('learned', 'learnt')
#        mod_line.append(mod)
# for l in mod_line:
#     print(l.rstrip())


# with open('p_ttxt.txt','a') as file:
#     file.write("I love programming mate.")

#10-3 Guest 
# with open('guest.txt','a') as file:
#     response=input("What is your name?")
#     file.write(response)
  
    
#10-4 Guest Book
# done='nothing'
# while done != 'n' and done != 'N':
#     with open('guest_book.txt','a') as file:
#      response=input("What is your name?")
#      print(f"Hi {response}")
#      visit=f"{response.title()} has visited\n"
#      file.write(visit)
#      done=input("Are you done?")
     
# #10-5 Programming Poll
# like_programming=True

# while like_programming!=False:
#     with open('programming.txt','a') as file:
#         like=input("Why do you like programming ?")
#         file.write(f"{like}\n")
#         complete=input("Do you still like programming ?")
#         if complete=='Y' or complete=='y':
#             like_programming=False


# #10-6
# five=5
# other_number=2
# answer=five/other_number
# try: 
#     print(answer)
# except ZeroDivisionError:
#     print("You cant do that man!")
    
# else:
#     print(f"Noice you have an answer")
    
# #10-6 Addition/Addition Calculator
# done='n'

# while done =='n':
#     try:
#         input1=int(input(f"Enter a number any number \n"))
#         input2=int(input(f"Enter a number any number \n"))
#         print(input1+input2)
#     except ValueError:
#         print("Not a number")
#     done=input("Are you done ?")

#10-8 Cats and Dogs/10-9 Silent Cats and Dogs
try:
    with open('cats.txt','r') as file:
        for f in file:
            print(f"{f}\n")
            
    with open('dogs.txt','r') as file:
        for f in file:
            print(f"{f}\n")
except FileNotFoundError:
    # print("File does'nt exist within this repository.")
    print("File does'nt exist within this repository.")

#10-10 Common Words
with open(
    'C:/Users/user101/Downloads/Weird_Book.txt',
    encoding='utf-8',
    errors='ignore'
)as file:
    c=file.read()
    print(c.lower().count('the'))

alive=[1,2,3,4,5,6]
with open('file.json','w') as f:
    json.dump(alive,f)

with open('file.json') as f:
    numbers=json.load(f)
    
    print(numbers)
    
#10-11 Favorite Number 
favourite_number=input("What's your favorite number ??")

with open('fave.json','w') as file:
    json.dump(favourite_number,file)
    print(f"{favourite_number} is your favourite number !")