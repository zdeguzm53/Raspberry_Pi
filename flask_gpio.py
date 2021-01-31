from flask import Flask, render_template, request
import RPi.GPIO as GPIO

# basic setup for LED's, gpio pins, flask
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
leds = [17, 18]
GPIO.setup(leds, GPIO.OUT)
GPIO.output(leds, GPIO.LOW)
app = Flask(__name__)

@app.route("/", methods=["GET","POST"]) # makes methods get and post so that user input on webpage works
def index():
	if request.method == 'POST': # if the request type is a post, so someone clicking one of the buttons
		if request.form.get('btn1') == 'btn1': # if its on button, turn LED's on
			GPIO.output(leds, GPIO.HIGH)	
		elif request.form.get('btn2') == 'btn2': # if its off button, turn LED's off
			GPIO.output(leds, GPIO.LOW)
		else:
			return render_template("index.html") # returns the html template
	
	return render_template("index.html")	
     
if __name__ == "__main__":
     app.run(host="0.0.0.0", port=80, debug=True)
