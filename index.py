#__author__ = Russ White OR russ.white88@gmail.com

import utils
import landing
import wsgiref.handlers
from google.appengine.ext import webapp
  
class WelcomeHandler(webapp.RequestHandler):

  def get(self):
    #check for session, if session direct to landingpage
    utils.Render(self, 'welcomescreen.html')
    
  def post(self):
    name = self.request.get('name')
    message = self.request.get('message')
    anon = self.request.get('anonymous')
    if not name and anon:
      utils.Render(
        self,
        'welcomescreen.html',
        {'error' : 'Please specify a name, or let us know you would like to be anonymous'})
    else:
      self.redirect('/landing')

class DefaultHandler(webapp.RequestHandler):

  def get(self):
    self.redirect('/welcome')

def main():
  application = webapp.WSGIApplication([
    ('/landing', landing.LandingHnandler),
    ('/resume', resume.ResumeHnandler),
    ('/contact', contact.ContactHandler),
    ('/welcome', welcome.WelcomeHandler),
    ('/', DefaultHandler)],
    debug=True)
  wsgiref.handlers.CGIHandler().run(application)

if __name__ == '__main__':
  main()
