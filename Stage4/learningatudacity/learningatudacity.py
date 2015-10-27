import webapp2
import jinja2
import os
import re
import random
import logging
import time
from crypto import Crypto
from udacity_datastore import *
from data_validation import *
from template_creation import generate_htmlstring

# sets templates directory relative application main file
TEMPLATES_DIR = os.path.join(os.path.dirname(__file__), "templates")
jinja_env = jinja2.Environment(loader = jinja2.FileSystemLoader(TEMPLATES_DIR),
                               extensions = ['jinja2.ext.autoescape'],
                               autoescape = "true")

# empty list objects for areas and userposts
areas = []
userposts = []

# get the last concept from datastore Concepts kind, so that we can traverse through its ancestory
lastconcept = Concepts.query(Concepts.last == True).get()

# Iterating through all concepts using parent property, loop breaks when it reaches an entity with no parent.
# This loop also stores all of entities in areas list object
while lastconcept:
    areas.insert(0, lastconcept)
    if not lastconcept.key.parent() is None:
        # if current iterative entity has a parent, make the parent as iterative entity for next iteration
        lastconcept = lastconcept.key.parent().get()
    else:
        break

logging.debug("change")
# This will help read the entity with no parent in Concepts kind
if lastconcept and not areas:
    areas.insert(0, lastconcept)

# Looping through all posts and storing it in usersposts list object in the form of tuples (time, post)
for each in Posts.query():
    if not each in userposts:
        userposts.append(each)

# As userposts is list of tuples, when sorted, all tuples are orderby posted date/time
userposts.sort()

class Handler(webapp2.RequestHandler):
    """WEBAPP2 Request Handler inherited class"""
    def write(self, *a, **kw):
        """Writes Responses to the screen"""
        self.response.write(*a, **kw)

    def render_str(self, template, **params):
        """renders template with provided params"""
        t = jinja_env.get_template(template)
        params = self.read_params(**params)
        return t.render(params)

    def render(self, template, **kw):
        """writes render template to screen"""
        self.write(self.render_str(template, **kw))

    def get_templates(self):
        """Generates templates dynamically using subclassess"""
        return [kls.__name__ for kls in Handler.__subclasses__()]

    def get_current_user(self):
        """
        Queries for current user using cookies
        Returns username if logged in else returns None
        """
        if self.request.cookies.get("user_id") and self.request.cookies.get("user_id") != '':
            self.usr = Users.get_by_username(self.request.cookies.get("user_id"))
            return self.usr.dispname
        else:
            return None

    def read_params(self, **params):
        """
        Reading all params on the fly
        """
        if self.__class__ not in [Blog] + Blog.__subclasses__():
            params['areas'] = areas
            params['posts'] = userposts
            params['user_dispname'] = self.get_current_user()
            logging.debug(params['user_dispname'])
            params['templates'] = self.get_templates()
        if self.__class__ is MainPage:
            params['home'] = True
        if self.request.get("getmetopic") == "Fetch" and self.request.get("topic"):
            concept_by_title = Concepts.query(Concepts.title == self.request.get("topic")).get()
            params['displayconcept'] = concept_by_title
        return params

class MainPage(Handler):
    """
    Inherited class of Handler class, which is inturn webpage handler for mainpage
    """
    def get(self):
        """
        Renders mainpage template to screen
        Also handles few forms with get methods on main page
        """
        if self.request.get("surpriseme") == "true" and areas:
            self.render("mainpage.html", displayconcept = random.choice(areas))
        else:
            self.render("mainpage.html")

    def post(self):
        """
        Handles forms with method post
        Fetches the user name and post and adds it to UserPosts Kind in datastore as an entity.
        """
        if self.request.get("login"):
            self.uname = str(self.request.get("username"))
            self.pwd = str(self.request.get("password"))
            if self.uname and self.uname != '':
                # If user name is provided and defined, encrypts it for checking/writing to database
                # Also uses it for cookie to retrieve user data
                # Encryption is needed for security
                self.encrypted_uname = Crypto.encrypto_wo_salt(self.uname)

            errors = validate_loginform(uname = self.encrypted_uname, pwd = self.pwd)
            if errors:
                self.render("mainpage.html", username = self.uname, **errors)
            else:
                self.response.headers.add_header("Set-Cookie", "user_id = {username}".format(username = self.encrypted_uname))
                self.redirect("/mainpage")

        if self.request.get("logout"):
            # unsets user_id cookie
            self.response.headers.add_header("Set-Cookie", "user_id = {username}".format(username = ''))
            # redirects to mainpage
            self.redirect("/mainpage")

        if self.request.get("post"):
            self.display_name = self.get_current_user()
            self.post = self.request.get("comment")
            if self.post and self.display_name:
                new_post = Posts(post = self.request.get("comment"), user = self.display_name)
                new_post.put()
                userposts.append(new_post)
                self.render("mainpage.html")
            else:
                self.render("mainpage.html", posterror = "Null Comments are not allowed")

