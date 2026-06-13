# filters.py
from backend import xp
from utilities import Image

class Filter:
    @classmethod
    def apply(cls,image:Image,Imagefilter:Filter,strength:float = 1.0):
        """Universal pipeline to apply Filters to Original Image.\n Both pixel level and large scale pixel value manipulation possible using given Strength"""
        if not isinstance(Imagefilter,Filter):raise TypeError("Only Accept filter type")
        pixelArray = image.pixelArray
        Imagefilter.imageSize(pixelArray.shape[0:2])
        Imagefilter.init()

        if not Imagefilter.massApply:
            for y in range(pixelArray.shape[0]):
                for x in range(pixelArray.shape[1]):
                    pixelArray[y,x] = Imagefilter.hue(y,x,pixelArray[y,x])

        else:
            filterArray = Imagefilter.hue(pixelArray)

        image.pixelArray = filterArray*strength + pixelArray*(1-strength)
        return image

    @classmethod
    def applyToCopy(cls,image:Image,Imagefilter:Filter,strength:float = 1.0) -> Image:
        """Universal pipeline to apply Filters to Copy of Image.\n Both pixel level and large scale pixel value manipulation possible using given Strength"""
        return cls.apply(image.copy(),Imagefilter,strength)


    def __init__(self):self.massApply:bool = True

    def init(self):pass
    
    def imageSize(self,size = (0,0)):
        self.width = size[1]
        self.height = size[0]

    def config(self):pass

    def hue(self,y:int,x:int,colour = (0,0,0))->xp.ndarray:    #returns colour
        """Returns a fresh filterArray with all filter applied to be applied on the original Image using given strength"""
        pass
        

class Vignette(Filter):
    def __init__(self,relativeRadius = 0,relativeCenter:tuple[float,float] = None,p = 2):
        super().__init__()
        self.config(relativeRadius,relativeCenter,p)

    def config(self,relativeRadius = 0,relativeCenter:tuple[float,float] = None,p = 2): # its 0 for smaller dimention 1 for larger dimmention and other range extrapolate
        self.rRadius = relativeRadius
        self.rCenter = relativeCenter
        self.parameterP = p

    def init(self):
        self.massApply=True
        if self.width!=0 and self.height!=0 and self.rCenter is None:
            self.center = (self.width//2,self.height//2)
        else:
            self.center = (self.width*self.rCenter[0],self.height*self.rCenter[1])
        a = min(self.width,self.height)//2
        b = max(self.width,self.height)//2
        self.radius = a + self.rRadius*(b-a)

    def hue(self,pixelArray:xp.ndarray)->xp.ndarray:
        Y,X = xp.indices(pixelArray.shape[0:2]).astype(xp.float32)
        distance = xp.sqrt((X-self.center[0])**2 + (Y-self.center[1])**2)
        v = xp.exp(-self.parameterP * (distance/self.radius)**4)
        filterArray:xp.ndarray =  pixelArray*v[:,:,None]
        return filterArray

class Grayscale(Filter):
    def __init__(self,mode=0):
        super().__init__()
        if (type(mode)==int and mode == 0) or (type(mode)==str and mode.lower() == "mean"):
            self.mode = 0
        if (type(mode)==int and mode == 1) or (type(mode)==str and mode.lower() == "median"):
            self.mode = 1

    def hue(self,pixelArray:xp.ndarray)->xp.ndarray:
        if self.mode == 0:
            filterArray:xp.ndarray = xp.mean(pixelArray,axis=2,keepdims=True)
        elif self.mode == 1:
            filterArray:xp.ndarray = xp.median(pixelArray,axis=2,keepdims=True)
        return filterArray
        
class ComplementaryMean(Filter):
    def hue(self,pixelArray:xp.ndarray)->xp.ndarray:
        RArray:xp.ndarray = xp.mean(pixelArray[:,:,1:3],axis=2,keepdims=True)
        GArray:xp.ndarray = xp.mean(pixelArray[:,:,[0,2]],axis=2,keepdims=True)
        BArray:xp.ndarray = xp.mean(pixelArray[:,:,0:2],axis=2,keepdims=True)
        filterArray = xp.concatenate((RArray,GArray,BArray),axis=2)
        return filterArray
    
class Negative(Filter):
    def hue(self,pixelArray:xp.ndarray)->xp.ndarray:
        filterArray = 255-pixelArray
        return filterArray
    
class ColourFilter(Filter):
    def __init__(self,rgbColour = (0,0,0)):
        self.massApply = True
        self.colour = rgbColour

    def hue(self,pixelArray:xp.ndarray)->xp.ndarray:
        filterArray = xp.full_like(pixelArray,self.colour)
        return filterArray


# def grayscale(colour):
#     return (sum(colour)//3,)*3

# def negative(colour):
#     return tuple([255-x for x in colour])

# def edgeGlow(ixputFileName):
#     Ixput = Image.open(ixputFileName)
#     width,height = Ixput.size
#     Output = Image.new("RGB",(width,height))

#     pixelIn = Ixput.load()
#     pixelOut = Output.load()

#     limit = 70
#     for i in range(width):
#         for j in range(height):
#             colour = pixelIn[i,j]
#             if i < limit or i >= width-limit or j < limit or j >= height-limit:pass
#             else:
#                 avg = [0,0,0]
#                 for x in range(i-1,i+2):
#                     for y in range(j-1,j+2):
#                         avg[0] += pixelIn[x,y][0]
#                         avg[1] += pixelIn[x,y][1]
#                         avg[2] += pixelIn[x,y][2]
#                 avg = [comp//25 for comp in avg]
#                 colour = [
#                     min(255,int(comp + ((comp - avg[z]) ** 2) / 255))
#                     if comp - 50 > avg[z]
#                     else comp
#                     for z, comp in enumerate(colour)
#                 ]
#             pixelOut[i,j] = tuple(colour)

#     Output.save("Output\\New.jpg")
