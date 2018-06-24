from picamera import PiCamera
from time import sleep

camera = PiCamera()

camera.start_preview()
sleep(5)
camera.capture('/home/pi/Desktop/image.jpg')
camera.stop_preview()

camera. resolution = (1920, 1080)
camera.framerate = 15
camera.start_preview()
sleep(5)
camera.capture('/home/pi/Desktop/max.jpg')
camera.stop_preview

camera.start_preview()
camera.annotate_text = "Dis Guy.... playing Fortnite"
sleep(5)
camera.capture('/home/pi/Desktop/text.jpg')
camera.stop_preview()

camera.start_preview()
camera.brightness = 71
sleep(5)
camera.capture('/home/pi/Desktop/bright.jpg')
camera.stop_preview()

camera.start_preview()
for i in range(100):
    camera.annotate_text = "Brightness: %s" % i
    camera.brightness = i
    sleep(0.1)
camera.stop_preview()

camera.start_preview()
for i in range(100):
    camera.annotate_text = "Contrast: %s" % i
    camera.contrast = i
    sleep(0.1)
camera.stop_preview()

camera.annotate_text_size = 86

from picamera import PiCamera, Color

camera.start_preview()
camera.annotate_background = Color('red')
camera.annotate_foreground = Color('green')
camera.annotate_text = "Dis Guy.... playing Fortnite"
sleep(5)
camera.stop_preview()

camera.start_preview()
camera.image_effect = 'colorswap'
sleep(5)
camera.capture('/home/pi/Desktop/colorswap.jpg')
camera.stop_preview()

camera.start_preview()
for effect in camera.IMAGE_EFFECTS:
    camera.image_effect = effect
    camera.annotate_text = "Effect: %s" % effect
    sleep(5)
camera.stop_preview()

camera.start_preview()
camera.awb_mode = 'tungsten'
sleep(5)
camera.capture('/home/pi/Desktop/sunlight.jpg')
camera.stop_preview()

