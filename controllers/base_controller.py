import webapp2
import json

#base controller class
class BaseController(webapp2.RequestHandler):

	#convenience method for writing json response
	def write_json(self, json_string):
		self.response.content_type = 'application/json'
		self.response.write(json_string)

	#converts params dictionary into query string
	#assumes all strings are already correctly uri encoded
	#based on: http://stackoverflow.com/questions/12229064/mapping-over-values-in-a-python-dictionary
	def to_query_string(self, params_dict):
		return "?" + "&".join(map(lambda (k,v): k + "=" + v, params_dict.iteritems()))
