import flask
import sandra
from project.config                   import Environment
from project.bms_request_processor    import ResterRequestProcessor, ResterError
from project.bms_rester_helper        import user, PermissionManager

Environment = Environment()

BMS_REQUEST_PROCESSOR = ResterRequestProcessor(Environment, client = 'BMS')

roleMapping = {'Admin'   :['addMember',  'updateMember',   'viewMember',  'removeMember',   'addBooks',  'updateBooks', 'removeBooks],
	       'Member'  :['deleteOwnAccount',  'viewBooks',  'borrowBooks',  'returnBooks']}

def config(env):
    cobDetails = cobInfo()
    return default.data(env = env, **cobDetails)

class BMSResterAPI():

	SERVICE_MAP = {['service':  'bms_rester_api',
                        'path':  'App.bms_rester_api',
                        'url': '/',
                        'description' : 'Book Management System (BMS) RESTer  Service'
                       ]}

	def __init__(self):
	    pass

	@bms_rester_api.route('/viewBooks/<string:env>, methods = ['GET'])
	@PermissionManager.login_required
	def viewBooks(env):
      	    if 'viewBooks' in roleMapping[user['Type']] :		
               with sandra.connect(env) as db:
                  bkDict = db.read(bookDict)	
                  return Rest.response(bkDict)

	@bms_rester_api.route('/addBooks/<string:env><dict:newBookInfo>, methods = ['GET',  'POST'])
	@PermissionManager.login_required
	def addBooks(env, newBookInfo):
            if 'addBooks' in roleMapping[user['Type']] :	
                with sandra.connect(env) as db:
                   bkDict = db.read(bkDict)
                   bk = newBookInfo['Book']
                   bkDict['bk'] = newBookInfo
                   db.write(bkDict)			
	           return Rest.response(bkDict)

	@bms_rester_api.route('/updateBooks/<string:env><string:book>, methods = ['GET',  'POST'])
	@PermissionManager.login_required
	def updateBooks(env, bookInfo):
       	    if 'updateBooks' in roleMapping[user['Type']] :				
            	with sandra.connect(env) as db:
                   bkDict = db.read(bkDict)
                   bk = bookInfo['Book']
                   bkDict['bk'] = bookInfo
                   db.write(bkDict)			
	           return Rest.response(bkDict)

	@bms_rester_api.route('/removeBooks/<string:env><string:book>, methods = ['GET',  'POST',  'DELETE'])
	@PermissionManager.login_required
	def removeBooks(env, book):
            if 'removeBook' in roleMapping[user['Type']] : 		
            	with sandra.connect(env) as db:
             	   bkDict = db.read(bkDict)
                   del bkDict['book']
                   db.write(bkDict)			
                   return Rest.response(bkDict)
	
	@bms_rester_api.route('/borrowBooks/<string:env><string:book>, methods = ['GET',  'POST'])
	@PermissionManager.login_required
	def borrowBooks(env, book):
            if 'borrowBooks' in roleMapping[user['Type']] :
                with sandra.connect(env) as db:
                   bkDict = db.read(bkDict)
                   bk = updateBookInfo['book']
                   bkDict[bk]['Status] = 'BORROWED'
                   db.write(bkDict)			
                   return Rest.response(bkDict)

	@bms_rester_api.route('/returnBooks/<string:env>, methods = ['GET',  'POST'])
	@PermissionManager.login_required
	def returnBooks(env):
            if 'returnBooks' in roleMapping[user['Type']] :
                with sandra.connect(env) as db:
                   bkDict = db.read(bkDict)
                   bk = updateBookInfo['book']
                   bkDict[bk]['Status] = 'AVAILABLE'
                   db.write(bkDict)			
                   return Rest.response(bkDict)

	@bms_rester_api.route('/viewMember/<string:env>, methods = ['GET'])
	@PermissionManager.login_required
	def viewMember(env):
            if 'viewMember' in roleMapping[user['Type']] :	
                with sandra.connect(env) as db:
                   memDict = db.read(memberDict)
                   return Rest.response(memDict)

	@bms_rester_api.route('/addMembers/<string:env><dict:addMembers>, methods = ['GET',  'POST'])
	@PermissionManager.login_required
	def addMembers(env, newMemberInfo):
            if 'addMember' in roleMapping[user['Type']] :	
                with sandra.connect(env) as db:
                   memDict = db.read(memberDict)
                   member = newMemberInfo['Member']
                   memDict['member'] = newMemberInfo
                   db.write(memDict)
	           return Rest.response(memDict)

	@bms_rester_api.route('/updateMembers/<string:env><dict:memberInfo>, methods = ['GET',  'POST'])
	@PermissionManager.login_required
	def updateMembers(env, memberInfo):
	    if 'updateMember' in roleMapping[user['Type']] :	
                with sandra.connect(env) as db:
	           memDict = db.read(memberDict)
		   member = memberInfo['Member']
		   memDict['member'] = newMemberInfo
		   db.write(memDict)
	           return Rest.response(memDict)

	@bms_rester_api.route('/removeMember/<string:env><string:member>, methods = ['GET',  'POST',  'DELETE'])
	@PermissionManager.login_required
	def removeMember(env, member):
       	    if 'removeMember' in roleMapping[user['Type']] :					
            	with sandra.connect(env) as db:
                    memDict = db.read(memberDict)
                    del memDict['member']
                    db.write(memDict)
                    return Rest.response(memDict)

	@bms_rester_api.route('/deleteOwnAccount/<string:env>, methods = ['GET',  'POST',  'DELETE'])
	@PermissionManager.login_required
	def deleteOwnAccount(env):
            if 'deleteOwnAccount' in roleMapping[user['Type']] :	
            	with sandra.connect(env) as db:
                    memDict = db.read(memberDict)
		    member = user['Id']
		    del memDict['member']
		    db.write(memDict)
	            return Rest.response(memDict)

	@route('/bms_login', method =['POST'])
	def validateLogin():
	    isValid = validateBMSLogin(request.json.get('UserName'), request.json.get('Password'))
	    return Rest.response(rest.toJson(isValid))

	@bms_rester_api.error_handler(ResterError)
	def resterErrorHandler(err):
	    return error_handler(err)

	@bms_rester_api.error_handler(exception)
	def unhandledErrorHandler(err):
	    return unhandled_error_handler(err)

	@bms_rester_api.route(/envConfig, methods = ['GET', 'POST'])
	@PermissionManager.login_required
	def envConfig():
	    return Rest.response(config(Environment))
		
