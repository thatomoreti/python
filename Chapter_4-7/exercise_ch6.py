#6-1 person 
person={'first_name':'karabo','last_name':'moreti','age':21,'city':'johannesburg'}
print(person['first_name'])
print(person['last_name'])
print(person['age'])
print(person['city'])

#6-2 favorite numbers
favorite_numbers={'james':2,'ayanda':4,'karabo':5,'lola':7,'pertunia':1}
for fave in favorite_numbers:
    print(f"{fave}'s favourite number is {favorite_numbers[fave]}")

#6-3 glossary
glossary={'list':'arrays , a cluster of variables according to index','dictionary':'collection of key-value pairs','if-statements':'conditionals and actions to take if they are are true or false','conditional checks':'checks for specific conditions','loop':'the repetition of repetitive tasks ','sets':'a group of data','object-oriented programming':'programming that employs the use of classes also using abstraction ','sdlc':'software development lifecycle; the life cycle that shows how software is built','software development principles':'principles that inform how to go about about the stages mentioned in the software development life cycle','SQL':'Language used to create databases and query said database','import':'reserved word in Python that allows the use of external libraries based on the one imported'}

for term in glossary:
    print(f"{term} \n'{glossary[term]}'")

#6-4 Glossary 2
for term, definition in  sorted(glossary.items()):
    print(f"{term}:{definition}")

#6-5 Rivers 
major_rivers={'nile':'egypt','victoria lake':'kenya','grand canyon':'usa'}
for river,country in major_rivers.items():
    print(f"The {river.title()} runs through {country.title()}")
    
    
#6-6 Polling
favorite_languages = {
'jen': 'python',
'sarah': 'c',
'edward': 'ruby',
'phil': 'python',
'karabo':'javascript',
'nsindiso':'java'
}
poll_takers=['jen','steve','karabo','brandon','phil']
for poll_taker in poll_takers:
    if poll_taker not in favorite_languages:
        print(f"{poll_taker.title()}, please take the poll")
    else:
        print(f"{poll_taker.title()}, thanks for taking the poll")
        
#6-7 People
person1={'first_name':'karabo','last_name':'moreti','age':21,'city':'johannesburg'}
person2={'first_name':'steve','last_name':'jackson','age':35,'city':'benoni'}
people=[]

people.append(person1)
people.append(person2)

for person in people:
    print(person)

#6-8 Pets
dog={'animal type':'canal','owner name':'steve'}
cat={'animal type':'feline','owner name':'karabo'}
snake={'animal type':'reptile','owner name':'jack'}
fox={'animal type':'canal','owner name':'ayanda'}
goat={'animal type':'mammal','owner name':'aobakwe'}

animals=[]

animals.append(dog)
animals.append(cat)
animals.append(snake)
animals.append(fox)
animals.append(goat)

for animal in animals:
    print(f"\n{animal}")
    
#6-9 Favorite Places
favorite_places={'thato':['durban','ohio','nairobi'],'kevin':['joburg','pretoria','lagos'],'lusanda':['midrand','oklahoma','barcelona']}
for name, place in favorite_places.items():
    print(f"\n{place} are favourite places for {name} ")

#6-10 Favorite Numbers
favorite_numbers={'james':[2,6,19],'ayanda':[4,7,15],'karabo':[5,82,62],'lola':[7,88,10],'pertunia':[1,44,55,66]}
for fave,number in favorite_numbers.items():
    print(f"{fave}'s favorite numbers are {number}")
    
#6-11 Cities
cities={'durban':{'country':'south africa','population':'2 million','fact':'it has a beach'},'barcelona':{'country':'spain','population':'4 million','fact':'it has the best team in the world'},'manchester':{'country':'england','population':'10 million','fact':'it has the best team in the world too!'}}
for city,detail in cities.items():
    print(f"{city}:{detail}")
    

