#__author__ = Russ White OR russ.white88@gmail.com

from google.appengine.ext import webapp

class LandingHandler(webapp.RequestHandler):

  def get(self):
    #check for session, if session direct to customized landingpage
    utils.Render(self, 'landing.html', {})
    #if no session redirect back to welcome to create a session
    utils.Render(self, 'landing.html', {})
    
  def post(self):
    #post options here
