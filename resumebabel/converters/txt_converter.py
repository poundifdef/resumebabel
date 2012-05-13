from genshi.template import NewTextTemplate, TemplateLoader
import re
from textwrap import TextWrapper

from converter_parent import ConverterParent


class TXTConverter(ConverterParent):
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

   def preprocess_resume(self):
      # TODO: parameterize text formatting features
      self.resume['column_width'] = 40
      self.resume['line_char'] = '*'
      self.resume['bullet'] = '~'

   def do_conversion(self):
      template_filename = self.get_resource('txt_template.txt') 

      loader = TemplateLoader('.')
      templ = loader.load(template_filename, cls=NewTextTemplate)
      stream = templ.generate(**self.resume)

      self.generated_resume = stream.render('text')
      
   def postprocess_resume(self):
      self.generated_resume = self.wrap(self.generated_resume,self.resume['column_width'],self.resume['bullet'])
