#8-8 User Album
def make_album(
    a_name,a_title,n_songs=None
                ):
    album={'Album Name':a_name,'Album Title':a_title,'Number of Songs':n_songs}
    if n_songs != None:
        album['Number of Songs']=n_songs
    show_album=print(album)
    return show_album

def whatevs():
    print("Fodder function.")
# while True:
#     a_name=input("Who is the Name of The Artist?")
#     a_title=input("What is the Name of The Album?")
#     num_songs=input("How many songs are in the album?")
#     done=input("Are you done ?")
#     make_album(a_name,a_title,num_songs)
#     if done == "Y" or "y":
#         break