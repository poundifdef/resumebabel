import collections
import json
import os
import sys

class ResumeBabel:
    def __init__(self, resume_json):
        self.resume = json.loads(resume_json, object_pairs_hook=collections.OrderedDict)

    def export_resume(self, output_file, output_format):
        """Export raw data of converted resume"""

        module_name = ('resumebabel.converters.' + output_format + '_converter.' +
                       output_format.upper() + 'Converter')

        resume_converter_class = self._get_class(module_name)

        r = resume_converter_class(self.resume)
        r.process_resume(output_file)

    # http://stackoverflow.com/a/452981/3788
    def _get_class(self, kls):
        parts = kls.split('.')
        module = ".".join(parts[:-1])
        m = __import__(module)
        for comp in parts[1:]:
            m = getattr(m, comp)
        return m
