# styles.py
from backend import xp
from utilities import Image
from filters import *
from effects import *
from masks import *

class Style:
    class Process:
        def __init__(self,opn:Filter|Effect,mask:Mask = FullMask(),strength:float = 1.0):
            self.operation = opn
            self.mask =mask
            self.strength = strength

    def __init__(self,name = "TestStyle"):
        self.name = name
        self.processes:list[Style.Process] = []

    def addProcess(self,process:Style.Process):self.processes.append(process)

    def apply(self,image:Image,imageMask:Mask = FullMask()):
        newImage = image.copy()
        for process in  self.processes:
            if isinstance(process.operation,Filter):
                processImage = Filter.applyToCopy(newImage,process.operation,process.strength)
            elif isinstance(process.operation,Effect):
                processImage = Effect.applyToCopy(newImage,process.operation,process.strength)
            processMask = process.mask.getMask(newImage.pixelArray.shape)
            newImage.pixelArray = processImage.pixelArray*processMask + newImage.pixelArray*(1-processMask)
            
        maskArray = imageMask.getMask(image.pixelArray.shape)
        image.pixelArray = newImage.pixelArray*maskArray + image.pixelArray*(1-maskArray) 
        
        return image
    
    def applyToCopy(self,image:Image,imageMask:Mask = FullMask()):
        return self.apply(image.copy(),imageMask)

