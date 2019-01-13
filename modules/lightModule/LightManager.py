import json
from modules.lightModule.LightSet import *

class LightManager:
    """
    This class manages the lights.
    """

    def __init__(self):
        """
        Contructor of the class.
        """

        self._lightSets = []
        self._LEDStrips = []
        self._listOfColors = {}
        self.load()


    def load(self):
        """
        This function loads the manager with a JSON file
        """

        with open('save/light.json') as file:
            data = json.load(file)

            # load the colors
            for color in data["colorsList"]:
                self._listOfColors[color["label"]] = color["value"]

            # load the LED strips
            for strip in data["LEDStrips"]:
                self._LEDStrips.append(LEDStrip(strip["id"], strip["label"]))

            # load the lightsets
            for lightSet in data["lightSets"]:
                # get the LED strips
                leds = []
                for stripId in lightSet["LEDStripIDs"]:
                    # get index
                    strip = None
                    for current in self._LEDStrips:
                        if stripId == current._id:
                            strip = current
                    leds.append(strip)
                    
                obj = LightSet(lightSet["label"], leds, lightSet["colors"])    
                self._lightSets.append(obj)


    def save(self):
        """
        This function saves the manager with all its informations.
        """

        with open('save/light.json', 'w') as file:
            data = {}

            # colors
            colors = []
            for color in self._listOfColors:
                temp = {}
                temp["label"] = color
                temp["value"] = self._listOfColors[color]
                colors.append(temp)

            # strips
            strips = []
            for strip in self._LEDStrips:
                strips.append(strip.toJSON())

            # lightsets
            lightsets = []
            for lightset in self._lightSets:
                lightsets.append(lightset.toJSON())

            data["colorsList"] = colors
            data["LEDStrips"] = strips
            data["lightSets"] = lightsets
            json.dump(data, file, indent=4)
    

    def applyColor(self, label, colorName):
        """
        This function applies a color to a LED strip.

        :param label:       The label of the LED strip
        :param colorName:   The name of the color

        :returns if it failed or not
        """

        # get the LED strip
        LEDStrip = None
        for current in self._LEDStrips:
            if label == current._label:
                LEDStrip = current
        if LEDStrip == None:
            return False

        try:
            LEDStrip.applyColor(self._listOfColors[colorName][0], self._listOfColors[colorName][1], self._listOfColors[colorName][2])
        except:
            return False
        
        return True


    def applyLightSet(self, label):
        """
        This function applies a lightset.

        :param label:    The label of the lightset

        :returns if it failed or not
        """

        # get the lightset
        lightSet = None
        for current in self._lightSets:
            if label == current._label:
                lightSet = current
        if lightSet == None:
            return False

        lightSet.apply()

        return True


    def turnOffLights(self):
        """
        This function turns off all the lights.

        :returns if it failed or not
        """

        for strip in self._LEDStrips:
            strip.turnOff()

        return True # we can't fail


    def turnOnLights(self):
        """
        This function turns on all the lights.

        :returns if it failed or not
        """

        for strip in self._LEDStrips:
            strip.turnOn()

        return True # we can't fail
        
        
    def addLEDStrip(self, LEDStrip):
        """
        This function adds a LED strip to the manager.

        :param LEDStrip:   The LED strip to add (an object)

        :returns if the LED strip is added or not
        """

        # check if there's no issue of same ID or label
        ok = True
        for strip in self._LEDStrips:
            if LEDStrip._id == strip._id:
                ok = False
            elif LEDStrip._label == strip._label:
                ok = False

        if ok:
            for current in self._lightSets:
                current.addLEDStrip(LEDStrip, [0, 0, 0])
            self._LEDStrips.append(LEDStrip)
            return True

        return False


    def addLightSet(self, lightSet):
        """
        This function adds a lightset to the manager.

        :param lightSet:   The lightset to add (an object)

        :returns if the lightSet is added or not
        """

        # check if there's no issue of same label
        ok = True
        for current in self._lightSets:
            if lightSet._label == current._label:
                ok = False

        if ok:
            self._lightSets.append(lightSet)
            return True

        return False


    def addLightSet(self, label, colors):
        """
        This function adds a lightset to the manager with all the light by default.

        :param label:    The label for the lightset
        :param colors:   The colors for the lightset (an array of array)

        :returns if the lightSet is added or not
        """

        # check if there's no issue of same label
        ok = True
        for current in self._lightSets:
            if label == current._label:
                ok = False

        # if not good size of color
        if len(self._LEDStrips) != len(colors):
            return False

        if ok:
            self._lightSets.append(LightSet(label, self._LEDStrips, colors))
            return True

        return False


    def addColor(self, name, color):
        """
        This function adds a color to the manager.
        If the name already exists, the color is updated.

        :param name:    The name of the color
        :param color:   The color (array with r, g and b values)
        """

        self._listOfColors[name] = color


    def updateLightSet(self, label, colors):
        """
        This function updates the lightset with the colors.

        :param label:    The label of the lightset
        :param colors:   The new colors of the lightset (an array of array)

        :returns if the lightSet is updated or not
        """

        # get the lightset
        lightSet = None
        for current in self._lightSets:
            if label == current._label:
                lightSet = current
        if lightSet == None:
            return False

        # if not good size of color
        if len(self._LEDStrips) != len(colors):
            return False

        lightSet._colors = colors
        return True
        
        
    def removeLEDStrip(self, label):
        """
        This function removes a LED strip.

        :param label:   The label of the LED strip to remove

        :returns if the LED strip is removed or not
        """

        # get the LED strip
        strip = None
        for current in self._LEDStrips:
            if label == current._label:
                strip = current
        if strip == None:
            return False

        for current in self._lightSets:
            current.removeLEDStrip(strip)
        self._LEDStrips.remove(strip)

        return True

    def removeLightSet(self, label):
        """
        This function removes a lightset.

        :param label:   The label of the lightset to remove

        :returns if the lightset is removed or not
        """

        # get the lightset
        lightSet = None
        for current in self._lightSets:
            if label == current._label:
                lightSet = current
        if lightSet == None:
            return False

        self._lightSets.remove(lightSet)

        return True
