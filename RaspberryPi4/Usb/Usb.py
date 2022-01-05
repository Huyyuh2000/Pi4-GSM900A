import serial

class USB:
    def __init__(self, baudrate, timeout):
        self.port = '/dev/ttyACM0'
        self.baudrate = baudrate
        self.timeout = timeout
        self.ser = serial.Serial(self.port, baudrate, timeout=self.timeout)
        self.ser.reset_input_buffer()
    def Send(data, datatype):
        if (datatype == None):
            encode = "utf-8"
            decode = "utf-8"
        else:
            encode = datatype
            decode = datatype
        self.ser.write(bytearray(data+"\r"+"\n").encode(encode))
        line = ser.readline().decode(decode).rstrip()
        print(line)
        time.sleep(1)
    def Receive():
        data = self.ser.readString()
        return data



        
