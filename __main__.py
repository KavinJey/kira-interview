import json
from prettytable import PrettyTable
from models import Book, User, BookGroup


class Main:
    """
    Main Program that does the initialization
    of the system as well as the interaction between
    User and program
    """

    def __init__(self):
        """
        This function acts as the login as well as starting the main
        program (calling run()), it also initializes all the books, etc.
        """

        # Loading in our dummy data and creating objects
        # for easier manipulation

        self.users = []
        self.bookGroups = []
        self.singleBooks = []

        # Populates our attribute arrays with objects defined in
        # models.py
        self.initializeAllBooks()
        self.initializeAllUsers()

        while True:
            print("Welcome to Saasvile Public Library's Booking System.")
            username = input("Please enter your username:\t")

            for user in self.userPool:
                if user.getUsername() == username:
                    password = input("Please enter your password:\t")
                    if user.getPassword() == password:
                        print("That's not correct. Try Again.")
                    else:
                        print("Login successfully.")
                        self.run()
                        break

    def run(self):
        """
        Function that runs after User succesfully logins.
        This is where all the routing to different options
        happens. In a traditional web app this would be like
        your routes.
        """

        print("\n\nWelcome to the Saasvile Public Library's Book Keeping System.\n\n What would you like to do today?")

    # TODO: Comment and document this code
    def initializeAllUsers(self):
        # Our 'users' table
        with open("users.json") as file:
            rawUserPool = json.loads(file.read())
            for user in rawUserPool:
                newUser = User(username=user['username'], password=user['password'], isAdmin=user['isAdmin'])
                self.users.append(newUser)

    # TODO: Comment and document this code
    def initializeAllBooks(self):
        with open('data.json') as books:
            rawBooks = json.loads(books.read())

            for book in rawBooks:

                # Creating individual books for inventory and
                # for reservation
                for n in range(int(book['quantity'])):
                    newSingleBook = Book(id=book['id'], title=book['title'], author=book['author'], status=False)

                    self.singleBooks.append(newSingleBook)

            bookGroups = set(self.singleBooks)
            # Quick increment variable
            id = 0
            for bookGroup in bookGroups:
                # List comprehension here just takes the singleBooks array, creates one with a single title and
                # attaches it to the BookGroup object
                newBookGroup = BookGroup(id, [book for book in self.singleBooks if
                                              book.getTitle() == bookGroup.getTitle() and book.getAuthor() == bookGroup.getAuthor()])
                self.bookGroups.append(newBookGroup)
                id += 1

    def listAllBooks(self):
        """
        Function that covers the first requirement for the PoC.
        This functino is meant to display and print out all the books
        that are in the library.

        """

        # using library called PrettyTable here for nice prints
        table = PrettyTable(["Id", "Title", "Author", "Quantity"])

        for book in self.bookGroups:
            table.add_row([str(book.getId()), book.getTitle(), book.getAuthor(), book.getQuantity()])
        print(table)

    def listCurrentlyReserved(self):
        print("Titles that are reserved:")
        reservedBooks = [book for book in self.singleBooks if book.getStatus() == "Reserved"]
        table = PrettyTable("Id", "Title", "Author", "Status")
        for book in reservedBooks:
            table.add_row([str(book.getId()), book.getTitle(), book.getAuthor() ,book.getStatus()])

        print(table)

    def reserveBookForUser(self):
        pass

    def createUser(self):
        pass


if __name__ == '__main__':
    # Pseudo code for main method

    # Initialize Logging program
    # Login Required (User logs in)
    # Options outlined:
    #       List all books
    #       Searching for book by title
    #       Reservation of all available books
    #       Viewing all books reserved
    #       Create User
    # if exit
    #   exit
    # else
    #   restart
    Main()

