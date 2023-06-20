import smbus

# HMC5883L address
address = 0x0D

# Register addresses
config_register = 0x00
data_register = 0x03

# Create I2C bus object
bus = smbus.SMBus(3)  # Use 1 for Raspberry Pi Model B+

# Set the configuration register
bus.write_byte_data(address, config_register, 0x00)

while True:
    # Check if data is available
    data_available = bus.read_byte_data(address, data_register) & 0x01

    print(data_available)

