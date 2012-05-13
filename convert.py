import json
import os
import sys


# http://stackoverflow.com/a/452981/3788
def get_class(kls):
    parts = kls.split('.')
    module = ".".join(parts[:-1])
    m = __import__(module)
    for comp in parts[1:]:
        m = getattr(m, comp)
    return m

if __name__ == '__main__':
    input_json = sys.argv[1]
    output_file = sys.argv[2]
    output_format = (os.path.splitext(output_file)[1])[1:]

    # TODO: make sure output_format is not empty

    module_name = ('resumebabel.converters.' + output_format + '_converter.' +
                   output_format.upper() + 'Converter')

    resume_converter_class = get_class(module_name)

    fd = open(input_json)
    resume = json.load(fd)

    r = resume_converter_class(resume)
    r.create_output("out.txt")
