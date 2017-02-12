import webapp2
from controllers.base_controller import BaseController
from google.appengine.api import urlfetch
import secret
import urllib
import json

class OauthController(BaseController):
	"""Retrieves data from Google after they are redirected back
	after Oauth login"""

	#validates google oauth response and sends request for token
	#then uses token to retrieve google+ information for accout
	def get(self):
		redirect_params = secret.oauth_redirect_params()
		state = self.request.get('state')
		#make sure state matches
		if state != redirect_params['state']:
			#bad request
			self.response.set_status(400)
			self.response.write("State variable does not match")	
			return
		#create payload for POST request to validate response from google
		#and get toke
		authorization_code = self.request.get('code')
		validation_payload = secret.oauth_redirect_validation_params()
		validation_payload['code'] = authorization_code
		headers = {'Content-Type': 'application/x-www-form-urlencoded'}
		
		#post payload, and hopefully retrieve token
		#based on: https://cloud.google.com/appengine/docs/python/issue-requests
		try:
			token_response = urlfetch.fetch(url="https://www.googleapis.com/oauth2/v4/token", 
										payload=urllib.urlencode(validation_payload), 
										method=urlfetch.POST, 
										headers=headers)
			if token_response.status_code != 200:
				self.response.set_status(token_response.status_code)
				self.response.write("Google Oauth validation failed")
				return
		except urlfetch.Error:
			self.response.set_status(500)
			self.response.write("Error connecting to Google Oauth for validation")	
			return
		#response is in json, so parse it
		token_response_content = json.loads(token_response.content)
		#check for token
		if 'access_token' not in token_response_content:
			self.response.set_status(500)
			self.response.write("Error retrieving access token")
			return
		access_token = token_response_content['access_token']
		#get the google+ info
		headers = {'Authorization': 'Bearer ' + access_token}
		try:
			google_plus_response = urlfetch.fetch(url="https://www.googleapis.com/plus/v1/people/me", 
										method=urlfetch.GET, 
										headers=headers)
			if google_plus_response.status_code != 200:
				self.response.set_status(google_plus_response.status_code)
				self.response.write("Failed getting Google+ info")
				return
		except urlfetch.Error:
			self.response.set_status(500)
			self.response.write("Error getting Google+ info")
			return

		google_plus_info = json.loads(google_plus_response.content)
		#check for errors
		if 'error' in google_plus_info:
			self.response.set_status(400)
			self.response.write("Access token for getting Google+ info was invalid")
			return

		#if we are here, we got the google+ info, so print it
		#check if signed up for Google+
		if google_plus_info['isPlusUser'] is False:
			self.response.write('You have not signed up for Google+!')
			return
		#print out first and last name, link to Google+ account, and original state variable
		self.response.write('Your first name is: ' + google_plus_info['name']['givenName'] + '<br>')
		self.response.write('Your last name is: ' + google_plus_info['name']['familyName'] + '<br>')
		self.response.write('The url to your Google+ account is: <a href="' + google_plus_info['url'] + '">'+ google_plus_info['url'] +'</a><br>')
		self.response.write('The original state variable was: ' + state)
