import sys
import json
from genshi.template import MarkupTemplate

class ResumeHTML(object):
	def __init__(self, resume):
		self.resume = resume

	def create_output(self):
		templ = MarkupTemplate('<h1>Hello, $fname</h1>')
		stream = templ.generate(**resume)
		print stream
		print stream.render('xhtml')
		print 'hello world'

if __name__ == '__main__':
	fd = open('resume.json')
	resume = json.load(fd)

	r = ResumeHTML(resume)
	r.create_output()
