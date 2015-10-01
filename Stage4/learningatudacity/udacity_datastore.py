from google.appengine.ext import ndb

class Users(ndb.Model):
    uname = ndb.StringProperty(indexed=False, required=True)
    uname_lc = ndb.ComputedProperty(lambda self: self.uname.lower(), indexed=True)
    pwd = ndb.StringProperty(indexed=False, required=True)
    nickname = ndb.StringProperty(indexed=False)
    created = ndb.DateTimeProperty(auto_now_add=True)
    lastlogin = ndb.DateTimeProperty(auto_now = True, indexed=False)
    access = ndb.StringProperty(choices=['admin', 'user'], required=True)

class Posts(ndb.Model):
    post = ndb.StringProperty(indexed=False, repeated=False)
    user = ndb.StructuredProperty(Users)

class Concepts(ndb.Model):
    concept = ndb.JsonProperty(indexed=True)
    created = ndb.DateTimeProperty(auto_now_add=True)
    modified = ndb.DateTimeProperty(auto_now=True)