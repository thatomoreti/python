playlist=["Is it us?","Forget Me Nots","Sense","Sentry"]
name="karabo"
print(f"Here's your chill playlist {name.title()}: {playlist}")

playlist.append("We goin be alright")
print(f"You have successfully added {playlist[4]}")
print(f"Here's your chill playlist {name.title()}: {playlist}")

playlist.insert(2,"Hard Times")
print(f"You have successfully added {playlist[2]}")
print(f"Here's your chill playlist {name.title()}: {playlist}")

print("There's are too many songs in this playlist. The system will delete one")
del_playlist=playlist.pop(1)
print(f"{del_playlist} has been successfully deleted! ")
print(f"Here's your updated chill playlist {name.title()}: {playlist}")

print("There's are too many songs in this playlist still. The system will delete one")
del playlist[0]
print(f"Here's your updated chill playlist {name.title()}: {playlist}")

print(f"Here's your final list in both orders: \n \t{sorted(playlist)}\n\t{sorted(playlist,reverse=True)}")