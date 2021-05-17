class Library:      # a class library that will perform funtions like display, issuing and recieving books
    def __init__(self, lib):
        self.books = lib

    def displaybooks(self):
        
        for b in self.books:
            print(">"+b)

    def Borrowbook(self, bookname):
        if bookname in self.books:
            print(f"{bookname} book has been issued")
            self.books.remove(bookname)
            return True
        else:
            print("The book is either not available or has already been issued to someone else")
            return False

    def returnbook(self, bookname):
        self.books.append(bookname)
        print("The books has been returned, Thank you <3")


class Student:          #a class student that will call class librar when the books are either returned or issued
    def reqbook(self):
        self.book = input("Enter the name of the book: ")
        return self.book

    def returnbook(self):
        self.book = input("Enter the name of the book that is to be returned: ")
        return self.book

if __name__ == "__main__":      
    cenlib = Library(["Django" , "Java" , "Python" , "C++"])    #there are the books that are being used for demonstration of the program
    student = Student()
    cenlib.displaybooks()
    while(True):
        welcomemsg = '''\n ==== Welcome to Central Library ====         
        Please Choose an Option:
        1. List all the books
        2. Request a book
        3. Add/Return a book
        4. Exit 
        '''                     #this is the welcome message for the user 
        print(welcomemsg)       
        a = int(input("Enter a choice: "))          #this will take the integer value from the user
        if a == 1:                                   #the entered the value will compared here and the corresponding function will be called
            cenlib.displaybooks()
        elif a == 2:
            cenlib.Borrowbook(student.reqbook())
        elif a == 3:
            cenlib.returnbook(student.returnbook())
        elif a == 4:
            exit()
        else:
            print("Invalid choice")
    print(welcomemsg)
