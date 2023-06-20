# import the ohbot module
import platform
import serial
import serial.tools.list_ports

print ("Python version: " + platform.python_version())
print ("Platform: " + platform.system())

ports = list(serial.tools.list_ports.comports())

def checkPort(p):
    try:
        ser = serial.Serial(p[0], 19200)

        ser.timeout = 0.5
        ser.write_timeout = 0.5
        ser.flushInput()

        msg = "v" + "\n"
        print (f"msg: {msg}")
        ser.write(msg.encode('latin-1'))

        line = ser.readline()
        ser.close()

        subString = "v1".encode('latin-1')

        print (f"line: {line}")

        if line.find(subString) != -1:
            return True
        else:
            return False
    except Exception as ex:
        print (f"Exception: {ex}") 
        return False

for p in ports:
    print (p)
    print (checkPort(p))


