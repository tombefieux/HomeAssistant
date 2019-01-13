from modules.lightModule.LEDStrip import *

class LightSet:
    """
    This class represents a mood :). It contains a color for each LED strip so, you
    can create a lightset named "work" with all the LED strips to white for example. 
    """

    def __init__(self, label, LEDStrips, colors):
        """
        Constructor of the class.

        :param label:      A label for the lightset
        :param LEDStrips:  The LEDStrips (an array)
        :param colors:     The color for each LED strip (in the same order as the LED strips), (an array of array)
        """

        self._label = label
        self._LEDStrips = LEDStrips
        self._colors = colors


    def apply(self):
        """
        This function applies the lightset.
        """
        
        i = 0
        for LEDStrip in self._LEDStrips:
            LEDStrip.applyColor(self._colors[i][0], self._colors[i][1], self._colors[i][2])
            i += 1


    def updateColorFor(self, id, color):
        """
        This function updates the color of a LEDstrip.

        :param id:      The id of the LEDStrip
        :param color:   The new color (An array)
        """

        # find the good LED strip
        currentStrip = None
        index = 0
        for LEDStrip in self._LEDStrips:
            if LEDStrip._id == id:
                currentStrip = LEDStrip
            if currentStrip == None:
                index += 1
                
        if currentStrip == None:
            return

        self._colors[index] = color

        
    def addLEDStrip(self, LEDStrip, color):
        """
        This function adds a LED strip to the lightset.

        :param LEDStrip: The LED strip
        :param color:    The color for this LED strip (an array)
        """

        self._LEDStrips.append(LEDStrip)
        self._colors.append(color)
        

    def removeLEDStrip(self, LEDStrip):
        """
        This function removes a LED strip in the lightset.

        :param LEDStrip:   The LED strip to remove
        """
        
        # find the good position
        currentStrip = None
        index = 0
        for current in self._LEDStrips:
            if current._id == LEDStrip._id:
                currentStrip = current
            if currentStrip == None:
                index += 1
                
        if currentStrip == None:
            return

        self._LEDStrips.remove(LEDStrip)
        self._colors.remove(self._colors[index])


    def toJSON(self):
        """
        This function returns a string representing the serialized lightset in JSON.

        :returns: the data
        """

        ids = []
        for current in self._LEDStrips:
            ids.append(current._id)
        
        data = {}
        data['label'] = self._label;
        data['LEDStripIDs'] = ids;
        data['colors'] = self._colors;
        
        return data
