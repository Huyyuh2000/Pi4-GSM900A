import serial
from time import sleep
from System_Info import GET_FLATFORM

class USB:
    def __init__(self, baudrate, timeout):
        if (GET_FLATFORM() == "win32"):
            self.port = 'COM6'
        elif (GET_FLATFORM() == "linux" | GET_FLATFORM() == "linux2"):
            self.port = '/dev/ttyACM0'
        elif (GET_FLATFORM() == "darwin"):
            self.port = ''
        self.baudrate = baudrate
        self.timeout = timeout
        self.phonenumber = "+84903631936"
        self.ser = serial.Serial(self.port, baudrate, timeout=self.timeout)
        self.ser.reset_input_buffer()
        self.encodeFormat = "utf-8"
        self.decodeFormat = "utf-8"
    def send(self, data):
        encodedData = (data + "\r\n").encode(self.encodeFormat)
        print('send: ', encodedData)
        written = self.ser.write(encodedData)
        sleep(1)
        sendandreceive = self.ser.read_all()
        sendandreceive_size = sendandreceive.__sizeof__()
        response_raw = sendandreceive[written-1:sendandreceive_size-1]
        response_string = response_raw.decode(self.decodeFormat)
        response = response_string.split("\r\n")[1]
        return response

        
    def endText(self):
        self.ser.write(chr(26).encode("utf-8"))
    def receive(self):
        data = self.ser.read_all()
        return data




        
