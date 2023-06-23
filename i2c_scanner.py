import smbus

# Create I2C bus object
bus = smbus.SMBus(1)  # Use 1 for Raspberry Pi Model B+

# Scan for devices
for address in range(0x03, 0x78):
    try:
        bus.read_byte(address)
        print("Device found at address: 0x{:02X}".format(address))
    except IOError:
        pass

# bus 3
bus = smbus.SMBus(3)

# Scan for devices
for address in range(0x03, 0x78):
    try:
        bus.read_byte(address)
        print("Device found at address: 0x{:02X}".format(address))
    except IOError:
        pass