import smbus


# loop through busses
for i_bus in [1,3] :
    
    # create I2C bus object
    bus = smbus.SMBus(i_bus)  # Use 1 for Raspberry Pi Model B+

    # scan for devices
    for address in range(0x03, 0x78):
        try:
            bus.read_byte(address)
            print("Device found at address: 0x{:02X} on Bus:{}".format(address, i_bus))
        except IOError:
            pass