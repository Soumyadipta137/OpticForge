import math
from backend import xp
from PIL import Image as Img

class Image:
    """Wrapper Class for PIL.Imgae.Image and saves image internally as xp.array to save repeated conversion"""
    @classmethod
    def deImagifier(cls,image:Img.Image) -> xp.ndarray:
        """This Converts Pillow Image into Numpy array(Height,width,RGB)"""
        return xp.array(image)
    
    @classmethod
    def imagifier(cls,pixelArray:xp.ndarray) -> Img.Image:
        """This Converts Pillow Image into Numpy array(Height,width,RGB)"""
        return Img.fromarray(pixelArray.astype(xp.uint8))

    def __init__(self,filename,opacity = None):
        Ixput = Img.open(filename)
        self.pixelArray = self.deImagifier(Ixput)
        if opacity is not None:
            self.opacity(opacity)

    def save(self,filename):
        self.imagifier(self.pixelArray).save(filename)

    def copy(self) -> Image:
        cls = type(self)
        newObj = cls.__new__(cls)
        newObj.pixelArray = self.pixelArray.copy()
        return newObj

    def opacity(self,opacity:float|int):
        if type(opacity)==int:
            opacity:float = opacity/255
        opacity:float = opacity-math.floor(opacity)
        self.setMask(xp.full(self.pixelArray.shape, opacity, dtype=xp.float32))

    def setMask(self,mask):self.mask=mask


    

class Mask:
    def __init__(self,image,background,mask):pass
        