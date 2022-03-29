from gpiozero import MotionSensor
import time
import datetime
 
print('Home Secure started')
time.sleep(1)
print ('Ready')
pir = MotionSensor(23)

while True:
  pir.wait_for_motion()
  print('Motion Detected'+ datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
  pir.wait_for_no_motion()
