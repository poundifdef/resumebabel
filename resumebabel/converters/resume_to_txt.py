import re
from genshi.template import NewTextTemplate, TemplateLoader
from textwrap import TextWrapper

class ResumeText(object):
   def wrap(self, text, column_width=80, bullet='*'):
      docWrapper = TextWrapper(width=column_width, replace_whitespace=False)
      listWrapper = TextWrapper(width=column_width, subsequent_indent='   ', replace_whitespace=False)

      # split document by newlines
      docSplit = text.splitlines()

      # build regular expression to identify list lines
      expression = ""
      reservedChars = ['.', '^', '$', '*', '+', '?', '{', '}', '[', ']', '\\', '|', '(', ')']
      if bullet in reservedChars:
          expression = '.*\{0}[^\{0}]'.format(bullet)
      else:
          expression = '.*{0}[^{0}]'.format(bullet)

      # loop through all lines in the document
      for paragraph in range(len(docSplit)):
          if re.match(expression,docSplit[paragraph]) == None:
              # use standard wrapping if not a list item
              docSplit[paragraph] = docWrapper.fill(docSplit[paragraph])
          else:
              # use list wrapping if a list item
              docSplit[paragraph] = listWrapper.fill(docSplit[paragraph])

      return '\n'.join(docSplit)

   def __init__(self, resume):
      self.resume = resume

   def preprocess_resume(self):
      self.resume['tresume'] = self.resume
      
      # TODO: parameterize text formatting features
      self.resume['column_width'] = 40
      self.resume['line_char'] = '*'
      self.resume['bullet'] = '~'
      return self.resume

   def create_output(self, outputFile = ""):
      self.preprocess_resume()
      
      from pkg_resources import resource_string, resource_listdir, resource_filename

      #print resource_listdir('resumebabel.resources', '')
      template_filename = resource_filename('resumebabel.resources', 'txt_template.txt')
      


      loader = TemplateLoader('.')
      templ = loader.load(template_filename, cls=NewTextTemplate)
      #templ = loader.load('/home/jay/github/resumebabel/resources/txt_template.txt', cls=NewTextTemplate)
      
      #templ = NewTextTemplate('''{% include ../resources/txt_template.txt %}''')
      #templ = NewTextTemplate('''{% include /home/jay/github/resumebabel/resources/txt_template.txt %}''')
      stream = templ.generate(**self.resume)
      self.generatedResume = stream.render('text')
      
      self.postprocess_resume()
     
      if outputFile != "":
        with open(outputFile, "w") as file:
            file.write(self.generatedResume)
        print("Wrote to " + outputFile + " successfully")
      
      #print self.generatedResume
      
   def postprocess_resume(self):
      self.generatedResume = self.wrap(self.generatedResume,self.resume['column_width'],self.resume['bullet'])
