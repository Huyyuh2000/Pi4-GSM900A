from RaspberryPi4.Usb.Usb import USB
import sys

class SIM900A:
    def __init__(self, phonenumber, mode, data):
        self.USB = USB("9600",1)
        self.sendmess = b"AT+CMGF=1"
        self.readmess = b"AT+CNMI=2,2,0,0,0"
        self.phonenumber = bytearray(phonenumber)
        self.mode =mode
        self.data = data

        if (self.mode == "Send Message"):
            self.SendMess(self.data)
    def SendMess(self, data):
        self.USB.Send(self.sendmess, None)
        feedback_1 = self.Receive()
        while (feedback_1 == b""):
            print("timeout config send message mode")
            self.USB.Send(self.sendmess, None)
            feedback_1 = self.Receive()
        if (feedback_1 == b"OK"):
            self.USB.Send(b"AT+CMGS"+self.phonenumber)
            feedback_2 = self.Receive()
            while (feedback_2 == b""):
                print("timeout config number")
                self.USB.Send(b"AT+CMGS"+self.phonenumber)
                feedback_2 = self.Receive()
            if (feedback_2 == b"OK"):
                self.USB.Send(data)
                self.USB.Send(b"0x1A")
                feedback_3 = self.Receive()
                while (feedback_3 != b"OK"):
                    print("timeout config finish text")
                    self.USB.Send(b"0x1A")
                    time.sleep(1)
                print("finish send message")
            else:
                print(feedback_2)
        else:
            print(feedback_1)
        

if __name__ == '__main__':
    SIM900A(sys.argv[1], sys.argv[2], sys.argv[3])