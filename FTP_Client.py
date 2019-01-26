from ftplib import FTP

ftp = FTP ('')
ftp.connect('localhost',1026)
ftp.login()

# cwd is Change working directory, 
# for windows this may need to be c:\
ftp.cwd('.')
ftp.retrlines('LIST')

def uploadFile():
	filename = 'testfile.txt'
	ftp.storbinary('STOR ' + filename, open(filename, 'rb'))
	#ftp.quit()

def downloadFile():
	filename = 'testfile.txt'
	localfile = open(filename, 'wb')
	ftp.retrbinary('RETR ' + filename, localfile.write, 1024)
	#ftp.quit()
	localfile.close()

uploadFile()
#downloadFile()

