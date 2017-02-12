import webapp2
from controllers.base_controller import BaseController
import secret
import state_controller

class OauthRedirectController(BaseController):
	"""Redirects user to Google Oauth login"""

	#redirects user to google oauth to login
	def get(self):
		params_dict = secret.oauth_redirect_params()
		#randomly generate state variable and save it
		state = state_controller.randomly_generate_state()
		state_controller.save_state(state)
		params_dict['state'] = state
		google_oauth_url = "https://accounts.google.com/o/oauth2/v2/auth"
		redirect_url = google_oauth_url + self.to_query_string(params_dict)
		#redirect changed to link to prevent site being categorized as phishing
		# self.redirect(redirect_url)
		self.response.write("<h1>Google Oauth Implementation</h1><a href='" + redirect_url + "'>By clicking this link, you agree to share your Google+ email address and name</a>")
		