import sys
import json

from resumebabel.converters.txt_converter import TXTConverter
   
if __name__ == '__main__':
   fd = open(sys.argv[1])
   resume = json.load(fd)

   r = TXTConverter(resume)
   r.create_output("out.txt")
