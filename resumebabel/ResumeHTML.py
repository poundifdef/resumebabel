import sys
import json
from pprint import pprint
from copy import deepcopy
from genshi.template import MarkupTemplate, TemplateLoader

class ResumeHTML(object):
   def __init__(self, resume):
      self.resume = resume

   def convert_to_hresume(self):
      # TODO: htmlencode 
      # TODO: markdown to html
      hresume = deepcopy(self.resume)

      # TODO: Convert json to hresume-specific formats (ie iso date format)
      hresume['hresume'] = deepcopy(self.resume)
      return hresume

   def create_output(self):
      r = self.convert_to_hresume()

      loader = TemplateLoader('.')
      templ = loader.load('ResumeHTMLTemplate.html') 
      stream = templ.generate(**r)

      # TODO: output to file? method param for this?
      print stream.render('xhtml')

if __name__ == '__main__':
   fd = open('resume.json')
   resume = json.load(fd)

   r = ResumeHTML(resume)
   r.create_output()
