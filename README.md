# bookstore
VIEW THE HOSTED SOLUTION
-------------------------

The solution is hosted on https://boiling-oasis-79884.herokuapp.com/  and is connected to a remote MySql database. Click on the link and read from Testing the API section in this document.

INSTALL THE PROJECT ON THE LOCAL MACHINE
-----------------------------------------

To run this project on a local machine, download and extract bookstore-master

Navigate to the bookstore-master in command line

Install Dependencies: Type the following commands
  > pip install -r requirements.txt

If you want to connect your local MySql database, change the settings.py file as follows
    DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': '<your dtabase name>',
        'USER': '<username>',
        'PASSWORD': '<password>',
        'HOST': '<host address(127.0.0.1 in case of local machine)>', 
        'PORT': '3306',
    }
  
After installing dependencies activate shell
  > pipenv shell
 
Now type the following command to runserver
  > python manage.py runserver

Now open browser and go to http://127.0.0.1:8000/

TESTING THE API
----------------
If you're testing the hosted solution, replace 127.0.0.1:8000 with boiling-oasis-79884.herokuapp.com

The project uses djangorestframework to create a REST API. This package has a browsable api which lets us browse through JSON data in a Web browser. It outputs JSON data for command line clients. To view only JSON produced by the page, select JSON from the GET dropdown on the right side.

We get the following output JSON
{
    "books": "http://127.0.0.1:8000/books/"
}

The service requirements in the assignment is obtained by the following endpoints.

Get all books - http://127.0.0.1:8000/books/

Get a single book: http://127.0.0.1:8000/books/1  
  --gets the book with id 1
  
The above get operations are accessible by every user. Click on Login button on the top right of the page. Now type the following username and password:

----username: testuser
----password: abcd.123

The user "testuser" is a normal user. He is not authorized to create, update, or delete books in the database. He has access to following operations:

Get all books - http://127.0.0.1:8000/books/

Get a single book: http://127.0.0.1:8000/books/1  
  --gets the book with id 1

There is another user called "admin" in the database and this user has full access to create, update, or delete books. To test this logout as testuser and login with the following username and password.
--- username: admin
--- password: 1234

Now go to http://127.0.0.1:8000/books/

In the bottom of the page tou can see a form with POST button to create a new book in the database. Enter book details in the form, and click on POST button.

Now you can see the book in the above JSON output. 

Now in the JSON output, you get a url field with which you can navigate to book details. Now click on any of the book's url. You will be navigated to a page where you can see the book details. (or) type the following url in the browser

------ http://127.0.0.1:8000/books/<id>  where id is the id of the book

As you have logged in as admin, you can see a form at the bottom of the page with PUT button which loaded the book details. Modify any of the field to update the book.

Also, there is a DELETE button at the top to delete that book from the database. 

Try logging in as admin and testuser to see the difference between their authorization permissions.

The database used is MySql. You can see in the settings.py file 

    DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'bookstore',
        'USER': 'bookstoreadmin',
        'PASSWORD': 'Book.admin69',
        'HOST': '103.74.54.23',
        'PORT': '3306',
    }
 The above specified database is hosted in my personal web hosting.
 
 So, in a nutshell
 --> I developed the speciified REST API using Django
 --> It provides all the specified services, and also provides 'delete a book' in addition to the services asked in the assignment.
 --> It uses MySql as a backend as asked in the assignment.
 --> The project uses permissions in order to provide authentication and authorization
 
 
 Summary of the services built:
 -----------------------------------------------------------------------------------------------------------------
  URL                                 Request Method             Description                  admin    testuser
 ------------------------------------------------------------------------------------------------------------------
 http://127.0.0.1:8000/books/          GET               gets all the books in database        Yes        Yes
 ------------------------------------------------------------------------------------------------------------------
 http://127.0.0.1:8000/books/          POST                Add a new book                      Yes        No
 ------------------------------------------------------------------------------------------------------------------
 http://127.0.0.1:8000/books/<id>      GET              Get a single book with id 1            Yes        Yes
 ------------------------------------------------------------------------------------------------------------------
 http://127.0.0.1:8000/books/<id>      PUT               Update the book details               Yes        No
 ------------------------------------------------------------------------------------------------------------------
 http://127.0.0.1:8000/books/<id>     DELETE             Delete the book                       Yes        No
 ------------------------------------------------------------------------------------------------------------------
 
 
 
 
 
 
 
 
 
 
