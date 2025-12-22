#Practice project , helping me practice concepts learned in chapter 4 , 5 , 6 and 7
wardrobe={'hats':['cap','bucket-hat','beanie'],'torso':['black-t','shirt','jacket','long-sleeve t'],'pants':['sweatpants','formal'],'shoes':['nike','adidas','slippers'],'necklaces':['chain','heart-shaped']}
clothes_on_person=[]
isReady=False
while isReady == False :
    response=input("What are you looking for")
    if response in wardrobe:
        wear=input("What do you want to wear?")
        if wear in wardrobe[response]:
            worn_clothes=wardrobe[response].remove(wear)
            clothes_on_person.append(worn_clothes)
    quit=input(f"Are you ready now?Y/N\n")
    if quit =='y' or quit=='Y':
        isReady= True