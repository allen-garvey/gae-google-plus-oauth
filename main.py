#!/usr/bin/env python

import webapp2
from controllers.oauth_controller import OauthController
from controllers.oauth_redirect_controller import OauthRedirectController

app = webapp2.WSGIApplication([
    ('/', OauthRedirectController),
    ('/oauth/?', OauthController)
], debug=True)
