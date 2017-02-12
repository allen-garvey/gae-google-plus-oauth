#functions for saving and getting value of state variable
#in memcache
from google.appengine.api import memcache
from random import randint

#generates a new random state variable
def randomly_generate_state():
	return "hunter" + str(randint(2, 5000))

#returns memcache state variable key
def state_variable_key():
	return "state_variable_key"

#returns state variable from memcache
#returns None if nothing is saved
def get_state():
	return memcache.get(state_variable_key())

#saves state variable in memcache
def save_state(state):
	#delete key, if exists
	memcache.delete(key=state_variable_key())
	#state expires in 5 minutes
	expiration = 60 * 5
	memcache.add(key=state_variable_key(), value=state, time=expiration)