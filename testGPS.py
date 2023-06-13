import serial

# Configure the serial port
port = serial.Serial("/dev/ttyUSB0", baudrate=9600, timeout=1)

# Main loop
while True:
    try:
        # Read a line of data from the serial port
        line = port.readline().decode("utf-8")
        
        # Process the GPS data
        if line.startswith("$GPRMC"):
            # Assuming the data follows the NMEA format (e.g., $GPRMC)
            data = line.split(",")
            if len(data) >= 4:
                latitude = data[3]
                longitude = data[5]
                
                print("Latitude:", latitude)
                print("Longitude:", longitude)
    
    except KeyboardInterrupt:
        # Exit gracefully on Ctrl+C
        port.close()
        break
