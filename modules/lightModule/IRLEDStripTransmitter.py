import os
import time

class IRLEDStripTransmitter:
	"""
	This class is used to send data to LED strip controllers with irsend.
	"""

	@staticmethod		
	def sendValue(dest, value):
		"""
		This method sends one value to a LED strip controller.
		If you want to send a color, use the sendRGBColorTo method instead. 
		
		:param dest:	The destination ID of the LED strip
		:param value:	The sent value
		"""
		
		temp = dest;
		temp << 8;
		temp += value
		os.system("irsend SEND_ONCE myConf " + str(temp));


	@staticmethod
	def sendRGBColorTo(dest, r, g, b):
		"""
		This method sends a color to a LED strip controller.
		
		:param dest:	The destination ID of the LED strip
		:param r:		The red value of the color
		:param g:		The green value of the color
		:param b:		The blue value of the color
		"""
		
		IRLEDStripTransmitter.sendValue(dest, r);
		time.sleep(0.1);
		IRLEDStripTransmitter.sendValue(dest, g);
		time.sleep(0.1);
		IRLEDStripTransmitter.sendValue(dest, b);
			
			
	@staticmethod
	def turnOff(dest):
		"""
		This method turns off a LED strip.
		
		:param dest:	The destination ID of the LED Strip to turn off
		"""
		IRLEDStripTransmitter.sendRGBColorTo(dest, 0, 0, 0)


	@staticmethod
	def turnOn(dest):
		"""
		This method turns on a LED strip.
		
		:param dest:	The destination ID of the LED Strip to turn on
		"""
		IRLEDStripTransmitter.sendRGBColorTo(dest, 255, 255, 255)
