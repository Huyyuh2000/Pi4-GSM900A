from Usb import USB
import sys
from time import sleep

class SIM900A:
    def __init__(self, data):
        self.USB = USB("9600",0)
        
        self.handshake = "AT"
        self.sendmessagemode = "AT+CMGF=1"
        self.phonenumber = "AT+CMGS=\"+84903631936\""
        self.data = data

        self.SendMess(self.data)
    def SendMess(self, data):
        #Handshake
        response = self.USB.send(self.handshake)
        if (response == "Error"):
            response = self.USB.send(self.handshake)
            print("Error, Resend handshake")
        else: print("Response: ",response)
    
        response = self.USB.send(self.sendmessagemode)
        if (response == "Error"):
            response = self.USB.send(self.handshake)
            print("Error, Resend set message mode")
        else: print("Response: ",response)

        response = self.USB.send(self.phonenumber)
        if (response == "Error"):
            response = self.USB.send(self.handshake)
            print("Error, Resend phone number")
        else: print("Response: ",response)

        self.USB.send(data)
        self.USB.endText()

if __name__ == '__main__':
    SIM900A(sys.argv[1])