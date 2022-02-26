import time
from picamera import PiCamera

camera = PiCamera()

camera.start_preview()
sleep(30)
camera.stop_preview()
