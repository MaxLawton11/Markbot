from turtle import pos
from sensors import heading, position

if __name__ == '__main__' :
   test_pos = position.GPS()
   print(test_pos.getPosition())