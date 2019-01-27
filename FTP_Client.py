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
	try:
		ftp.storbinary('STOR ' + filename, open(filename, 'rb'))
		print('Successfully uploaded ' + filename)
	except:
		print('That didn\'t work, please try another file')

def retrieve(filename):
	try:
		localfile = open(filename, 'wb')
		ftp.retrbinary('RETR ' + filename, localfile.write, 1024)
		localfile.close()
		print('Successfully downloaded ' + filename)
	except:
		print('Cannot find ' + filename + ' on the FTP server')

def prompt():
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

	elif 'STORE' in cmd:
		cmdList = cmd.split()
		if len(cmdList) == 2:
			store(cmdList[1])
			prompt()
		else:
			print('STORE takes one parameter- The file you would like to upload')
			prompt()

	elif 'RETRIEVE' in cmd:
		cmdList = cmd.split()
		if len(cmdList) == 2:
			retrieve(cmdList[1])
			prompt()
		else:
			print('RETRIEVE takes exactly one parameter- The file you would like to download')
			prompt()

	elif 'QUIT':
		ftp.quit()
	else:
		print('Valid commands are CONNECT, LIST, RETRIEVE and STORE')
		prompt()


if __name__ == '__main__':
	print('Python FTP Client is up and running, \nPlease use CONNECT to connect to the FTP server')
	prompt()
