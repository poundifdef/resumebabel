import sys
import json

from resumebabel.converters.resume_to_txt import ResumeText
   
if __name__ == '__main__':
   fd = open(sys.argv[1])
   resume = json.load(fd)

   r = ResumeText(resume)
   r.create_output("out.txt")
