import sys
import json
from pprint import pprint
from copy import deepcopy
from genshi.template import NewTextTemplate, TemplateLoader

class ResumeLaTeX(object):
   def __init__(self, resume):
      self.resume = resume

   def preprocess_resume(self):
      self.resume['ltxresume'] = self.resume
      
      # TODO: parameterize text formatting features
      return self.resume

   def create_output(self, outputFile = ""):
      self.preprocess_resume()
      
      templ = NewTextTemplate('''{% include ResumeLaTeXTemplate.txt %}''')
      stream = templ.generate(**self.resume)
      self.generatedResume = stream.render('text')
      
      self.postprocess_resume()
     
      if outputFile != "":
        with open(outputFile, "w") as file:
            file.write(self.generatedResume)
        print("Wrote to " + outputFile + " successfully")
      
      print self.generatedResume
      
   def postprocess_resume(self):
      return
   
if __name__ == '__main__':
   fd = open('resume.json')
   resume = json.load(fd)

   r = ResumeLaTeX(resume)
   r.create_output("out.tex")