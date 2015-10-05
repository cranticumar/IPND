from google.appengine.ext import ndb

class Posts(ndb.Model):
    post = ndb.StringProperty(indexed=True, repeated=True)
    user = ndb.StringProperty(indexed=False)
    posted_on = ndb.DateTimeProperty(auto_now=True, indexed=True)

class Concepts(ndb.Model):
    concept = ndb.JsonProperty(indexed=True)
    created = ndb.DateTimeProperty(auto_now_add=True)
    modified = ndb.DateTimeProperty(auto_now=True)