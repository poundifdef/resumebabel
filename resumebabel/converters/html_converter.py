from copy import deepcopy

from converter_parent import ConverterParent

from jinja2 import Template, PackageLoader, Environment

class HTMLConverter(ConverterParent):
    def __init__(self, resume):
        self.preprocessed = {}
        super(HTMLConverter, self).__init__(resume)

    def preprocess_resume(self):
        # TODO: htmlencode
        # TODO: markdown to html
        self.preprocessed['resume'] = self.resume
        self.preprocessed['hresume'] = deepcopy(self.resume)

        # TODO: Convert json to hresume-specific formats (ie iso date format)
        # self.preprocessed['hresume'] = CONVERT_HRESUME_FORMATS_HERE()

    def do_conversion(self):
        template_filename = self.get_resource('html_template.html')

        env = Environment(loader=PackageLoader('resumebabel', 'resources'))
        template = env.get_template('html_template.html')
        self.generated_resume = template.render(**self.preprocessed)
        # TODO: output to file? method param for this?
