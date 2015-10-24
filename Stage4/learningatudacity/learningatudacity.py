import webapp2
import jinja2
import os
import re
import random
import logging
from crypto import *
from udacity_datastore import *
from data_validation import *
from template_creation import generate_htmlstring

TEMPLATES_DIR = os.path.join(os.path.dirname(__file__), "templates")
jinja_env = jinja2.Environment(loader = jinja2.FileSystemLoader(TEMPLATES_DIR),
                               extensions = ['jinja2.ext.autoescape'],
                               autoescape = "true")

areas = []
userposts = []
lastconcept = Concepts.query(Concepts.last == True).get()

while lastconcept:
    logging.debug("in for")
    areas.insert(0, lastconcept)
    if not lastconcept.key.parent() is None:
        # if current iterative entity has a parent, make the parent as iterative entity for next iteration
        lastconcept = lastconcept.key.parent().get()
        logging.debug("in if")
    else:
        logging.debug("in else")
        break

if lastconcept and not areas:
    logging.debug("in if")
    areas.insert(0, lastconcept)

for each in Posts.query():
    if not each.post in userposts:
        userposts.append((str(each.posted_on), each.user, each.post))

userposts.sort()

class Handler(webapp2.RequestHandler):
    """WEBAPP2 Request Handler inherited class"""
    CURRENT_USER = None

    def write(self, *a, **kw):
        """Writes Responses to the screen"""
        self.response.write(*a, **kw)

    def render_str(self, template, **params):
        """renders template with provided params"""
        t = jinja_env.get_template(template)
        params['areas'] = areas
        params['posts'] = userposts
        return t.render(params)

    def render(self, template, **kw):
        """writes render template to screen"""
        self.write(self.render_str(template, **kw))

    def get_templates(self):
        """Generates templates dynamically using subclassess"""
        return [kls.__name__ for kls in Handler.__subclasses__()]

class MainPage(Handler):
    def get(self):
        if self.request.get("getmetopic") and self.request.get("topic"):
            concept_by_title = Concepts.query(Concepts.title == self.request.get("topic")).get()
            self.render("mainpage.html", templates = self.get_templates(), home=True, displayconcept = concept_by_title)
        elif self.request.get("surpriseme") == "true" and areas:
            self.render("mainpage.html", templates = self.get_templates(), home=True, displayconcept = random.choice(areas))
        else:
            self.render("mainpage.html", templates = self.get_templates(), home=True)

    def post(self):
        logging.debug("I am in post")
        post = self.request.get("post")
        uname = self.request.get("username")
        if not uname:
            self.render("mainpage.html", templates = self.get_templates(),
                        home = True, error = True)
        if post:
            new_post = Posts(post = self.request.get("comment"),
                             user = uname)
            npos = new_post.put()
            userposts.append([npos.uname_lc, npos.posted_on, npos.post])
            self.render("mainpage.html", templates = self.get_templates(),
                        home = True, posts = userposts)

class ShoppingCart(Handler):
    def get(self):
        products = self.request.get_all("product")
        self.render("shoppingcart.html", templates = self.get_templates(), products = products)

class FizzBuzz(Handler):
    def get(self):
        n = self.request.get("n")
        n = n and int(n)
        self.render("fizzbuzz.html", templates = self.get_templates(), n = n)

class ValidateDate(Handler):
    def get(self):
        month = self.request.get("month")
        day = self.request.get("day")
        year = self.request.get("year")
        if month and day and year:
            self.post(month = month, day = day, year = year)
        else:
            self.render("validatedate.html", templates = self.get_templates())

    def post(self, month="", day="", year="", error = ""):
        if validate_date(month, day, year):
            self.render("validatedate.html", templates = self.get_templates(),
                        month = month, day = day, year = year, message = "Awesome!! You have entered a Valid Day", col = "green")
        else:
            self.render("validatedate.html", templates = self.get_templates(),
                        month = month, day = day, year = year, message = "Invalid Day", col = "red")

class ROT13Cipher(Handler):
    def get(self, **kw):
        self.render("rot13cipher.html", templates = self.get_templates(), val = self.request.get("text"))

    def post(self):
        text_to_encrypt = self.request.get("text") if self.request.get("text") else None
        encrypted_text = rot13cipher(text_to_encrypt) if text_to_encrypt else ""
        self.render("rot13cipher.html", templates = self.get_templates(),
                    val = encrypted_text)

