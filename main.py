from sensors import heading, position

def main() :
   pos = position.GPS()
   for i in range(100) :
      result = pos.getPosition()
      if result != None:
         # Access the desired variables
         time = pos.time
         latitude = pos.latitude
         longitude = pos.longitude
         latitude_error = pos.latitude_error
         longitude_error = pos.longitude_error
         speed = pos.speed
         altitude = pos.altitude
         altitude_error = pos.altitude_error

         # Use the variables as needed
         print("Time:", time)
         print("Latitude:", latitude)
         print("Longitude:", longitude)
         print("Latitude Error:", latitude_error, "m")
         print("Longitude Error:", longitude_error, "m")
         print("Speed:", speed)
         print("Altitude:", altitude, "m")
         print("Altitude Error:", altitude_error, "m")
         print("-"*20)
   
   pos.closeConnection()

if __name__ == '__main__' :
   main()
