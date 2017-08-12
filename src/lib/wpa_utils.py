import os
import subprocess

'''
Module defining classes and methods to interact with the wpa_supplicant D-Bus. This file 
defines an abstraction for the lower level system calls. Currently uses python-wpa-supplicant.
'''

# Finite state machine that affords interacting with wpa_cli.
# Every method is either a python staticmethod or classmethod to have one runtime
# source-of-truth.
class WpaStateMachine:
	WPA_PATH = None
	CURRENTLY_EXECUTING_CMD = None

	# add more states as needed, but keep STATE_IDLE as it denotes 'readiness' for the ssm
	STATE_IDLE = 0
	STATE_EXECUTING_CMD = 1

	CURRENT_STATE = STATE_IDLE

	def __init__(self):
		raise Exception("No instances of WpaStateMachine should be created! Use class methods instead")

	@classmethod
	def _getWpaPath(cls):
		if not cls.WPA_PATH:
			path = os.environ['WPA_EXEC_PATH']

			if len(path):
				cls.WPA_EXEC_PATH = path
		
		return cls.WPA_EXEC_PATH

	@classmethod
	def _execute(cls, cmd, timeout=60, callback=None):
		'''
		Convenience method to run an arbitrary shell command

		cmd - command string
		timeout - seconds to wait for command to terminate, default 60 seconds
		callback - optional function to act on the stdout and stderr of the command.
							 should be in form: def func(stdout, stderr): <do something>
		'''
		cls.CURRENTLY_EXECUTING_CMD = cmd
		cls.CURRENT_STATE = cls.STATE_EXECUTING_CMD
		proc = subprocess.Popen(cmd, stdout=subprocess.PIPE)

		try:
			stdout, stderr = proc.communicate(timeout)

			if callback:
				callback(stdout, stderr)

		except TimeoutExpired:
			proc.kill()
			outs, errs = proc.communicate()	# wait for proc.kill() to term. process

		# Command has terminated
		cls.CURRENTLY_EXECUTING_CMD = None
		cls.CURRENT_STATE = cls.STATE_IDLE

	# example callback
	@staticmethod
	def testPrint(stdo, stde):
		print stdo

	# TODO: this is an example method that will be replaced with something like: discoverPeers()
	@staticmethod
	def test():
		WpaStateMachine._execute('pwd', callback=WpaStateMachine.testPrint)
