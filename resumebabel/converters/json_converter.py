import json
from converter_parent import ConverterParent


class JSONConverter(ConverterParent):
    def do_conversion(self):
        self.generated_resume = json.dumps(self.resume, indent=4)
