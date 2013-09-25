import serial
import time

mbedComms = serial.Serial('/dev/ttyACM0', 115200)

print("Setting motor 0 to 50 power!")

# tell mbed to set motor 0 to 100 power
mbedComms.write('M0(50)')
# flush the message down the wire
mbedComms.flush()
# listen for a byte of acknowledgement
mbedComms.read(1)

time.sleep(2)

print("Setting motor 0 to 0 power!")

mbedComms.write('M0(0)')
mbedComms.flush()
mbedComms.read(1)

print("Success!")

# clean up
mbedComms.close()
