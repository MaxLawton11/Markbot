from sensors import heading, position

if __name__ == '__main__' :
   test_pos = position.GPS()
   while True :
      result = test_pos.getPosition()
      if result != None:
         # Access the desired variables
         latitude = result.latitude
         longitude = result.longitude
         latitude_error = result.latitude_error
         longitude_error = result.longitude_error
         speed = result.speed
         altitude = result.altitude
         altitude_error = result.altitude_error

         # Use the variables as needed
         print("Latitude:", latitude)
         print("Longitude:", longitude)
         print("Latitude Error:", latitude_error)
         print("Longitude Error:", longitude_error)
         print("Speed:", speed)
         print("Altitude:", altitude)
         print("Altitude Error:", altitude_error)