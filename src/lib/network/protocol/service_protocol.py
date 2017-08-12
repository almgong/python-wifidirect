from twisted.protocols.basic import LineReceiver

'''
Protocol for handling WpaService client requests. Depends on WpaStateMachine
to implement lower level abstractions to perform commands.

This protocol expects to receive exactly one of the following messages:

START_DISCOVERING_PEERS
STOP_DISCOVERING_PEERS
...

The above constants are defined in as class variables, and should be reused
as such.
'''
class WpaServiceProtocol(LineReceiver):
	START_DISCOVERING_PEERS = 0
	STOP_DISCOVERING_PEERS = 1

	def connectionLost(self, reason):
		print "[WpaServiceProtocol]: Connection was lost due to: %s"%(reason)

	def connectionMade(self):
		print "[WpaServiceProtocol]: Connection made!"

	def lineReceived(self, line):
		print "[WpaServiceProtocol]: Received message: %s"%(line)

		try:
			line = int(line)	# converting strings to integers handles leading and trailing spaces
		except ValueError:
			print "[WpaServiceProtocol]: Invalid message: %s, dropping..."%(line)
			return

		if line ==  WpaServiceProtocol.START_DISCOVERING_PEERS:
			print "Start discovering peers!"
		elif line == WpaServiceProtocol.STOP_DISCOVERING_PEERS:
			print "Stop discovering peers..."
		else:
			print "[WpaServiceProtocol]: Invalid message: %s, dropping..."%(line)

