from sensors import heading, position

if __name__ == '__main__' :
   test_pos = position.GPS()
   while True :
      result = test_pos.getPosition()
      if result != None:
         # Access the desired variables
         time = test_pos.time
         latitude = test_pos.latitude
         longitude = test_pos.longitude
         latitude_error = test_pos.latitude_error
         longitude_error = test_pos.longitude_error
         speed = test_pos.speed
         altitude = test_pos.altitude
         altitude_error = test_pos.altitude_error

         # Use the variables as needed
         print("Time:", time)
         print("Latitude:", latitude)
         print("Longitude:", longitude)
         print("Latitude Error:", latitude_error, "m")
         print("Longitude Error:", longitude_error, "m")
         print("Speed:", speed)
         print("Altitude:", altitude)
         print("Altitude Error:", altitude_error, "m")
         print("-"*20)