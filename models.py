#__author__ = Russ White OR russ.white88@gmail.com

from google.appengine.ext import ndb

class Visitor(ndb.Model):
  anonymous = ndb.BooleanProperty()
  name = ndb.StringProperty()
  start_date = ndb.DateTimeProperty()

class Feature(ndb.Model):
  enabled = ndb.BooleanProperty()
  name = ndb.StringProperty()

# TODO: resume versioning
# TODO: sessions
# TODO: Messaging
# TODO: Comments
# TODO: Blogging