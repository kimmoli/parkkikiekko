# main.py -- put your code here!


from pyb import Pin
from pyb import LED

mot1 = Pin('Y3', Pin.OUT_PP)
mot2 = Pin('Y4', Pin.OUT_PP)
mot1.low()
mot2.low()

kello12 = Pin('Y5', Pin.IN, Pin.PULL_UP)



def kolmannes():
   m = kello12.value()
   n = m
   mot1.high()   
   
   while not (m == 0 and n == 1):
      pyb.delay(1)
      n = m
      m = kello12.value()

   mot1.low()

while True:
  LED(1).on()
  kolmannes()
  kolmannes()
  kolmannes()
  LED(1).off()
  pyb.delay(500)
  