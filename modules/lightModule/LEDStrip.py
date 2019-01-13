from modules.lightModule.IRLEDStripTransmitter import *

class LEDStrip:
    """
    This class represents a LED strip.
    """

    def __init__(self, id, label):
        """
        Constructor of the class.

        :param id:     the destination ID of the LED strip
        :param label:  the label for the LED strip
        """

        self._id = id
        self._label = label


    def applyColor(self, R, G, B):
        """
        This method applies a color to the LED strip.

        :param R:   The red value of the color
	:param G:   The green value of the color
	:param B:   The blue value of the color
        """
        
        IRLEDStripTransmitter.sendRGBColorTo(self._id, R, G, B)


    def turnOff(self):
        """
        This method turns off the LED strip.
        """

        IRLEDStripTransmitter.turnOff(self._id);


    def turnOn(self):
        """
        This method turns on the LED strip.
        """

        IRLEDStripTransmitter.turnOn(self._id);


    def toJSON(self):
        """
        This function returns a string representing the serialized LED strip in JSON.

        :returns: the JSON data
        """
        
        data = {}
        data['id'] = self._id;
        data['label'] = self._label;
        
        return data
