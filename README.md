# Python_FTP Client and Server modules

The first step is to install the prereq's for the modules using pip

`pip install pyftpdlib`

## FTP Server
The FTP server should now be ready to go out of the box.
Just run the module with

`python FTP_Server.py`

## FTP_Client
Once the server is running, you'll need to open a second terminal.
On the second terminal, navigate to the correct directory run the client with 

`python FTP_Client.py`

Once the client is running you should see the client prompt open with

**FTP>>>**

There are five commands you can run on the client. Below are the commands
with their syntax
- CONNECT \<IP Address\> \<Port Number\>
- LIST
- STORE \<Filename\>
- RETRIEVE \<Filename\>
- QUIT

Please refer to the code for an in depth look at each command