class ShoppingCart(Handler):
    """
    Inherited class of Handler class and a webpage handler for shopping cart application
    """
    def get(self):
        """
        Handles form with get method
        Gets all products and lists all products added so far
        This is an example for get forms
        """
        products = self.request.get_all("product")
        self.render("shoppingcart.html", products = products)

class FizzBuzz(Handler):
    """
    Inherited class of Handler class and a webpage handler for FizzBuzz application
    """
    def get(self):
        """
        Gets the input number as a string and converts it to number
        It iterates through 0 to input number and 
        If divisible by 3, prints Fizz
        If divisible by 5, prints Buzz
        If divisible by both, print FizzBuzz
        This is good application that shows handling logic inside templates
        """
        n = self.request.get("n")
        n = n and int(n)
        self.render("fizzbuzz.html", n = n)

class ValidateDate(Handler):
    """
    Inherited class of Handler class and a webpage handler for date validation application
    """
    def get(self):
        """
        Gets month, day and year from user
        If all three are defined, they are inputted to post method.
        This is done this way to demonstrate that get and post methods can also be connected.
        """
        month = self.request.get("month")
        day = self.request.get("day")
        year = self.request.get("year")
        if month and day and year:
            self.post(month = month, day = day, year = year)
        else:
            self.render("validatedate.html")

    def post(self, month="", day="", year="", error = ""):
        """
        This post method receives inputs from get method and validates the date
        Post validation, it posts result to the user.
        """
        if validate_date(month, day, year):
            self.render("validatedate.html", month = month, day = day, year = year,
                        message = "Awesome!! You have entered a Valid Day", col = "green")
        else:
            self.render("validatedate.html", month = month, day = day, year = year,
                        message = "Invalid Day", col = "red")

class ROT13Cipher(Handler):
    """
    Inherited class of Handler class and a webpage handler for ROT13 cipher application
    ROT13 cipher meaning, encrypts user input by advancing each alphabet character by 13 characters
    in a cyclic manner.
    """
    def get(self, **kw):
        """
        Renders page for receiving inputs to encrypt
        """
        self.render("rot13cipher.html", val = self.request.get("text"))

    def post(self):
        """
        Once the input is posted, encrypt it and posted it back to user in same text area
        """
        text_to_encrypt = self.request.get("text") if self.request.get("text") else None
        encrypted_text = rot13cipher(text_to_encrypt) if text_to_encrypt else ""
        self.render("rot13cipher.html", val = encrypted_text)

class SignUp(Handler):
    """
    Inherited class of Handler class and a webpage handler for user registration, login and logout
    operations.
    This will also set a cookies which will help in identifying user.
    """
    # CONSTANT Time to sleep for datastore to get update, immediate redirection is causing problems at times
    DATASTORE_LATENCY = 1
    def get(self):
        """
        Checks if user is logged in.
        If user is logged in, renders the page with logout option
        If user is not logged in, renders the page with signup/registration form and login form
        """
        if self.request.cookies.get("user_id"):
            self.render("signup.html", already_logged_in = True)
        else:
            self.render("signup.html")

    def post(self):
        """
        Registration form to register a new user
        Login form to sign in to the website.
        Logout form to logout from the website.
        Also does the validation of all fields during registration
        Once logged in, redirects to Main Page.
        """
        self.uname = str(self.request.get("username"))
        self.pwd = str(self.request.get("password"))
        if self.uname and self.uname != '':
            # If user name is provided and defined, encrypts it for checking/writing to database
            # Also uses it for cookie to retrieve user data
            # Encryption is needed for security
            self.encrypted_uname = Crypto.encrypto_wo_salt(self.uname)
        else:
            self.encrypted_uname = None
        if self.request.get("signup"):
            self.disname = str(self.request.get("dispname"))
            self.verify = str(self.request.get("verify"))
            self.email = str(self.request.get("email"))
            self.errors = validate_signupform(uname = self.uname, pwd = self.pwd, disname = self.disname,
                                              verify = self.verify, email = self.email)
            if self.errors:
                self.render("signup.html", username = self.uname, email = self.email, **self.errors)
            else:
                # once validation goes through, a new entity is created in Users Kind with
                # encrypted username and salt encrypted password (hashlib and hmac alogorithms
                # used)
                Users.register_newuser(disname = self.disname, usrname = self.encrypted_uname,
                                       pwd = Crypto.encrypto(self.pwd), email = self.email)
                self.response.headers.add_header("Set-Cookie", "user_id = {username}".format(username = self.encrypted_uname))
                # providing 1 seconds for datastore to get updated
                time.sleep(DATASTORE_LATENCY)
                self.redirect("/mainpage")
        elif self.request.get("login"):
            # validates if user login and password are correct, if authenticated, sets cookie
            # and redirects to Welcome Page
            errors = validate_loginform(uname = self.encrypted_uname, pwd = self.pwd)
            if errors:
                self.render("signup.html", username = self.uname, **errors)
            else:
                self.response.headers.add_header("Set-Cookie", "user_id = {username}".format(username = self.encrypted_uname))
                self.redirect("/mainpage")
        elif self.request.get("logout"):
            # Logs out, unset the cookie and re-direct to SingUp Page
            self.response.headers.add_header("Set-Cookie", "user_id = {username}".format(username = ''))
            self.redirect("/signup")

