from genshi.template import NewTextTemplate, TemplateLoader

from converter_parent import ConverterParent

class TEXConverter(ConverterParent):
    def do_conversion(self):
        template_filename = self.get_resource('tex_template.tex')
        loader = TemplateLoader('.')
        templ = loader.load(template_filename, cls=NewTextTemplate)
        stream = templ.generate(**self.resume)

        #TODO: embed .cls file into resume (or output a .zip with both)
        self.generated_resume = stream.render('text')
