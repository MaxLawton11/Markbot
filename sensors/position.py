from gps import gps, WATCH_ENABLE

class GPS :
    def __init__(self) :
        # Connect to the GPSd service
        self.session = gps(mode=WATCH_ENABLE)
        
        self.latitude = None
        self.longitude = None
        self.latitude_error = None
        self.longitude_error = None
        self.speed = None
        self.altitude = None
        self.altitude_error = None
        
    def getPosition(self) :
        try:
            # Wait for new data
            report = self.session.next()
        
            
            # Check if the report is a TPV (Time-Position-Velocity) report
            if report['class'] == 'TPV':
                # Update the instance variables
                self.latitude = report.get('lat')
                self.longitude = report.get('lon')
                self.latitude_error = report.get('epx')
                self.longitude_error = report.get('epy')
                self.speed = report.get('speed')
                self.altitude = report.get('alt')
                self.altitude_error = report.get('epv')
                
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