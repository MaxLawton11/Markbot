import smbus
import time

# HMC5883L address
address = 0x1E

# Register addresses
config_register = 0x00
data_register = 0x03

# Create I2C bus object
bus = smbus.SMBus(1)  # Use 1 for Raspberry Pi Model B+

# Function to read signed 16-bit data from two consecutive registers
def read_data(register):
    high = bus.read_byte_data(address, register)
    low = bus.read_byte_data(address, register + 1)
    value = (high << 8) | low
    if value > 32767:
        value -= 65536
    return value

# Set the configuration register
bus.write_byte_data(address, config_register, 0x00)

while True:
    # Read magnetometer data
    x = read_data(data_register)
    z = read_data(data_register + 2)
    y = read_data(data_register + 4)

    # Print the raw values
    print("Raw Magnetometer Data:")
    print("X: {0}".format(x))
    print("Y: {0}".format(y))
    print("Z: {0}".format(z))

    # Calculate heading in degrees
    heading = (180 * math.atan2(y, x)) / math.pi

    # Normalize heading to a 0-360 degree range
    if heading < 0:
        heading += 360

    # Print the heading
    print("Heading: {0} degrees".format(heading))

    # Wait for a while before reading again
    time.sleep(0.5)
