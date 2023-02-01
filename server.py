import sys
import struct
import binascii
#import socket library
from socket import *

# initializes balance to $100
balance = 100    
continueSelection = 1

print("The server is ready to receive")

#checks to see if withdrawal / deposit amount is a non-integer
def checkInputConstraints(input):
    if input.isdigit():
        return True
    else:
        return False

while(1):

    # establishes port number if none specified on command line
    if sys.argv.__len__() != 2:
        serverPort = 8675

    # Get port number from command line
    else:
        serverPort = int(sys.argv[1])

    # Choose SOCK_STREAM, which is TCP
    # This is a welcome socket
    serverSocket = socket(AF_INET, SOCK_STREAM)

    # The SO_REUSEADDR flag tells the kernel to reuse a local socket
    # in TIME_WAIT state, without waiting for its natural timeout to expire.
    serverSocket.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)

    # Start listening on specified port
    serverSocket.bind(('', serverPort))

    # Listener begins listening
    serverSocket.listen(1)

    
    # Forever, read in sentence, convert to uppercase, and send

    continue_var = 1
    while continue_var == 1:
        # Wait for connection and create a new socket
        # It blocks here waiting for connection
        connectionSocket, addr = serverSocket.accept()
        selection = 0

        # Read bytes from socket
        actionList = connectionSocket.recv(1024)
        mainMenuAction = actionList.decode('utf-8')
        splitActionList = mainMenuAction.split('!')
        selectionString = splitActionList[0]
        amountString = splitActionList[1]

        if 'balance' in mainMenuAction:
            # converts current balance to string and returns to the client
            balanceString = str(balance)
            returnString = "Your current balance is $" + balanceString
            balanceBytes = returnString.encode('utf-8')
            connectionSocket.send(balanceBytes)


        elif 'withdraw' in mainMenuAction:
            if checkInputConstraints(amountString):
                # checks to make sure withdrawal amount does not exceed balance
                if balance >= int(amountString):
                    # withdraws $x from balance
                    balance -= int(amountString)
                    resultString = "$" + amountString + " successfully withdrawn from account. New account balance is $" + str(balance)
                else:
                    resultString = "Withdrawal amount exceeds balance. Unable to withdraw $" + amountString
            else:
                resultString = "Invalid entry. Please enter a positive whole number for withdrawal."
            
            #returns the result of the operation to the client
            resultStringBytes = resultString.encode('utf-8')
            connectionSocket.send(resultStringBytes)



        elif 'deposit' in mainMenuAction:
            # checks to make sure deposit amount is a positive integer
            if checkInputConstraints(amountString):
                balance += int(amountString)
                resultString = "$" + amountString + " successfully deposited in account. New account balance is $" + str(balance)
            else:
                resultString = "Invalid entry. Please enter a positive whole number for deposit."

            #returns the result of the operation to the client
            resultStringBytes = resultString.encode('utf-8')
            connectionSocket.send(resultStringBytes)

        elif 'break' in mainMenuAction:
            continue_var = 0
            break

        else:
            returnString = "complete"
            codedReturnString = returnString.encode('utf-8')
            connectionSocket.send(codedReturnString)

        # break loop to establish new connection
        break

    # Close connection to client but do not close welcome socket
    connectionSocket.close()
