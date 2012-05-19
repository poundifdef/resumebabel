from genshi.template import NewTextTemplate, TemplateLoader
import re
from textwrap import TextWrapper

from converter_parent import ConverterParent


class TXTConverter(ConverterParent):
   def wrap(self, text, column_width=80, bullet='-'):
      docWrapper = TextWrapper(width=column_width, replace_whitespace=False)
      listWrapper = TextWrapper(width=column_width, subsequent_indent='   ', replace_whitespace=False)

      docSplit = text.splitlines()

      for line_number, line_value in enumerate(docSplit):
          if line_value.strip().startswith(bullet):
              # does this line start with a bullet point? If so, do hanging indent
              docSplit[line_number] = ' ' + listWrapper.fill(docSplit[line_number].strip())
          else:
              docSplit[line_number] = docWrapper.fill(docSplit[line_number])

      return '\n'.join(docSplit)

   def preprocess_resume(self):
       # TODO: calculate line lengths (ie '======') for headings
       pass

   def do_conversion(self):
      template_filename = self.get_resource('txt_template.txt') 

      loader = TemplateLoader('.')
      templ = loader.load(template_filename, cls=NewTextTemplate)
      stream = templ.generate(**self.resume)

      self.generated_resume = stream.render('text')
      
   def postprocess_resume(self):
      self.generated_resume = self.wrap(self.generated_resume)
