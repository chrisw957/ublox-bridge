import serial
import os
import sys

if os.path.exists('/dev/ttyGS0') == False:
    print "ERROR: /dev/ttyGS0 doesn't exist. Made sure g_serial module is loaded,"
    print "       and usb OTG port is connected to a host."
    sys.exit()

s1 = serial.Serial('/dev/ttyGS0', 9600, timeout=0, rtscts=False, dsrdtr=False)
s2 = serial.Serial('/dev/ttymxc3', 9600, timeout=0, rtscts=False, dsrdtr=False)
s1.flushInput()
s1.flushOutput()
s2.flushInput()
s2.flushOutput()

print "Now bridging ttyGS0 to ttymxc3 at 9600 baud..."
print "pretty CTRL-C to stop."

while True:
    bytesAvailable = s1.inWaiting()
    if bytesAvailable > 0:
        inBytes = s1.read(bytesAvailable)
        s1.write(inBytes)
        print "In from ttyGS0: " + str(bytesAvailable)
    
    bytesAvailable = s2.inWaiting()
    if bytesAvailable > 0:
        inBytes = s2.read(bytesAvailable)
        s1.write(inBytes)
        print "In from ttymxc3: " + str(bytesAvailable)


