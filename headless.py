import time
import Adafruit_SSD1306
import Adafruit_LSM303

from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont

RST = 24
accelerometer = Adafruit_LSM303.LSM303() # accelerometer setup

# display setup
disp = Adafruit_SSD1306.SSD1306_128_64(rst=RST, i2c_address=0x3d)
disp.begin()
disp.clear()
disp.display()
width = disp.width
height = disp.height 
image = Image.new('1', (width, height))

draw = ImageDraw.Draw(image) # gets drawing object to draw on image
draw.rectangle((0,0,width,height), outline=0, fill=0) # draws black rectangle on screen
font = ImageFont.load_default()

disp.image(image)
disp.display() # clears screen

radius = 5

while True:
	draw.rectangle((0, 0, width, height), outline=0, fill=0) # draws black rectangle on screen
	accel, mag = accelerometer.read() # gets accelerometer data
	accel_x, accel_y, accel_z = accel
	mag_x, mag_y, mag_z = mag
	
	# these lines get the x and y position for the dot based on the accelerometer values, more info on these in the readme
	x_pos = 64 - (accel_y / 100) / 15 * 128
	y_pos = 32 - (accel_x / 100) / 15 * 64 
		
	#print(x_pos, y_pos)
	# if you uncomment this line, you can see that when the accelerometer is in a neutral position,
	# the x and y position values hover around 63 and 33, which is extremely close to dead center

	draw.ellipse((x_pos - radius, y_pos - radius, x_pos + radius, y_pos + radius), outline=255, fill=255) # draws the dot that moves around
	
	disp.image(image)
	disp.display() # displays the dot
