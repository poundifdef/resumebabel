from copy import deepcopy
from genshi.template import MarkupTemplate, TemplateLoader

from converter_parent import ConverterParent

class HTMLConverter(ConverterParent):
   def preprocess_resume(self):
      # TODO: htmlencode 
      # TODO: markdown to html
      self.hresume = deepcopy(self.resume)

      # TODO: Convert json to hresume-specific formats (ie iso date format)
      self.hresume['hresume'] = deepcopy(self.resume)
      #return hresume

   def do_conversion(self):
      #r = self.convert_to_hresume()

      loader = TemplateLoader('.')
      templ = loader.load(self.get_resource('html_template.html')) 
      stream = templ.generate(**self.hresume)
      #stream = templ.generate(**r)

      # TODO: output to file? method param for this?
      self.generated_resume = stream.render('xhtml')
