import os
import sys

from lib.network.service import WpaService

COMMANDS_FILE_PATH = 'commands.json'
PYTHON_VER = sys.version_info[0]

commands = {}

'''
Main driver function that is used to start the wpa service.
'''
def main():
	loadEnvironmentVariables() # TODO: refactor so that environment variables are loaded elsewhere!
	WpaService.run()
	

def loadEnvironmentVariables():
	'''
	Temporary manner of loading environment variables until we use something
	like docker.
	'''
	os.environ['WPA_EXEC_PATH'] = '/linux_wifidirect/src/wpa/wpa_supplicant-2.6/wpa_supplicant'
	os.environ['WPA_SERVICE_PORT'] = '9555'

if __name__ == "__main__":
	main()