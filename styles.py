# styles.py
from backend import xp
from utilities import Image
from masks import *

class Style:
    class Process:
        def __init__(self,opn:Effect|Style,mask:Mask = FullMask(),strength:float = 1.0):
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
            processMask = process.mask.getMask(image.pixelArray.shape)
            if isinstance(process.operation,Effect):
                processImage = process.operation.applyToCopy(newImage,process.strength)
                processImage.pixelArray*=processMask
                newImage.pixelArray*=(1-processMask)
                newImage.pixelArray += processImage.pixelArray 

            if isinstance(process.operation,Style):
                newImage = process.operation.apply(newImage,Mask(process.strength*processMask))
            
        maskArray = imageMask.getMask(image.pixelArray.shape)
        newImage.pixelArray*=maskArray
        image.pixelArray*=(1-maskArray)
        image.pixelArray += newImage.pixelArray
        return image
    
    def applyToCopy(self,image:Image,imageMask:Mask = FullMask()):
        return self.apply(image.copy(),imageMask)


class Effect:
    def __init__(self):
        self.toCopy =False
    def apply(self,image:Image,strength:float = 1.0):
        """Universal pipeline to apply Effects to Original Image.\n Both pixel level and large scale pixel value manipulation possible using given Strength"""
        newImage = image.shallowCopy()
        newImage.pixelArray= array = self.hue(image.pixelArray)
        if newImage.pixelArray.shape[2]==1:newImage.pixelArray = xp.concatenate((array,array,array),axis=2)
        newImage.pixelArray*=strength
        newImage.pixelArray+= image.pixelArray*(1-strength)
        if not self.toCopy:image.pixelArray = newImage.pixelArray
        self.toCopy = False
        return newImage

    def applyToCopy(self,image:Image,strength:float = 1.0) -> Image:
        """Universal pipeline to apply Effects to Copy of Image.\n Both pixel level and large scale pixel value manipulation possible using given Strength"""
        self.toCopy = True
        return self.apply(image,strength)    

    def config(self):pass
    def hue(self,pixelArray:xp.ndarray)->xp.ndarray:"""Internal function\\\n"Make sure to return new array not shallow copy" """
    pass

class Transform(Effect):
    pass

class Filter(Effect):
    def init(self):pass
    def imageSize(self,size = (0,0)):self.height,self.width = size[0:2]

class ArrayFilter(Filter):pass

class PixelFilter(Filter):
    def apply(self,image:Image,strength:float = 1.0):
        """Universal pipeline to apply Filter to Original Image.\\\nPixel level colour manipulation possible with Strength"""
        self.imageSize(image.pixelArray.shape[0:2])
        self.init()
        newImage = image.shallowCopy()
        newImage.pixelArray = xp.empty_like(image.pixelArray)
        for y in range(image.pixelArray.shape[0]):
            for x in range(image.pixelArray.shape[1]):
                newImage.pixelArray[y,x] = self.hue((x,y),image.pixelArray[y,x])
        newImage.pixelArray *= strength 
        newImage.pixelArray+= image.pixelArray*(1-strength)
        if not self.toCopy:image.pixelArray = newImage.pixelArray
        self.toCopy = False
        return newImage
    
    def applyToCopy(self,image:Image,strength:float = 1.0) -> Image:
        """Universal pipeline to apply Filter to Copy of Image.\nPixel level colour manipulation possible with Strength"""
        self.toCopy = True
        return self.apply(image,strength)
        

    def hue(self,pos:tuple[int,int],colour = (0,0,0))->xp.ndarray:
        """Internal function\\\n(x,y), old pixel Colour -> returns new pixelcolour"""
        pass