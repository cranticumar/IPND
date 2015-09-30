﻿import webapp2
import jinja2
import os
import random
from udacity_datastore import Concepts
from google.appengine.ext import ndb
from date_validation import validate_date

templates_dir = os.path.join(os.path.dirname(__file__), "templates")
concepts_dir = os.path.join(os.path.dirname(__file__), "concepts")
jinja_env = jinja2.Environment(loader = jinja2.FileSystemLoader(templates_dir),
                               autoescape = "true")

areas = list()
for each in os.walk(concepts_dir):
    for concept in each[2]:
        if os.path.splitext(concept)[1] == '.txt':
            fh = open(os.path.join(each[0], concept))
            fcontent = fh.read()
            fh.close()
            t_c_tup = (os.path.splitext(concept)[0].replace('_','.'), fcontent)
            records_count = Concepts.query().filter(Concepts.concept == {t_c_tup[0] : t_c_tup[1]}).count()
            if records_count == 0:
                tmp = Concepts(concept = {t_c_tup[0] : t_c_tup[1]})
                tmp.put()
            elif records_count > 1:
                tmp = Concepts.query(Concepts.concept == {t_c_tup[0] : t_c_tup[1]}).get()
                tmp.key.delete()



for each in Concepts.query():
    if not each.concept.items()[0] in areas:
        areas.append(each.concept.items()[0])

areas.sort()
user = random.choice([None, 'kranthi', 'kranthi'])

class Handler(webapp2.RequestHandler):
    """WEBAPP2 Request Handler inherited class"""
    def write(self, *a, **kw):
        """Writes Responses to the screen"""
        self.response.write(*a, **kw)

    def render_str(self, template, **params):
        """renders template with provided params"""
        t = jinja_env.get_template(template)
        params['areas'] = params.get('areas', areas)
        params['user'] = params.get('user', user)
        return t.render(params)

    def render(self, template, **kw):
        """writes render template to screen"""
        print kw.get('templates')
        self.write(self.render_str(template, **kw))

    def get_templates(self):
        """Generates templates dynamically using subclassess"""
        return [kls.__name__ for kls in Handler.__subclasses__()]

class MainPage(Handler):
    def get(self):
        self.render("mainpage.html", templates = self.get_templates(), home=True)

    def post(self):
        content = self.request.get("comment")
        user = self.get_currentuser()
        if user:
            self.render("contentfeedback.html",
                        templates = self.get_templates(),
                        content = content,
                        user = user,
                        message = user + " logged in")
        else:
            self.render("contentfeedback.html",
                        templates = self.get_templates(),
                        content = content,
                        user = user,
                        message = "login to post comments")

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

class Admin(Handler):
    def get(self):
        self.render("admin.html", templates = self.get_templates())

app = webapp2.WSGIApplication([('/', MainPage),
                               ('/mainpage', MainPage),
                               ("/validatedate", ValidateDate),
                               ("/shoppingcart", ShoppingCart),
                               ("/fizzbuzz", FizzBuzz),
                               ("/admin", Admin)], debug=True)