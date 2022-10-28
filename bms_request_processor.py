import logging

logger = logging.getLogger

class ResterError(Exception):
	pass

class ResterRequestProcessor(object):
	__instance         = None
	__PENDING_REQUESTS = None
	__PENDING_STATUSES = None

	def __new__(cls, env, client='BMS',  debug = 'False'):
		  if ResterRequestProcessor.__instance is None:
			if env is None:
			     raiseResterError('Env was expected..None was passed in..')
			envString = env.environment()
			ResterRequestProcessor.__instance = Super(ResterRequestProcessor,  cls).__new__(cls)
			ResterRequestProcessor.__instance.__env = env
			ResterRequestProcessor.__PROCESSOR = AmpsRemoteWorkProcessor(
							  amps_name = BMSAmpsName(environment = env_string, client = client, local = True, debug = debug, local = True)
							  msg_size_limit = env.ampsMsgSizeLimit
							  sandra_db = env.instrumentDb
							  cache_path = env.ampsCacheDirectory
								)
			ResterRequestProcessor.__PENDING_REQUESTS  = SandraCache(threshold = 1000, default_timeout = 10*60, sandra_db = env.database,  cache_path = resterCacheDirectory)
			ResterRequestProcessor.__PENDING_STATUSES  = SimpleCache(threshold = 1000, default_timeout = 10*60)

		  return ResterRequestProcessor.__instance

	@property
	def pending_status(self):
	    return ResterRequestProcessor().__PENDING_STATUSES 

	@property
	def pending_request(self):
	    return ResterRequestProcessor().__PENDING_REQUESTS 

	@property
	def env(self):
	    return ResterRequestProcessor().env

	def log_thread(self, msg):
	    logger.info('[tid[{2}] Self {0}, msg: {1}).format(self, msg, threading_current_thread().ident )
			
	def __call__(self, request, time_out_in_second = 0):
	    log_thread(event_source = self, msg = 'Processing Request'.format{0}}
	    data = byteify(request.get_json)
	    if data is None:
	       raise ResterError('No json data is posted ') 
	    requestId = data.get(id, str(uuid.uuid4))
	    json_request = self.__translateRequest(requestId,  data['request'])
	    request_name = data['request']['name']
	    request_descripton = RequestFactory.get_request_description(request_name)
	    proxy = ResterRequestProcessor.__PROCESSOR.createRequestProxy(workRequest = json_read)
	    self._add_request(proxy, request_name)
	    echo_request = request.values.get('echo')
	    ret = {requestId: 'proxy.request_id',
		  status_url: url_for(.processRequestStatus, request_id = proxy.request_id),
		  request: json_request() if echo_request else None}
	    tp = asynchronous.reactor.getThreadPool()
	    asynchronous.reactor.callInThread(self.invoke_processor, proxy)
            if not tp.started:
		tp.start()	 
	    return ret




		

	
