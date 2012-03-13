import sys
import json
from genshi.template import MarkupTemplate, TemplateLoader

class ResumeHTML(object):
   def __init__(self, resume):
      self.resume = resume

   def create_output(self):
      loader = TemplateLoader('.')
      templ = loader.load('ResumeHTMLTemplate.html') 
      stream = templ.generate(**resume)
      print stream.render('xhtml')

if __name__ == '__main__':
   fd = open('resume.json')
   resume = json.load(fd)

   r = ResumeHTML(resume)
   r.create_output()
