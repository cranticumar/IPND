from crypto import *
from google.appengine.ext import ndb
from google.appengine.ext import db

class Posts(ndb.Model):
    post = ndb.TextProperty(indexed = False, required = True)
    user = ndb.StringProperty(indexed = False, required = True)
    posted = ndb.DateTimeProperty(auto_now_add = True, indexed = True)
    last_modified = ndb.DateTimeProperty(auto_now = True)

class Concepts(ndb.Model):
    title = ndb.StringProperty(required = True, repeated = False)
    concept = ndb.TextProperty(indexed = False, required = True)
    created = ndb.DateTimeProperty(auto_now_add = True)
    modified = ndb.DateTimeProperty(auto_now = True)
    last = ndb.BooleanProperty(required = True)

class BlogPosts(ndb.Model):
    title = ndb.StringProperty(required = True, indexed = False)
    blogpost = ndb.TextProperty(required = True, indexed = False)
    posted_on = ndb.DateTimeProperty(auto_now_add = True, indexed = True)
    last_modified = ndb.DateTimeProperty(auto_now = True)

class Users(ndb.Model):
    dispname = ndb.StringProperty(required = True, indexed = False)
    username = ndb.StringProperty(required = True, indexed = True)
    password = ndb.StringProperty(required = True, indexed = False)
    email = ndb.StringProperty(required = False, indexed = False)

    @classmethod
    def get_by_username(cls, usrname):
        return cls.query(cls.username == usrname).get()

    @classmethod
    def register_newuser(cls, disname, usrname, pwd, email = None):
        usr = cls(dispname = disname, username = usrname, password = pwd, email = email)
        usr.put()

    @classmethod
    def login(cls, usrname, pwd):
        usr = cls.get_by_username(usrname)
        if usr and decrypto(pwd, usr.password):
            return usr