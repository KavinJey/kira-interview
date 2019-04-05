# Kira Interview Assessment

#### Usage 

This program is developed as part as the Kira Interview Assesment. 
The task was to create a program that has the following functionality:
* List all books in inventory
* Allow searching for books by title
* Allow reservation of available books
* Viewing books currently reserved 



This program is build in Python and uses the command line to interface with it. There is a user system for the employees to use. 

The default admin 'user' is: 

```{"username": "kavin", "password": "testPass"}```

The default library customer is:

```{"username": 'testUser', "password": 'newPass'}```

There are multiple features available. The program will prompt you with options for what to do next. 

The main screen has 6 options:

1. View All Books
2. View All Reserved Books
3. Reserve A Book For a User
4. Search for a book by Title
5. Create a new User 
6. Logout and Exit

Each of these options have prompts that make interaction intuitive. 

#### Build

This program is built using Python3 and 1 dependency library. In order to run the program, you'll first need to clone the repo. 

`git clone https://github.com/KavinJey/kira-interview.git`

`cd kira-interview`

After we have the files we'll have to create a virtualenv in order to install dependencies 

**(Assuming virtualenv is installed on your Linux machine)**

`virtualenv env -p python3`

`source env/bin/activate`

`pip install -r requirements.txt`



After which you can run the program by doing

`python __main__.py`



#### Technical Documentation

`models.py` defines most of our models. We have a Book, BookGroup and a User class. 

I'll go over what they do: 



`class Book`

This class is for a single book within the inventory. I wanted to be able to set status on the books and so making each (1) book an instance of a class made sense. Status can include things like "Reserved", "Damaged", etc.This also means that single books can be further developed (add attributes like serial #, history of borrows, etc).

The attributes for this are:

* Id
* Title
* Author
* ReservedBy
* Status 

This class mainly has getters and setters for its attributes



`class BookGroup`

This class is for a single type of book within the inventory. Think of this class as an aggregate class. It contains all the single books that make up the title as an attribute. This class also handles the reservation of books through functions. 

The attributes for this are:

* Id
* Books (Array of Book Objects)
* Quantity Available
* Quantity Reserved
* Title
* Author 

The way reservations work is by decremented the quantity available, increment the quantity reserved, changing the status of a single book within the book array. 



`class User`

This class represents either an admin user (library employee) or a customer of the library. This is just normal user/pass. The password is stored as a plain text string which is bad practice, however for a PoC this is fine. 

The attributes for this are:

* username
* password
* isAdmin (boolean)



`The __main__.py` file runs the main program and orchestrates everything. A lot of the PoC features are etched out here. Within this file a class called `Main` is declared, this class represents the entire library system and we'll go in depth of what that means:



`class Main`

The initialize function controls the flow of the program. The pseudo code for the entire program is as follows: 

~~~python
```
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
```
    

~~~

The attributes are as follows:

* userPool (array of User Objects)
* bookGroups (array of BookGroup objects)
* singleBooks (array of all single books)

Lets go over the functions in this class:

`__init__()`

This function initializes everything. At first I wrote all the data initialization within this function however it quickly got messy and required re-factoring. 

This function also calls `initializeAllBooks()` which takes the json file within th e directory containing the test data provided and parses and creates objects for better interaction. This function also calls `initializeAllUsers()` which takes `users.json` and creates User objects. 

After calling both those functions we go ahead and start the sign-in flow. If a User isn't a admin then they can't login to this system.  After logging in, the function will call `run()`



`run()`

After the user successfully authenticates, they're brought into the `run()` function. This function acts as a router for all the other features. Within a Django application this would by your `urls.py` or `routes.js` for React. This prompts the user for what they want to do, takes that input, and runs a function that fulfills the feature.



`listAllBooks()`

This implements the feature of listing the books. This function uses a python package called PrettyTable for outputting the books as nice looking tables. Essentially all this function is doing is taking the attribute associated with the class (bookGroups) and spitting it out as a nice table. 



`listCurrentlyReserved()`

This function is almost a copy cat of `listAllBooks()`. The only difference being that I use list comprehension to filter by the books that contain the status 'Reserved'. 



`reserveBookForUser()`

This function implements the reservation feature. It only makes sense that you'd need to specify a user to reserve the book for and so this function prompts for the username of the user that you want to reserve the book for. After doing so we call the `removeOneForReservation` function on the bookGroup object which handles all the data handling 



`createUser()`

This function is just helpful for creating Users if ever necessary. 



`searchForBookByTitle()`

This function implements the search by title feature. How this works is it takes a query string from the User and creates an empty array to hold the things that match the query. Then we run through all the bookGroups and look for titles that contain the query string, if it does we append it to the empty array and after going through all the books we return that list as a table similar to the `listAllBooks()`





If you have any questions, let me know!