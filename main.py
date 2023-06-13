from sensors import heading, position

if __name__ == '__main__' :
   test_pos = position.GPS()
   while True :
      
      if test_pos != None:
         print(test_pos)