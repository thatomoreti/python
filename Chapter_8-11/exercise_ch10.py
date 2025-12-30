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
     
#10-5 Programming Poll
like_programming=True

while like_programming!=False:
    with open('programming.txt','a') as file:
        like=input("Why do you like programming ?")
        file.write(f"{like}\n")
        complete=input("Do you still like programming ?")
        if complete=='Y' or complete=='y':
            like_programming=False
