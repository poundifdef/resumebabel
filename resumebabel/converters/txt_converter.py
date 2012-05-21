import re
from textwrap import TextWrapper
from copy import deepcopy

from converter_parent import ConverterParent

from jinja2 import Template, PackageLoader, Environment


class TXTConverter(ConverterParent):
   def __init__(self, resume):
      self.column_width = 80
      self.preprocessed = {}
      super(TXTConverter, self).__init__(resume)

   def wrap(self, text):
      wrapper = TextWrapper(width=self.column_width, replace_whitespace=False)
      docSplit = text.splitlines()

      for line_number, line_value in enumerate(docSplit):
          docSplit[line_number] = wrapper.fill(docSplit[line_number].strip())

      return '\n'.join(docSplit)

   def preprocess_resume(self):
       self.preprocessed['resume'] = deepcopy(self.resume)
       self.preprocessed['column_width'] = self.column_width

   def do_conversion(self):
      template_filename = self.get_resource('txt_template.txt') 

      env = Environment(loader=PackageLoader('resumebabel', 'resources'))
      template = env.get_template('txt_template.txt')
      self.generated_resume = template.render(**self.preprocessed)
      
   def postprocess_resume(self):
      self.generated_resume = self.wrap(self.generated_resume)
