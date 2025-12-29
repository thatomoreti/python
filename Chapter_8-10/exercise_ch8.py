#8-1 Message
def display_message():
    print("In chapter 8 ,I will be learning about functions, how the work, how they are called and what they are.")
display_message()

#8-2 Favorite Book
def favorite_book(title):
    print(f"My favorite book is {title}")
favorite_book('Life of Pi')

#8-3 T-Shirt
def make_shirt(size,text):
    print(f"The shirt is a size {size}, and on it, it is written:{text}")
make_shirt(36,'Thw World is Yours!')
make_shirt(text='Money Trees is the perfect place for shading , thats just how i feel',size=22)

#8-4 Large Shirts
def make_shirt(text,size='Large'):
    print(f"The shirt is a size {size}, and on it, it is written:{text}")
make_shirt("Power!")

#8-5 Cities
def describe_city(city_name,city_country='South Africa'):
    print(f"{city_name.title()} is in {city_country.title()}")
describe_city('Toronto')
describe_city('Cape Town')
describe_city('Durban')

#8-6 City Names
def city_country(city_name,city_country):
    output=print(f"{city_name.title()}, {city_country.title()}")
    return output
city_country('Lagos','Nigeria')
city_country('Nairobi','Kenya')
city_country('Kuraman','South Africa')

#8-7 Album
def make_album(a_name,a_title,n_songs=None):
    album={'Album Name':a_name,'Album Title':a_title,'Number of Songs':n_songs}
    if n_songs != None:
        album['Number of Songs']=n_songs
    show_album=print(album)
    return show_album

make_album('Kendrick','To Pimp A Butterfly')
make_album('J Cole','2014 Forest Hill Drive',12)
make_album('Paramore','Paramore','N/A')
 
# #8-8 User Album
# def make_album(a_name,a_title,n_songs=None):
#     album={'Album Name':a_name,'Album Title':a_title,'Number of Songs':n_songs}
#     if n_songs != None:
#         album['Number of Songs']=n_songs
#     show_album=print(album)
#     return show_album

# while True:
#     a_name=input("Who is the Name of The Artist?")
#     a_title=input("What is the Name of The Album?")
#     num_songs=input("How many songs are in the album?")
#     done=input("Are you done ?")
#     make_album(a_name,a_title,num_songs)
#     if done == "Y" or "y":
#         break

#8-9 Messages 
messages=['We on it!','Live , Laugh, Love','Hey You']

def show_messages(messages):
    for text in messages:
        print(text)
show_messages(messages)

#8-10 Sending Messages
def send_messages(messages):
    sent_messages=[]
    while messages:
        text=messages.pop()
        print(f"Message:{text} is being sent")
        sent_messages.append(text)
    return sent_messages

# s_messages=send_messages(messages)
# print(messages)
# print(s_messages)

#8-11 Archived Messages
a_messages=send_messages(messages[:])
print(messages)
print(a_messages)

#8-12 Sandwiches 
def sandwich_orders(*orders):
    print(f"Summary of Orders:")
    for o in orders:
        print(f"\t-{o}")
sandwich_orders('burger','sub')
sandwich_orders('burger','sub','samoosa','kota')
sandwich_orders('burger')

#8-13 User Profile
def build_profile(first, last, **user_info):
    """Build a dictionary containing everything we know about a user."""
    user_info['first_name'] = first
    user_info['last_name'] = last
    return user_info
user_profile = build_profile('karabo', 'moreti',
interest='music',
fave_sport='football')
print(user_profile)

#8-14 Cars
def build_car(manufacturer_name, model_name, **car_info):
    """Build a dictionary containing everything we know about a car."""
    car_info['manufacturer name'] = manufacturer_name
    car_info['model name'] = model_name
    return car_info
cars = build_car('mercedes', 'x-18',
color='black',
horse_power='136 k/h')
print(cars)
