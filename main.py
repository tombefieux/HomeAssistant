from modules.lightModule.LightManager import *

# test the light module
led = LEDStrip(2, "Foo")

manager = LightManager()
manager.addColor("red", [255, 0, 0])
manager.addColor("green", [0, 255, 0])
manager.addColor("blue", [0, 0, 255])

if manager.applyLightSet("test"):
    print("light set applied")

if manager.addLightSet("test", [[0, 0, 0], [255, 255, 255]]):
    print("lightset added")
    
if manager.applyLightSet("test"):
    print("lightset applied")
        
if manager.updateLightSet("test", [[0, 0, 0], [255, 255, 255]]):
    print("lightset updated")

if manager.removeLightSet("test"):
    print("lightset removed")

if manager.turnOnLights():
    print("turned on")

if manager.turnOffLights():
    print("turned off")

if manager.addLEDStrip(led):
    print("added")

if manager.removeLEDStrip("Foo"):
    print("removed")

manager.save()
