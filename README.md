# Client-Server-ATM
Client - Server ATM

# TO USE:

-- To be run using Python3 --

For funtionality, run both files in separate terminal windows
following the instructions below:

# Server:
	1.) Specify the usage of python3 followed by filename 'server.py'. Optional argument(s) include:
		- port number (integer)
			- EX: 'python3 server.py XXXXX'
				- This will instruct the server to listen on port 'XXXXX'
		
		If no port number is specified, server will default to port 8675.
		Otherwise, server will open and listen on the port number specified by the user (shown above).
	
	2.) Do nothing. Server will run in terminal without interaction from user.
		
# Client:
	1.) Specify the usage of python3 followed by filename 'client.py'. Optional argument(s) include
		- host address (server)
		- port number
			- EX: 'python3 client.py server XXXXX'
				- This will instruct the server to send data to 'server'
				on port 'XXXXX'
				
		If no host is specified, client will default to localhost
		
		If no port number is specified, client will default to 8675
		Otherwise, client will send data to the specified server address at 
		the specified port (shown above).
	
	2.) Follow menu options and instructions on output screen.
	
		Neither main menu nor banking functions can (or will) accept
		negative or decimal values. Any data entered into the server that
		strays from the client-side instructions will not be processed
		and the user will be re-routed back to the menu / instruction page.
