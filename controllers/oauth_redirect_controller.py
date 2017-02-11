import webapp2
from controllers.base_controller import BaseController
from secret import oauth_secret

class OauthRedirectController(BaseController):
	"""Redirects user to Google Oauth login"""

	#redirects user to google oauth to login
	def get(self):
		params_dict = oauth_secret()
		google_oauth_url = "https://accounts.google.com/o/oauth2/v2/auth"
		self.redirect(google_oauth_url + self.to_query_string(params_dict))
		