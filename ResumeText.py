import sys
import json
from pprint import pprint
from copy import deepcopy
from genshi.template import NewTextTemplate, TemplateLoader

<<<<<<< HEAD
def wrap(text, width=80):
    # Thanks Dominick Saputo! http://code.activestate.com/recipes/148061-one-liner-word-wrap-function/
    lines = []
    for paragraph in text.split('\n'):
        line = []
        len_line = 0
        for word in paragraph.split(' '):
            len_word = len(word)
            if len_line + len_word <= width:
                line.append(word)
                len_line += len_word + 1
            else:
                lines.append(' '.join(line))
                line = [word]
                len_line = len_word + 1
        lines.append(' '.join(line))
    return '\n'.join(lines)

=======
>>>>>>> f91433fdac69a165113ef80d9ce10cbe7ef9fc68
class ResumeText(object):
   def __init__(self, resume):
      self.resume = resume

<<<<<<< HEAD
   def preprocess_resume(self):
      self.resume['tresume'] = self.resume
      
      # TODO: parameterize text formatting features
      self.resume['max_columns'] = 40
      self.resume['line_char'] = '*'
      return self.resume

   def create_output(self, outputFile = ""):
      self.preprocess_resume()
      
      templ = NewTextTemplate('''{% include ResumeTextTemplate.txt %}''')
      stream = templ.generate(**self.resume)
      self.generatedResume = stream.render('text')
      
      self.postprocess_resume()
     
      if outputFile != "":
        with open(outputFile, "w") as file:
            file.write(self.generatedResume)
        print("Wrote to " + outputFile + " successfully")
      
      print self.generatedResume
      
   def postprocess_resume(self):
      self.generatedResume = wrap(self.generatedResume,resume['max_columns'])  
   
=======
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

>>>>>>> f91433fdac69a165113ef80d9ce10cbe7ef9fc68
if __name__ == '__main__':
   fd = open('resume.json')
   resume = json.load(fd)

   r = ResumeText(resume)
<<<<<<< HEAD
   r.create_output("out.txt")
=======
   r.create_output()
>>>>>>> f91433fdac69a165113ef80d9ce10cbe7ef9fc68
