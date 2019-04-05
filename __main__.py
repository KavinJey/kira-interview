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

        self.userPool = []
        self.bookGroups = []
        self.singleBooks = []

        # Populates our attribute arrays with objects defined in
        # models.py
        self.initializeAllBooks()
        self.initializeAllUsers()

        flag = True
        while flag:
            print("\nWelcome to Saasvile Public Library's Booking System.")
            username = input("Please enter your username:\t")

            for user in self.userPool:
                if user.getUsername() == username:
                    password = input("Please enter your password:\t")

                    if user.getPassword() == password:
                        print("Login successfully.")
                        if user.getIsAdmin():
                            self.run()
                            flag = False
                        else:
                            print("This is not an admin user and therefore cannot use "
                                  "this system.")
                    else:
                        print("That's not correct. Try Again.")
            else:
                    print("That Username doesn't exist!")

    def run(self):
        """
        Function that runs after User succesfully logins.
        This is where all the routing to different options
        happens. In a traditional web app this would be like
        your routes.
        """
        flag = True
        while flag:
            try:
                print(
                    "\n\nWelcome to the Saasvile Public Library's Book Keeping System.\n\n What would you like to do "
                    "today? (Enter number)")
                choice = int(input(
                    "\n\n1.View all books.\n2.View All Reserved Books\n3.Reserve a book for a User\n4.Search for "
                    "book by Title\n5.Create a new User.\n6.Logout and Exit.\n\n"))

                if choice > 6 or choice < 0:
                    print("That's an invalid choice. Please enter a valid response.")

                else:
                    if choice == 1:
                        self.listAllBooks()
                    elif choice == 2:
                        self.listCurrentlyReserved()
                    elif choice == 3:
                        self.reserveBookForUser()
                    elif choice == 4:
                        self.searchForBookByTitle()
                    elif choice == 5:
                        self.createUser()
                    elif choice == 6:
                        print("See you soon. Bye")
                        flag = False

            except ValueError:
                print("Not a valid choice. Try again.")

    def initializeAllUsers(self):
        """
        This function initializes the user pool
        from a json file located within the directory
        """

        # Our 'users' table
        with open("users.json") as file:
            rawUserPool = json.loads(file.read())
            for user in rawUserPool:
                newUser = User(username=user['username'], password=user['password'], isAdmin=user['isAdmin'])
                self.userPool.append(newUser)

    def initializeAllBooks(self):
        """
        This function initializes the book inventory
        as well as BookGroups
        """

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
            idForBookGroup = 0
            for bookGroup in bookGroups:
                # List comprehension here just takes the singleBooks array,
                # creates one with a single title and
                # attaches it to the BookGroup object
                newBookGroup = BookGroup(idForBookGroup, [book for book in self.singleBooks if
                                                          book.getTitle() == bookGroup.getTitle()
                                                          and book.getAuthor() == bookGroup.getAuthor()])

                self.bookGroups.append(newBookGroup)
                idForBookGroup += 1

    def listAllBooks(self):
        """
        Function that covers the first requirement for the PoC.
        This function is meant to display and print out all the books
        that are in the library.

        """

        # using library called PrettyTable here for nice prints
        table = PrettyTable(["Id", "Title", "Author", "Quantity"])
        for book in self.bookGroups:
            table.add_row([str(book.getId()), book.getTitle(), book.getAuthor(), book.getQuantityAvailable()])
        print(table)

    def listAllBookNotReserved(self):
        """
        This function implements the books that are available.
        Reserved books are kept from this list.
        """

        table = PrettyTable(["Id", "Title", "Author", "Quantity"])
        for book in self.bookGroups:
            if book.getQuantityAvailable() > 0:
                table.add_row([str(book.getId()), book.getTitle(), book.getAuthor(), book.getQuantityAvailable()])

        print(table)

    def listCurrentlyReserved(self):
        """
        This function implements the viewing books that
        are currently reserved feature.
        """
        print("Titles that are reserved:")
        reservedBooks = [book for book in self.singleBooks if book.getStatus() == "Reserved"]
        table = PrettyTable(["Id", "Title", "Author", "Status", "Reserved By"])

        # Making sure we have books to put in the list
        if len(reservedBooks) > 0:
            for book in reservedBooks:
                table.add_row([str(book.getId()), book.getTitle(), book.getAuthor(), book.getStatus(),
                               book.getReservedBy().getUsername()])

        print(table)

    def reserveBookForUser(self):
        """
        This function implements the reservation.
        It will ask the user for the input of the user that
        wants to reserve the book and then lists the books to select
        from.
        """

        print("Welcome to Reservation System. ")

        reserveUser = input("Please enter the user you'd like to reserve for: ")
        reserveUserObject = False
        for user in self.userPool:
            if user.getUsername() == reserveUser:
                reserveUserObject = user

        if not reserveUserObject:
            print("User does not exist. Try again.")

        else:
            print(" \n\n Here is a list of available books:")
            self.listAllBookNotReserved()

            flag = True
            while flag:
                try:
                    bookId = int(input("\n\nWhat book would you like to reserve? (Enter id)"))
                    # Hard coding here bc we have dummy data
                    if 7 < bookId < 0:
                        print("Not a valid id. Try again.")

                    else:
                        for book in self.bookGroups:
                            if book.getId() == bookId:
                                book.removeOneForReservation(reserveUserObject)
                                print(
                                    "%s has been reserved for %s" % (book.getTitle(), reserveUserObject.getUsername()))
                                flag = False

                except ValueError:
                    print("That's not a valid id. ")

    def createUser(self):
        """
        Method to create user. There should be some
        input handling here.
        """
        # Should put input handling here
        username = input("Please enter a username:\t")
        password = input("Please enter a password:\t")
        isAdmin = input("Should this user be an admin? Y or N").upper()

        if isAdmin == "Y":
            newUser = User(username=username, password=password, isAdmin=True)

        elif isAdmin == "N":
            newUser = User(username=username, password=password, isAdmin=False)

        else:
            print("Error, creating user. Incorrect input. Try again.")

    def searchForBookByTitle(self):
        query = input("Please enter title of book you'd like to search for:\t")
        booksThatMatch = []

        for book in self.bookGroups:
            if query.lower() in book.getTitle().lower():
                print(query, book.getTitle())
                booksThatMatch.append(book)

        table = PrettyTable(["Id", "Title", "Author", "Quantity"])
        for book in booksThatMatch:
            if book.getQuantityAvailable() > 0:
                table.add_row([str(book.getId()), book.getTitle(), book.getAuthor(), book.getQuantityAvailable()])

        print("\n\nHere are your results:")
        print(table)


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
