import sys

class HelloWorld:
    def __init__(self, str1, str2):
        self.str1 = str1
        self.str2 = str2
        self.printString()
    def printString(self):
        print("HelloWorld" + " " + self.str2)

if __name__ == '__main__':
    HelloWorld(sys.argv[1], sys.argv[2])