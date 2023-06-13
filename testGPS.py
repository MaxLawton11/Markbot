from gps import gps, WATCH_ENABLE

# Create a GPS object
session = gps(mode=WATCH_ENABLE)

# Main loop
while True:
    try:
        # Wait for new data
        report = session.next()
        
        # Check if the report is a TPV (Time-Position-Velocity) report
        if report['class'] == 'TPV':
            # Print the raw data
            print(report)
            
    except KeyboardInterrupt:
        # Exit gracefully on Ctrl+C
        session.close()
        break
    except StopIteration:
        # End of file reached
        session.close()
        print("GPSD has terminated")
        break
