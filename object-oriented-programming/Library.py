# Book
#   Title
#   Author
#   Year

# Library 
#   Add book
#   Remove book
#   View all book
#   Search book (Author, Title, Year)


class Library:
    def __init__(self):
        self.book_list = []
    
    def add_book(self):
        loop = int(input("How many books do you want to add?: "))
        
        for i in range(loop):
            title = input("Title: ").lower()
            author = input("Author: ").lower()
            year = int(input("Year: "))
            
            print(f"You have added {title}, which was written by {author} in {year}")
            
            book = Book(title, author, year)
            self.book_list.append(book)
    
        menu()
    
    def remove_book(self):
        counter = 0
        
        for book in self.book_list:
            counter += 1
            print(f"{counter}) Title: {book.title} | Author: {book.author} | Year: {book.year}")
        
        delete_index = int(input("Press the number corresponding to the book you want to delete: "))
        delete_index = delete_index - 1
        
        book_to_delete = self.book_list[delete_index]
        print(f"Sucessfully deleted {book_to_delete.title}")
        
        del self.book_list[delete_index]
        
        menu()
    
    def view_book(self):
        for book in self.book_list:
            print(f"Title: {book.title} | Author: {book.author} | Year: {book.year}")

        menu()
    
    def search_book(self):
        print("1) Search by Title")
        print("2) Search by Author")
        print("3) Search by Year")
        print("4) Search by Author and Year")
        search_option = int(input("What option would you want?: "))
        
        while True:
# Option 1            
            if search_option == 1:
                title = input("Enter the Title: ").lower()
                counter = 0
                found = False
                
                for book in self.book_list:
                    if book.title == title:
                        counter += 1
                        found = True
                        
                        print(f"{counter}) Title: {book.title} | Author: {book.author} | Year: {book.year}")
                if not found:
                    print("No Books Found")   
                break
# Option 2            
            elif search_option == 2:
                author = input("Enter the Author: ").lower()
                counter = 0
                found = False
                
                for book in self.book_list:
                    if book.author == author:
                        counter += 1
                        found = True
                        
                        print(f"{counter})  Title: {book.title} | Author: {book.author} | Year: {book.year} ")
                    
                if not found:
                    print("No Books Found")
                break
# Option 3
            elif search_option == 3:
                year = int(input("Enter the Year: "))
                
                counter = 0
                found = False
                
                for book in self.book_list:
                    if book.year == year:
                        counter += 1
                        found = True
                        
                        print(f"{counter})  Title: {book.title} | Author: {book.author} | Year: {book.year} ")
                        
                if not found:
                    print("No Books Found")
                break
# Option 4
            elif search_option == 4:
                author = input("Enter the Author: ").lower()
                year = int(input("Enter the Year: "))
                
                counter = 0
                found = False
                
                for book in self.book_list:
                    if book.author == author and book.year == year:
                        counter += 1
                        found = True
                        
                        print(f"{counter})  Title: {book.title} | Author: {book.author} | Year: {book.year} ")
                    
                if not found:
                    print("No Books Found")
                break
            else:
                print("Invalid Option...")
            
            menu()
            
        
                
    

class Book:
    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year

##############################################################
def menu():
    while True:
        print("----- Menu -----")
        print("1. Add Book")
        print("2. Remove Book")
        print("3. View all Books")
        print("4. Search Book")
        print("5. Exit")
        option_menu = int(input("Select an Option: "))
        if option_menu == 1:
            my_library.add_book()
            break
        elif option_menu == 2:
            my_library.remove_book()
            break
        elif option_menu == 3:
            my_library.view_book()
            break
        elif option_menu == 4:
            my_library.search_book()
            break
        elif option_menu == 5:
            print("Goodbye!")
        else:
            print("Invalid Option")
            
 ######################################################           
my_library = Library()

menu()


