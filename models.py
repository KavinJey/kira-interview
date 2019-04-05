class Book:
    """
    Book class that contains all metrics concerning books.
    Title, author, quantity.
    """

    def __init__(self, id, title, author, status):
        """
        Book Constructor Class.
        :param id: id of Book (Int)
        :param title: title of Book (String)
        :param author:  author of Book (String)
        :param status: string that represents conditions, for this project
                        only possible statuses are reserved, unreserved
        """
        self.id = id
        self.title = title
        self.author = author
        self.status = status

    def getId(self):
        """
        Returns Id of Book Instance
        :return: Id of Book
        :rtype: Int
        """
        return self.id

    def getTitle(self):
        """
        Returns Title of Book Instance
        :return: Title of Book
        :rtype: String
        """
        return self.title

    def getAuthor(self):
        """
        Returns Author of Book Instance
        :return: Author of Book Instance
        :rtype: String
        """
        return self.author

    def getStatus(self):
        """
        Returns Quantity of Book Instance
        :returns: Quantity of Book in Stock
        :rtype: int
        """
        return self.status

    def setStatus(self, status):
        """
        Setter for status.
        :param status: string that dictates status
=        """
        self.status = status

    def __str__(self):
        return self.title + "By: " + self.author

    def __repr__(self):
        return " | " + self.title + " By: " + self.author + " |"

    def __eq__(self, other):
        """
        :param other: Other Book Object
        :return: Boolean value dictating whether both are equal
        """
        return self.author == other.author and self.title == other.title

    def __hash__(self):
        return hash(('title', self.title,
                     'author', self.author))


class BookGroup:
    """
    Aggregate class for the Collection of books.

    """

    def __init__(self, id, books):
        """
        Book Group constructor. This class will contain
        the quantity of the book instance.
        :param: id, id of group
        :param: books, array full of books
        """
        self.id = id
        self.books = books
        self.quantityAvailable = len(books)
        self.quantityReserved = 0
        self.title = books[0].getTitle()
        self.author = books[0].getAuthor()

    def getAuthor(self):
        return self.author

    def getTitle(self):
        return self.title

    def getQuantityAvailable(self):
        return self.quantityAvailable

    def getQuantityReserverd(self):
        return self.quantityReserved

    def getId(self):
        return self.id

    def removeOneForReservation(self):
        if self.quantityAvailable == 0:
            raise Exception("Quantity is 0. Cannot remove.")

        else:
            # Decrementing by 1
            self.quantityAvailable -= 1
            self.quantityReserved += 1
            self.books[0].setStatus("Reserved")
            self.books.pop(0)

    def __str__(self):
        return "| Id: " + str(self.id) + " | Book Title: " + self.books[0].getTitle() + " | Quantity: " + str(
            self.quantity) + " |"

    def __repr__(self):
        return "| Id: " + str(self.id) + "| Book Title: " + self.books[0].getTitle() + " | Quantity: " + str(
            self.quantity) + " |"


class User:
    """
    Person class that represents a User.
    Since it's a PoC I can hard-code the password
    as a string rather than use encryption or a managed
    Auth service.
    """

    def __init__(self, username, password, isAdmin):
        """
        :param username: username
        :param password: password for user
        :param isAdmin: Boolean value that represents
                        whether the user is an admin
        """
        self.username = username
        self.password = password
        self.isAdmin = isAdmin

    def getUsername(self):
        """
        Getter for Username
        :return: Username -> (String)
        """

    def getPassword(self):
        """
        Getter for User
        :return: Password -> (String)
        """

    def __str__(self):
        return "|" + "Username: " + self.username + " Password: " + self.password + " |"

    def __repr__(self):
        return "|" + "Username: " + self.username + " Password: " + self.password + " |"
