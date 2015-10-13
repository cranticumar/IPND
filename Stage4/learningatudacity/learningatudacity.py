import webapp2
import jinja2
import os
import re
import random
import logging
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

while lastconcept and not lastconcept.key.parent() is None:
    areas.insert(0, lastconcept)
    lastconcept = lastconcept.key.parent().get()

if lastconcept:
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
        params['user'] = params.get('user', Handler.CURRENT_USER)
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
        self.render("mainpage.html", templates = self.get_templates(), home=True, user = Handler.CURRENT_USER)

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
                tmp = Concepts(concept = generate_htmlstring(title, concept), title = title, last=True)
                if not prnt is None: 
                    tmp.parent = prnt.key
                    prnt.last=False
                    prnt.put()
                tmp.put()
                self.redirect("/addcontent")
        else:
            self.render("addcontent.html", templates = self.get_templates(), error = "You need right Magic word to add content", contentadd = True)

app = webapp2.WSGIApplication([('/', MainPage),
                               ('/mainpage', MainPage),
                               ("/validatedate", ValidateDate),
                               ("/shoppingcart", ShoppingCart),
                               ("/fizzbuzz", FizzBuzz),
                               ("/addcontent", AddContent),
                               ("/rot13cipher", ROT13Cipher)], debug=True)