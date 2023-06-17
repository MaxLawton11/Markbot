from gps import gps, WATCH_ENABLE # make sure to intall gps with pip3

# class to cheack postion using the usb gps
# pulls data from equivalent command `cgps`
class GPS :
    def __init__(self) :
        # connect to the GPSd service
        self.session = gps(mode=WATCH_ENABLE)
        
        # store data in object
        self.time = None
        self.latitude = None
        self.longitude = None
        self.latitude_error = None
        self.longitude_error = None
        self.speed = None
        self.altitude = None
        self.altitude_error = None
        
    def getPosition(self) :
        try:
            # wait for new data
            report = self.session.next()
            
            # check if the report is a TPV (Time-Position-Velocity) report
            if report['class'] == 'TPV':
                # update variables
                self.time = report.get('time')
                self.latitude = report.get('lat')
                self.longitude = report.get('lon')
                self.latitude_error = report.get('epx')
                self.longitude_error = report.get('epy')
                self.speed = report.get('speed')
                self.altitude = report.get('alt')
                self.altitude_error = report.get('epv')
                
                # return the raw data
                return report
            
        except StopIteration:
            # loop stopped
            self.session.close()
            return None
        
    def closeConnection(self) :
        # when done
        self.session.close()
        return None
