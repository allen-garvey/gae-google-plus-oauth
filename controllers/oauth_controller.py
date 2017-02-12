import webapp2
from controllers.base_controller import BaseController
from secret import oauth_secret

class OauthController(BaseController):
	"""Retrieves data from Google after they are redirected back
	after Oauth login"""

	def get(self):
		secrets = oauth_secret()
		self.response.write("hello from oauth")
		