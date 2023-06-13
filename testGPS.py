import gps

print(1)

# Connect to the GPSd service
session = gps.gps("localhost", "2947")
session.stream(gps.WATCH_ENABLE | gps.WATCH_NEWSTYLE)

print(2)

# Main loop
while True:
    try:
        # Wait for new data
        report = session.next()
        if report['class'] == 'TPV':
            if hasattr(report, 'lat') and hasattr(report, 'lon'):
                print("Latitude:", report.lat)
                print("Longitude:", report.lon)
    except KeyboardInterrupt:
        # Exit gracefully on Ctrl+C
        session.close()
        break
    except StopIteration:
        # End of file reached
        session.close()
        print("GPSD has terminated")
        break
