import os
from factory.service_factory import WpaServiceFactory
from twisted.internet import reactor

'''
Module defining classes and methods for controlling the runtime of
the main WPA service. Local clients should be able to connect to
the appropriate port.

Currently the main WpaService class is a Twisted server listening on port
WPA_SERVICE_PORT (environment var), and uses lib.wpa_utils.WpaStateMachine
to send commands to the wpa_cli.
'''

class WpaService:
	SERVICE_RUNNING = False
	SERVICE_PORT = None

	_REACTOR = None

	class MisconfiguredError(Exception):
		pass

	@classmethod
	def run(cls):
		if not cls.SERVICE_RUNNING:
			cls.SERVICE_PORT = int(os.environ['WPA_SERVICE_PORT'])

			if cls.SERVICE_PORT:
				print "[%s]: WpaService is now running on port %s "%(cls, cls.SERVICE_PORT)

				reactor.listenTCP(cls.SERVICE_PORT, WpaServiceFactory())
				reactor.run()

				cls.SERVICE_RUNNING = True
			else:
				raise MisconfiguredError('Could not retrieve the service port to use.')
		else:
			print "[%s]: WpaService is already running on port %s "%(cls, cls.SERVICE_PORT)

	@classmethod
	def stop(cls):
		cls.SERVICE_PORT = None
		cls.SERVICE_RUNNING = False
		cls._REACTOR = None

		reactor.stop()
