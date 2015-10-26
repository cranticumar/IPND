from crypto import Crypto
from google.appengine.ext import ndb
from google.appengine.ext import db

class Posts(ndb.Model):
    """
    Posts Kind to store user posts to the website
    """
    post = ndb.TextProperty(indexed = False, required = True)
    user = ndb.StringProperty(indexed = False, required = True)
    posted = ndb.DateTimeProperty(auto_now_add = True, indexed = True)
    last_modified = ndb.DateTimeProperty(auto_now = True)

class Concepts(ndb.Model):
    """
    Concepts kind in datastore to store concepts for users to read
    Users can commit concept to database only if he/she has a magicword
    """
    title = ndb.StringProperty(required = True, repeated = False)
    concept = ndb.TextProperty(indexed = False, required = True)
    created = ndb.DateTimeProperty(auto_now_add = True)
    modified = ndb.DateTimeProperty(auto_now = True)
    last = ndb.BooleanProperty(required = True)

class BlogPosts(ndb.Model):
    """
    BlogPosts kind in datastore to make blog posts to blog portion of website
    """
    title = ndb.StringProperty(required = True, indexed = False)
    blogpost = ndb.TextProperty(required = True, indexed = False)
    posted_on = ndb.DateTimeProperty(auto_now_add = True, indexed = True)
    last_modified = ndb.DateTimeProperty(auto_now = True)

class Users(ndb.Model):
    """
    Users Kind in datastore to store user credentials and details
    """
    dispname = ndb.StringProperty(required = True, indexed = False)
    username = ndb.StringProperty(required = True, indexed = True)
    password = ndb.StringProperty(required = True, indexed = False)
    email = ndb.StringProperty(required = False, indexed = False)

    @classmethod
    def get_by_username(cls, usrname):
        # queries and get user entity by username (encrypted)
        return cls.query(cls.username == usrname).get()

    @classmethod
    def register_newuser(cls, disname, usrname, pwd, email = None):
        # creates a new user entity and commits to database
        usr = cls(dispname = disname, username = usrname, password = pwd, email = email)
        usr.put()

    @classmethod
    def login(cls, usrname, pwd):
        # helps validating if user entity already exists
        usr = cls.get_by_username(usrname)
        if usr and Crypto.decrypto(pwd, usr.password):
            return usr