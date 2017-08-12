from lib.network.protocol.service_protocol import WpaServiceProtocol
from twisted.internet.protocol import Factory

'''
Factory for creating protocol instances to handle WpaService requests.
'''
class WpaServiceFactory(Factory):
	def buildProtocol(self, addr):
		return WpaServiceProtocol()