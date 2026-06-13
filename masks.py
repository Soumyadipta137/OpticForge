import functools
from backend import xp
from utilities import coordArray2DTransform

class Gradient:
    @staticmethod
    def selection(array:xp.ndarray): #basic default function to be used for converting mask into selection(place holder for no fading)
        return xp.where(array>0,1.0,0.0)

    def __init__(self,func:function[float] = None,reach=0.1,useAngle=False):
        self.reach = reach
        self.func = func
        self.useAngle = useAngle

        if self.func is None:
            self.func = lambda x:x
            self.reach = 0.0
        if self.reach == 0.0:self.reach = 0.001        

    def gradient(self,normalizedArray:xp.ndarray,inverse,angle = None) -> xp.ndarray:
        reverseDistance = 1 - normalizedArray
        reverseDistance = xp.clip(reverseDistance,0.0,1.0)
        if self.useAngle:   mask = self.func(reverseDistance/self.reach,angle)
        else:               mask = self.func(reverseDistance/self.reach)
        mask:xp.ndarray = xp.clip(mask,0.0,1.0)
        if inverse:mask = 1-mask
        return xp.concatenate((mask[:,:,None],mask[:,:,None],mask[:,:,None]),axis=2)


class Mask:
    def __init__(self,mask:xp.ndarray):
        self.mask:xp.ndarray = mask.astype(xp.float32)

    def getMask(self,ndShape):return self.mask.clip(0.0,1.0)

    @classmethod
    def combineArray(cls, *args:xp.ndarray):
        if len(args) == 1:
            if isinstance(args[0], xp.ndarray):
                if args[0].ndim == 3:return Mask(xp.clip(args[0].astype(xp.float32),0.0, 1.0))
                elif args[0].ndim == 4:
                    args = args[0]
            else:args = args[0]

        mask = functools.reduce(lambda a, b: a * b,args)
        return Mask(xp.clip(mask.astype(xp.float32),0.0, 1.0))
    
class MaskSet(Mask):
    def __init__(self,*args:Mask,inverse = False):
        self.maskList:list[Mask] = []
        self.inverse = inverse
        for mask in args:self.maskList.append(mask)

    def getMask(self, ndShape):
        newMask = 1
        for mask in self.maskList:newMask *= mask.getMask(ndShape)
        if self.inverse:newMask = 1 - newMask
        return newMask
    
class MaskJoin(Mask):
    def __init__(self,*args:Mask,inverse = False):
        self.maskList:list[Mask] = []
        self.inverse = inverse
        for mask in args:self.maskList.append(mask)

    def getMask(self, ndShape):
        newMask = 0
        for mask in self.maskList:newMask = newMask + mask.getMask(ndShape) -newMask*mask.getMask(ndShape)
        if self.inverse:newMask = 1 - newMask
        return newMask

    
class FullMask(Mask):
    def __init__(self,opacity = 1.0):self.alpha = opacity
    def getMask(self, ndShape):return xp.full(ndShape,self.alpha,xp.float32,)

class EllipseMask(Mask):
    def __init__(self,rCentre:float|tuple[float, float],radii:float|tuple[float, float],
                gradient: Gradient = Gradient(),theta: float = 0.0,inverse=False):
        self.rCentre = rCentre
        self.radii = radii
        if type(self.radii)==float:self.radii=(self.radii,self.radii)
        if type(self.rCentre)==float:self.rCentre=(self.rCentre,self.rCentre)
        self.mask = None
        self.theta = theta
        self.inverse = inverse
        self.gradient = gradient

    def getMask(self, ndShape):
        Y, X = xp.indices(ndShape[0:2], dtype=xp.float32)
        rx,ry = coordArray2DTransform(X,Y,(self.rCentre[0]*ndShape[1],self.rCentre[1]*ndShape[0]),self.theta)
        rDistance = xp.sqrt((rx / (self.radii[0] * ndShape[1])) ** 2 + (ry / (self.radii[1] * ndShape[0])) ** 2)
        self.mask = self.gradient.gradient(rDistance,self.inverse)
        return self.mask


class CircleMask(EllipseMask):  #Radii According to smaller Side
    def __init__(self,rCentre: tuple[float, float],radii:float,gradient: Gradient = Gradient(),inverse=False):
        super().__init__(rCentre,(radii,radii),gradient,0.0,inverse)

class RectangularMask(Mask):
    def __init__(self,rCentre: tuple[float, float],sides: tuple[float, float],
                gradient: Gradient = Gradient(),theta: float = 0.0,inverse=False):
        self.rCentre = rCentre
        self.sides = sides
        self.mask = None
        self.theta = theta
        self.inverse = inverse
        self.gradient = gradient

    def getMask(self, ndShape):
        Y, X = xp.indices(ndShape[0:2], dtype=xp.float32)
        rx,ry = coordArray2DTransform(X,Y,(self.rCentre[0]*ndShape[1],self.rCentre[1]*ndShape[0]),self.theta)
        rDistance = 2* xp.maximum(xp.abs(rx) / (self.sides[0] * ndShape[1]),xp.abs(ry) / (self.sides[1] * ndShape[0]))
        self.mask = self.gradient.gradient(rDistance,self.inverse)
        return self.mask