class SignUp(Handler):
    def get(self):
        if self.request.cookies.get("user_id"):
            self.render("signup.html", templates = self.get_templates(), already_logged_in = True)
        else:
            self.render("signup.html", templates = self.get_templates())

    def post(self):
        self.uname = str(self.request.get("username"))
        self.pwd = str(self.request.get("password"))
        if self.uname and self.uname != '':
            self.encrypted_uname = encrypto_wo_salt(self.uname)
        if self.request.get("signup"):
            self.disname = str(self.request.get("dispname"))
            self.verify = str(self.request.get("verify"))
            self.email = str(self.request.get("email"))
            self.errors = validate_signupform(uname = self.uname, pwd = self.pwd, disname = self.disname,
                                              verify = self.verify, email = self.email)
            if self.errors:
                self.render("signup.html", templates = self.get_templates(),
                            username = self.uname, email = self.email, **self.errors)
            else:
                Users.register_newuser(disname = self.disname, usrname = self.encrypted_uname,
                                       pwd = encrypto(self.pwd), email = self.email)
                self.response.headers.add_header("Set-Cookie", "user_id = {username}".format(username = self.encrypted_uname))
                self.redirect("/welcome")
        elif self.request.get("login"):
            errors = validate_loginform(uname = self.encrypted_uname, pwd = self.pwd)
            if errors:
                self.render("signup.html", templates = self.get_templates(),
                            username = self.uname, **errors)
            else:
                self.response.headers.add_header("Set-Cookie", "user_id = {username}".format(username = self.encrypted_uname))
                self.redirect("/welcome")
        elif self.request.get("logout"):
            self.response.headers.add_header("Set-Cookie", "user_id = {username}".format(username = ''))
            self.redirect("/signup")

class Welcome(SignUp):
    def get(self, *kw):
        if self.request.cookies.get("user_id"):
            self.usr = Users.get_by_username(self.request.cookies.get("user_id"))
            self.render("welcome.html", username = self.usr.dispname)
        else:
            self.redirect("/signup")

class AddContent(Handler):
    def get(self):
        self.render("addcontent.html", templates = self.get_templates(), contentadd = True)

    def post(self):
        if self.request.get("magicword"):
            title = self.request.get("title")
            concept = self.request.get("concept")
            if title == "" or concept == "":
                self.render("addcontent.html", templates = self.get_templates(), error = "Please add both title and Concept", contentadd = True)
            else:
                prnt = Concepts.query(Concepts.last == True).get()
                if not prnt is None: 
                    tmp = Concepts(concept = generate_htmlstring(title, concept), title = title, parent = prnt.key, last=True)
                    prnt.last=False
                    prnt.put()
                else:
                    tmp = Concepts(concept = generate_htmlstring(title, concept), title = title, last=True)
                tmp.put()
                self.redirect("/addcontent")
        else:
            self.render("addcontent.html", templates = self.get_templates(), error = "You need right Magic word to add content", contentadd = True)

class Blog(Handler):
    def get(self):
        blogposts = BlogPosts.query().order(-BlogPosts.posted_on)
        self.render("blog.html", blogposts = blogposts)

class BlogPost(Blog):
    def get(self, post_id):
        blog_post = BlogPosts.get_by_id(int(post_id))

        if not blog_post:
            self.error(404)
            return

        self.render("blog.html", blogposts = [blog_post])

class NewPost(Blog):
    def get(self):
        self.render("/newpost.html")

    def post(self):
        title = self.request.get("subject")
        content = self.request.get("content")
        if title and content:
            add_to_store = BlogPosts(title = title, blogpost = content)
            newpost = add_to_store.put()
            self.redirect("/blog/" + str(newpost.id()))
        else:
            self.render("/newpost.html", title = title, post = content, error = "Title and Content Please")
            

app = webapp2.WSGIApplication([('/', MainPage),
                               ('/mainpage', MainPage),
                               ("/validatedate", ValidateDate),
                               ("/shoppingcart", ShoppingCart),
                               ("/fizzbuzz", FizzBuzz),
                               ("/signup", SignUp),
                               ("/welcome", Welcome),
                               ("/addcontent", AddContent),
                               ("/rot13cipher", ROT13Cipher),
                               ("/blog", Blog),
                               ("/blog/(\d+)", BlogPost),
                               ("/blog/newpost", NewPost)], debug=True)