from backend import xp
from utilities import Image

class Filter:
    @classmethod
    def apply(cls,image:Image,Imagefilter:Filter):
        """Universal pipeline to apply Filters to Original Image.\n Both pixel level and large scale pixel value manipulation possible"""
        if not isinstance(Imagefilter,Filter):raise TypeError("Only Accept filter type")
        pixelArray = image.pixelArray
        Imagefilter.imageSize(pixelArray.shape[0:2])
        Imagefilter.init()

        if not Imagefilter.massApply:
            for y in range(pixelArray.shape[0]):
                for x in range(pixelArray.shape[1]):
                    pixelArray[y,x] = Imagefilter.hue(y,x,pixelArray[y,x])

        else:
            pixelArray = Imagefilter.hue(pixelArray)

        image.pixelArray = pixelArray
        return image
    
    @classmethod
    def applyToCopy(cls,image:Image,Imagefilter:Filter):
        """Universal pipeline to apply Filters to Copy of Image.\n Both pixel level and large scale pixel value manipulation possible"""
        return cls.apply(image.copy(),Imagefilter)


    def __init__(self):self.massApply:bool = False

    def init(self):pass
    
    def imageSize(self,size = (0,0)):
        self.width = size[1]
        self.height = size[0]

    def config(self):pass

    def hue(self,y:int,x:int,colour = (0,0,0)):pass   #returns colour
        

class Vignette(Filter):
    def __init__(self,relativeRadius = 0,relativeCenter:tuple[float,float] = None,p = 2):
        super().__init__()
        self.config(relativeRadius,relativeCenter,p)

    def init(self):
        self.massApply=True
        if self.width!=0 and self.height!=0 and self.rCenter is None:
            self.center = (self.width//2,self.height//2)
        else:
            self.center = (self.width*self.rCenter[0],self.height*self.rCenter[1])
        a = min(self.width,self.height)//2
        b = max(self.width,self.height)//2
        self.radius = a + self.rRadius*(b-a)

    def config(self,relativeRadius = 0,relativeCenter:tuple[float,float] = None,p = 2): # its 0 for smaller dimention 1 for larger dimmention and other range extrapolate
        self.rRadius = relativeRadius
        self.rCenter = relativeCenter
        self.parameterP = p

    def hue(self,pixelArray:xp.ndarray):
        Y,X = xp.indices(pixelArray.shape[0:2]).astype(xp.float32)
        distance = xp.sqrt((X-self.center[0])**2 + (Y-self.center[1])**2)
        v = xp.exp(-self.parameterP * (distance/self.radius)**4)
        pixelArray =  pixelArray*v[:,:,None]
        return pixelArray.astype(xp.uint8)

class Grayscale(Filter):
    def __init__(self,brightness):
        super().__init__()
        self.config(brightness)

    def config(self):pass
        


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
