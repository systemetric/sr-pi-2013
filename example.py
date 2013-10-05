import serial
import time

mbedComms = serial.Serial('/dev/ttyACM0', 115200)

print("Setting motor 0 to -100 power!")

# tell mbed to set motor 0 to 100 power
mbedComms.write('M0(-100)')
# flush the message down the wire
mbedComms.flush()
# listen for a line of acknowledgement
mbedComms.readline()

time.sleep(1)

print("Setting motor 0 to 0 power!")

mbedComms.write('M0(0)')
mbedComms.flush()
mbedComms.readline()

print("Success!")

# clean up
mbedComms.close()
