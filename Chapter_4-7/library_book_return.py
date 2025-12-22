#A project simulating a library return system , to help me practice chapter 4-7
checked_out_books=['I write what I like','Life of Pi','Killman','The Book']
return_books=[]
toQuit=False
while toQuit == False:
    book=input('What book do you want to return?')
    if book in checked_out_books:
        removed_book=checked_out_books.remove(book)
        return_books.append(book)
        print(f"Thank you for returning the book: {book}")
    else:
        print("Book was not checked out from the library.")
    done=input(f"Are you done?Y/N\n")
    if done == 'Y' or done == 'y':
        toQuit=True
        
for r_book in return_books:
    print(f"\tThese book has been returned:{r_book}\n")