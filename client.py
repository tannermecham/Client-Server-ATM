import sys
import struct
import binascii

# Import socket library
from socket import *

# function definition for main menu options
def mainMenuFunction():
    print("\nPlease make a number selection to continue:")
    print("1.) Check account balance")
    print("2.) Withdraw money")
    print("3.) Deposit money")
    print("4.) Exit banking System")
    print()

print("\nWelcome to the automated banking system.")
continueCondition = True
while(continueCondition):

    # establishes port number if none specified on command line
    if sys.argv.__len__() != 3:
        serverName = 'localhost'
        serverPort = 8675
   
    # Get from command line if specified
    else:
        serverName = sys.argv[1]
        serverPort = int(sys.argv[2])

    # Choose SOCK_STREAM, which is TCP
    clientSocket = socket(AF_INET, SOCK_STREAM)

    # Connect to server using hostname/IP and port
    clientSocket.connect((serverName, serverPort))

    continue_var = 1
    while continue_var == 1:

        # initialize outputString to null
        outputString = ''
        skipOutput = False

        # Prints the main menu options
        mainMenuFunction()

        # gets main menu selection input from user
        selection = input('Selection: ')
        

        if selection == '1':
            selection1 = 'balance'
            outputString = selection1 + "!" + "n"

            # sends the users selection to client
            selection1Bytes = outputString.encode('utf-8')
            clientSocket.send(selection1Bytes)

        elif selection == '2':
            selection2 = 'withdraw'
            withdrawalAmount = input('How much would you like to withdraw? $')
            print()
            outputString = selection2 + "!" + withdrawalAmount

            # sends the users selection to client
            withdrawalBytes = outputString.encode('utf-8')
            clientSocket.send(withdrawalBytes)

        elif selection == '3':
            selection3 = 'deposit'
            depositAmount = input('How much would you like to deposit? $')
            print()
            outputString = selection3 + "!" + depositAmount

            # sends the users selection to client
            depositBytes = outputString.encode('utf-8')
            clientSocket.send(depositBytes)

        elif selection == '4':
            print("Exiting. Goodbye")
            continue_var = 0
            serverBreakStatement = "break!break"
            
            # sends the users selection to client            
            SBSBytes = serverBreakStatement.encode('utf-8')
            clientSocket.send(SBSBytes)
            continueCondition = False
            break

        # protects the program from unexpected user input for menu selection
        else:
            print("Invalid Selection. Please make a different choice.")

            # ensures the client does not wait on a response from server if one is never sent
            skipOutput = True


        # only waits to receive from server if the server has sent something
        if not skipOutput:
            modifiedSentence = clientSocket.recv(1024)
            print('--> From Server: {0}'.format(modifiedSentence.decode('utf-8')) + ' <--')
            break
        
        
    clientSocket.close()
