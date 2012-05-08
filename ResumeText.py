import sys
import json
from pprint import pprint
from copy import deepcopy
from genshi.template import NewTextTemplate, TemplateLoader

class ResumeText(object):
   def __init__(self, resume):
      self.resume = resume

   def convert_to_tresume(self):
      tresume = deepcopy(self.resume)

      tresume['tresume'] = deepcopy(self.resume)
      return tresume

   def create_output(self):
      r = self.convert_to_tresume()

      templ = NewTextTemplate('''{% include ResumeTextTemplate.txt %}''')
      stream = templ.generate(**r)

      # TODO: output to file? method param for this?
      print stream.render('text')

if __name__ == '__main__':
   fd = open('resume.json')
   resume = json.load(fd)

   r = ResumeText(resume)
   r.create_output()