class AddContent(Handler):
    """
    Inherited class of Handler class and a webpage handler for adding content to website
    This page is accessible to only logged in users and users who have the magic word
    """
    def get(self):
        """
        Provides a page to enter content, title and magic word field to add content to website
        """
        self.render("addcontent.html", contentadd = True)

    def post(self):
        """
        Gets title, concept and magic word from the form
        Validates all the fields, if there are no errors, adds to content to Concepts Kind
        """
        if self.request.get("magicword"):
            title = self.request.get("title")
            concept = self.request.get("concept")
            if title == "" or concept == "":
                # If there are errors, renders it back with errors
                self.render("addcontent.html", error = "Please add both title and Concept", contentadd = True)
            else:
                # gets the current last/recently added concept (concept with last field set to True)
                prnt = Concepts.query(Concepts.last == True).get()
                if not prnt is None: 
                    # create an entity with last field set to true and parent field set to recently added entity's key
                    tmp = Concepts(concept = generate_htmlstring(title, concept), title = title, parent = prnt.key, last=True)
                    # as there can be only one recently added concept, setting previous last concept entity last field to False
                    prnt.last=False
                    # committing the preivous recently/last added concept changes
                    prnt.put()
                else:
                    # If this is the first time concept being added, entity creation happens without parent field
                    tmp = Concepts(concept = generate_htmlstring(title, concept), title = title, last=True)
                # Commiting post to datastore
                tmp.put()
                self.redirect("/addcontent")
        else:
            self.render("addcontent.html", error = "You need right Magic word to add content", contentadd = True)

class Blog(Handler):
    """
    Inherited class of Handler class and a webpage handler for Blog page
    """
    def get(self):
        """
        Displays all blogs in an order
        """
        blogposts = BlogPosts.query().order(-BlogPosts.posted_on)
        self.render("blog.html", blogposts = blogposts)

class BlogPost(Blog):
    """
    Inherited class of Blog class and a webpage handler for each blog post permalink
    """
    def get(self, post_id):
        """
        Whenever a new post is posted to Blog, displays a blog post
        """
        blog_post = BlogPosts.get_by_id(int(post_id))

        if not blog_post:
            self.error(404)
            return

        self.render("blog.html", blogposts = [blog_post])

class NewPost(Blog):
    """
    Inherited class of Blog class and a webpage handler for adding a blog post
    """
    def get(self):
        """
        Displays a form to post new post.
        """
        self.render("/newpost.html")

    def post(self):
        """
        Gets title and content from posted data and stores it in Concepts kind (Data store)
        If success, redirects to blog post permalink, else errors are displayed
        """
        title = self.request.get("subject")
        content = self.request.get("content")
        if title and content:
            add_to_store = BlogPosts(title = title, blogpost = content)
            newpost = add_to_store.put()
            self.redirect("/blog/" + str(newpost.id()))
        else:
            self.render("/newpost.html", title = title, post = content, error = "Title and Content Please")

# web application with all web page handlers
app = webapp2.WSGIApplication([('/', MainPage),
                               ('/mainpage', MainPage),
                               ("/validatedate", ValidateDate),
                               ("/shoppingcart", ShoppingCart),
                               ("/fizzbuzz", FizzBuzz),
                               ("/signup", SignUp),
                               ("/addcontent", AddContent),
                               ("/rot13cipher", ROT13Cipher),
                               ("/blog", Blog),
                               ("/blog/(\d+)", BlogPost),
                               ("/blog/newpost", NewPost)], debug=True)