# Open a serial connection from BeagleBone Black (rev. C) to a Telit GL865-QUAD GSM/GPRS module
# using the Adafruit BeagleBone IO Library (https://github.com/adafruit/adafruit-beaglebone-io-python).
# Must be executed as root.

import Adafruit_BBIO.UART as UART
import serial, time, sys

global serial_port

UARTNAME = "UART1"
# Adafruit_BBIO associates UARTx to /dev/ttyOx with 1<=x<=5. Read Adafruit
# documentation for more info.
PORTPATH = "/dev/ttyO1"
BAUD = 9600


def getReply (timeSleep=.1):
    global serial_port
    timeout = time.time() + 10
    while serial_port.inWaiting() < 3:  # read only 3 characters from the rx buffer
        time.sleep(1)                   # don't overwhelm the processor
        if time.time() > timeout:
            return "ERROR"
    time.sleep(timeSleep)
    return serial_port.readlines()


def ping():
    global serial_port
    AT = "AT\r"
    OK = "OK\r\n"
    serial_port.flushInput()        # clear buffer
    serial_port.write(AT)           # send AT<CR>
    response = getReply()           # wait for response from Telit

    if OK in response:
        print "Telit replied, communication OK."
        return True
    else:
        print "Failed to communicate with Telit. Check port or Telit status."
        sys.exit(1)


UART.setup(UARTNAME)
serial_port = serial.Serial(PORTPATH, BAUD, timeout=1, bytesize=8, stopbits=1, parity='N', writeTimeout=1)
serial_port.close()
serial_port.open()
if not serial_port.isOpen():
    print "Failed to open serial port %s on device %s" % (UARTNAME, PORTPATH)
print "Serial port %s open on device %s" % (UARTNAME, PORTPATH)
ping()
