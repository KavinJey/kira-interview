class Book:
    """
    Book class that contains all metrics concerning books.
    Title, author, quantity

    """

    def __init__(self, id, title, author, quantity):
        """
        Book Constructor Class.
        :param id: id of Book (Int)
        :param title: title of Book (String)
        :param author:  author of Book (String)
        :param quantity: quantity of books in Stock (Int)
        """
        self.id = id
        self.title = title
        self.author = author
        self.status = quantity

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

    def getQuantity(self):
        """
        Returns Quantity of Book Instance
        :returns: Quantity of Book in Stock
        :rtype: int
        """
        return self.quantity


class Reservation:
    """
    Reservation class that contains reservations for
    books. This class holds onto who, what and when the book
    is reserved
    """

    def __init__(self, book, person, day):
        """

        :param book:
        :param person:
        :param day:
        """



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
