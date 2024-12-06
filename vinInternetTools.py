#importing python libraries
from socket import create_connection
from time import sleep

# FUNCTIONS
def checkInternetConnection():
    try:
        create_connection(("8.8.8.8", 53), timeout=5)
        return True
    except OSError:
        return False

def waitForInternetConnection(sleepTime=1):
    while True:
        if checkInternetConnection():
            break
        sleep(sleepTime)
