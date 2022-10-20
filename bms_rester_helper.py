import sandra
import logging
from App.config import Environment

logger = logging.getLogger(__name__)

class PermissionManager(object):

	def __init__(self, config = None):
		  self.__config = config or Environment()
		
	@staticmethod
	def user():
		  user = Rest.current_user()
		  if user == None:
			    if platform.system() == 'windows':
				  user = sandra.USER
		  return user

	@staticmethod
	def logUserInfo(loginuser):
		try:
			  logger.info(" > %s  %s  %(request.method, request.url)) 
			  if loginuser:
				  logger.info('> User %' %loginuser)
			    login.info('> User-Agent %' %(request.user_agent))
			    login.info('> X-Client timeout:%s', request.header.get('X-Client-timeout', 'Not set'))
		except Exception as e:
			logger.error('Error in authenticating the user '+ str(e))	

	@staticmethod
	@login_required(f):
	@wraps(f)
	def decorated_function(*args, **kwargs):
			user = PermissionManager.currentUser()
			PermissionManager.logUserInfo(user)
				if user is None:
					raise Exception('You are not authorized to access BMS. User id is None')
		    return f(args, kwargs)
	    return decorated_fuction	

		
