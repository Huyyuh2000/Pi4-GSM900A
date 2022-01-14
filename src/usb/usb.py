import serial
from time import sleep
from src.util.system_info import get_sys_platform

class Usb:
    def __init__(self, baudrate, timeout):
        if (get_sys_platform() == "win32"):
            self.port = 'COM6'
        elif (get_sys_platform() == "linux" | system_info() == "linux2"):
            self.port = '/dev/ttyACM0'
        elif (get_sys_platform() == "darwin"):
            self.port = ''
        self.baudrate = baudrate
        self.timeout = timeout
        self.ser = serial.Serial(self.port, baudrate, timeout=self.timeout)
        self.ser.reset_input_buffer()
        self.encodeFormat = "utf-8"
        self.decodeFormat = "utf-8"

    def send(self, data):
        encodedData = (data + "\r\n").encode(self.encodeFormat)
        print('send: ', encodedData)
        written = self.ser.write(encodedData)
        sleep(1)
        send_receive = self.ser.read_all()
        self.ser.reset_input_buffer()
        send_receive_size = send_receive.__sizeof__()
        response_raw = send_receive[written-1:send_receive_size-1]
        response_string = response_raw.decode(self.decodeFormat)
        response = response_string.split("\r\n")[1]
        return response
        
    def end_text(self):
        self.ser.write(chr(26).encode("utf-8"))

    def receive(self):
        data = self.ser.read_all()
        return data




        
