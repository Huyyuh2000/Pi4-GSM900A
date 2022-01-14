from src.usb.usb import Usb
import sys
from time import sleep

class Sim900a:
    def __init__(self):
        self.Usb = Usb("9600",0)
        self.handshake = "AT"
        self.message_mode = "AT+CMGF=1"
        self.phone_number = "AT+CMGS=\"+84903631936\""

    def send_message(self, target, content):
        """ Send message to target
        send_message will:
        - Validate phone number and add country prefix (currently hardcoded +84)
        - Send content to target phone number
        """
        phone_number = self.validate_phone_number(target)


        response = self.Usb.send(self.handshake)
        if (response == "Error"):
            response = self.Usb.send(self.handshake)
            print("Error, Resend handshake")
        else: print("Response: ",response)
    
        response = self.Usb.send(self.message_mode)
        if (response == "Error"):
            response = self.Usb.send(self.message_mode)
            print("Error, Resend set message mode")
        else: print("Response: ",response)

        response = self.Usb.send(self.phone_number)
        if (response == "Error"):
            response = self.Usb.send(self.phone_number)
            print("Error, Resend phone number")
        else: print("Response: ",response)

        self.Usb.send(content)
        self.Usb.end_text()

    def validate_phone_number(self, phone_number):
        return