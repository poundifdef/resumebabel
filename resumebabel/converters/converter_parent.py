from pkg_resources import resource_filename


class ConverterParent(object):
    def __init__(self, resume):
        self.resume = resume

    def get_resource(self, resource_name):
        return resource_filename('resumebabel.resources', resource_name)

    def preprocess_resume(self):
        pass

    def do_conversion(self):
        raise Exception('Not implemented')

    def postprocess_resume(self):
        pass

    def process_resume(self, out_fd):
        self.preprocess_resume()
        self.do_conversion()
        self.postprocess_resume()

        out_fd.write(self.generated_resume)
