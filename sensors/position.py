import gps

class GPS :
    def __init__(self) :
        # Connect to the GPSd service
        self.session = gps.gps("localhost", "2947")
        self.session.stream(gps.WATCH_ENABLE | gps.WATCH_NEWSTYLE)
        
    def getPosition(self) :
        # loop until we get a result
        while True:
            try:
                # wait for new data
                report = self.session.next()
                print(report)
                if report['class'] == 'TPV':
                    if hasattr(report, 'lat') and hasattr(report, 'lon'):
                        latitude = report.lat
                        longitude = report.lon
                        return latitude, longitude
            except KeyboardInterrupt:
                # Exit gracefully on Ctrl+C
                self.session.close()
                break
            except StopIteration:
                # End of file reached
                self.session.close()
                print("GPSD has terminated")
                break
            
class Tester :
    def __init__(self) :
        print('we worken from position')