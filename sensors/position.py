import gps

class GPS :
    def __init__(self) :
        # Connect to the GPSd service
        self.session = gps(mode=WATCH_ENABLE)
        
    def getPosition(self) :
        try:
            # Wait for new data
            report = self.session.next()
            
            # Check if the report is a TPV (Time-Position-Velocity) report
            if report['class'] == 'TPV':
                # Return the raw data
                return report
            
        except StopIteration:
            # End of file reached
            self.session.close()
            print("GPSD has terminated")
            return None
            
class Tester :
    def __init__(self) :
        print('we worken from position')