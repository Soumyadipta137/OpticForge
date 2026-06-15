# utilities.py
import math
from backend import xp
from PIL import Image as Img

def coordArray2DTransform(x:xp.ndarray,y:xp.ndarray,centre:tuple[float,float]=(0.0,0.0),theta:float = 0.0):
    dx , dy = x-centre[0] , y-centre[1]
    thetaArray = xp.full(x.shape,theta,xp.float32)
    cosT , sinT = xp.cos(thetaArray) , xp.sin(thetaArray)
    rx = dx * cosT + dy * sinT
    ry = -dx * sinT + dy * cosT
    return (rx,ry)

class Image:
    """Wrapper Class for PIL.Imgae.Image and saves image internally as xp.array to save repeated conversion"""
    @classmethod
    def deImagifier(cls,image:Img.Image) -> xp.ndarray:
        """This Converts Pillow Image into Numpy array(Height,width,RGB)"""
        return xp.array(image).astype(xp.float32)
    
    @classmethod
    def imagifier(cls,pixelArray:xp.ndarray) -> Img.Image:
        """This Converts Pillow Image into Numpy array(Height,width,RGB)"""
        return Img.fromarray(pixelArray.astype(xp.uint8))

    def __init__(self,filename,opacity = None):
        self.pixelArray = self.deImagifier(Img.open(filename))
        self.opacity(opacity)

    def save(self,filename):
        self.imagifier(self.pixelArray).save(filename)

    def copy(self) -> Image:
        cls = type(self)
        newObj = cls.__new__(cls)
        newObj.pixelArray = self.pixelArray.copy()
        newObj.opacity(self.alpha)
        return newObj
    
    def shallowCopy(self):
        cls = type(self)
        newObj = cls.__new__(cls)
        newObj.pixelArray = self.pixelArray
        newObj.alpha = self.alpha
        return newObj

    def opacity(self,opacity:float|int = None):
        if opacity is None:opacity = 1.0
        if type(opacity)==int:
            opacity:float = opacity/255
        if opacity != 1.0:opacity:float = opacity-math.floor(opacity)
        self.alpha = opacity

