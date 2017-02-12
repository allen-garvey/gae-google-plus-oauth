import webapp2
from controllers.base_controller import BaseController
from secret import oauth_secret

class OauthRedirectController(BaseController):
	"""Redirects user to Google Oauth login"""

	#redirects user to google oauth to login
	def get(self):
		params_dict = oauth_secret()
		google_oauth_url = "https://accounts.google.com/o/oauth2/v2/auth"
		redirect_url = google_oauth_url + self.to_query_string(params_dict)
		#redirect changed to link to prevent site being categorized as phishing
		# self.redirect(redirect_url)
		self.response.write("<h1>Google Oauth Implementation</h1><a href='" + redirect_url + "'>By clicking this link, you agree to share your Google+ email address and name</a>")
		