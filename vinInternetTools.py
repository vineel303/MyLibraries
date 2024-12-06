from socket import create_connection
from time import sleep

def checkInternetConnection():
    try:
        create_connection(("8.8.8.8", 53), timeout=5)
        return True
    except OSError:
        return False

def checkInternetConnection_withWaiting(sleepTime=1): # goes into sleep until an internet connection is established
    while True:
        if checkInternetConnection():
            break
        sleep(sleepTime)
