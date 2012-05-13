from pkg_resources import resource_filename


class ConverterParent(object):
    def __init__(self, resume):
        self.resume = resume
        self.generated_resume = ''

    def get_resource(self, resource_name):
        return resource_filename('resumebabel.resources', resource_name)

    def preprocess_resume(self):
        pass

    def postprocess_resume(self):
        pass

    def process_resume(self, outputFile):
        self.preprocess_resume()
        self.do_conversion()
        self.postprocess_resume()

        with open(outputFile, "w") as file:
            file.write(self.generated_resume)

    def do_conversion(self):
        raise Exception('Not implemented')
