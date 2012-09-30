from copy import deepcopy
import markdown2

from converter_parent import ConverterParent

from jinja2 import Template, PackageLoader, Environment

class HTMLConverter(ConverterParent):
    def __init__(self, resume):
        self.preprocessed = {}
        super(HTMLConverter, self).__init__(resume)

    def preprocess_resume(self):
        # TODO: markdown to html for more that description?
        self.preprocessed['resume'] = deepcopy(self.resume)

        for experience_title, experiences in self.preprocessed['resume']['experiences'].iteritems():
            for experience in experiences:
                if experience.get('description'):
                    experience['description'] = markdown2.markdown(experience['description'])

    def do_conversion(self):
        template_filename = self.get_resource('html_template.html')

        env = Environment(loader=PackageLoader('resumebabel', 'resources'))
        template = env.get_template('html_template.html')
        self.generated_resume = template.render(**self.preprocessed)
