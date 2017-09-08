import os
import sys

from lib.network.service import WpaService

PYTHON_VER = sys.version_info[0]

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
	with open('../.WPA_PATH') as wpaExecPathFile:
		pathArr = wpaExecPathFile.readline().split('=')
		path = None
		if len(pathArr) == 2 and pathArr[0] == 'WPA_EXEC_PATH':
			path = pathArr[1]
		else:
			print("There was an issue with .WPA_PATH. Please check that this file exists and is correct.")
			sys.exit(1)

	os.environ['WPA_EXEC_PATH'] = path
	os.environ['WPA_SERVICE_PORT'] = '9555'

if __name__ == "__main__":
	main()