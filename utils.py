#__author__ = Russ White OR russ.white88@gmail.com

import os
from google.appengine.ext.webapp import template

def Render(handler, tname='welcomescreen.html', values={}):
  temp = os.path.join(
    os.path.dirname(__file__),
    'templates/' + tname)
  if not os.path.isfile(temp):
    return False
  # Make a copy of the dictionary and add the path
  newval = dict(values)
  newval['path'] = handler.request.path
  outstr = template.render(temp, newval)
  handler.response.out.write(outstr)
  return True
