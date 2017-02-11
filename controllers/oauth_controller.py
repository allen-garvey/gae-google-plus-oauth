import webapp2
from controllers.base_controller import BaseController

class OauthController(BaseController):
	"""Retrieves data from Google after they are redirected back
	after Oauth login"""

	def get(self):
		self.response.write("hello from oauth")
		