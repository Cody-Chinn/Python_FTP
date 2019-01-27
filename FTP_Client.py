from ftplib import FTP

ftp = FTP('')

def connect(ip, port):
	try:
		ftp.connect(ip, int(port))
		ftp.login()
		print('You\'re connected to ' + str(ip) + ' on port ' + port)
		prompt()
	except:
		print('That didn\'t work, please try another server')
		prompt()

def store(filename):
	# filename = 'testfile.txt'
	ftp.storbinary('STOR ' + filename, open(filename, 'rb'))

def retrieve(filename):
	# filename = 'testfile.txt'
	localfile = open(filename, 'wb')
	ftp.retrbinary('RETR ' + filename, localfile.write, 1024)
	localfile.close()

def prompt():
	global ftp
	
	cmd = input('\nFTP>>> ')
	
	if 'CONNECT' in cmd:
		cmdList = cmd.split()
		if len(cmdList) == 3:
			connect(cmdList[1], cmdList[2])
			cmdList = []
		else:
			print('CONNECT takes two parameters. IP and port number')
			prompt()

	elif 'LIST' in cmd:
		ftp.retrlines('LIST')
		prompt()

	elif 'QUIT':
		ftp.quit()
	else:
		print('Valid commands are CONNECT, LIST, RETRIEVE and STORE')
		prompt()


if __name__ == '__main__':
	print('Python FTP Client is up and running, \nPlease use CONNECT to connect to the FTP server')
	prompt()

	'''
	try:
		# ftp.connect('localhost', 1026)
		ftp.connect(ip, int(port))
		ftp.login()

		# cwd is Change working directory, 
		# this sets it to the current directory
		ftp.cwd('.')
		
		print('\nYour in! What would you like to do?')
		ftp.retrlines('LIST')
	'''

	
	#ftp.retrlines('LIST')
