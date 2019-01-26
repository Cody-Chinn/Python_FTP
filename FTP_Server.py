from pyftpdlib.authorizers import DummyAuthorizer
from pyftpdlib.handlers import FTPHandler
from pyftpdlib.servers import ThreadedFTPServer

def main():
	authorizer = DummyAuthorizer()
	authorizer.add_anonymous('.', perm='elradfmwM')
	handler = FTPHandler
	handler.authorizer = authorizer
	server = ThreadedFTPServer(('127.0.0.1', 1026), handler)
	server.serve_forever()

if __name__ == "__main__":
	main()
