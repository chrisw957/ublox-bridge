# ublox-bridge
Bridge ublox to usb serial gadget port

## Install requirements
<pre>
$ sudo apt-get install python
$ sudo apt-get install python-serial
</pre>

## Load the Serial Gadget module
<pre>
$ sudo modprobe g_serial
</pre>
You should now have a new serial port: /dev/ttyGS0

## Connect OTG Port
Connect the OTG port (J67) of the Nitrogen, to your PC.  The PC should discover a new serial port such as COM4.

## Run the Bridge utility
<pre>
$ cd ~/ublox-bridge
$ python ./bridge.py
</pre>

## Launch U-Center
On the PC, launch u-center, and select the USB comm port (such as COM4).  Make sure your settings are configured for 9600 baud.

U-Center should now be communicating with the Ublox gps receiver on the Nitrogen board.


