import math
from PIL import Image


def fisheye(x,y,relativeRadius = 0.8,rIndex = 0.85):
    #relativeRadius that many times the lower value (rad of circle fish eye makes)
    # rIndex is ratio of rad/roc(radius of curvature of fish eye) rIndex = -> semicircle
    
    Ixput = Image.open("grid.jpg")
    width,height = Ixput.size
    print(width,height)
    Output = Image.new("RGB",(width,height))
    pixelIn = Ixput.load()
    pixelOut = Output.load()

    VIEW_DIST = 650 # distance viewer is from the image
    CIRCULAR_RADIUS = relativeRadius*(min(width,height)/2) #radius of fisheye on screen
    RADIUS_OF_CURVATURE = CIRCULAR_RADIUS/rIndex

    for i in range(width):
        for j in range(height):
            dist = ((i-x)**2 + (j-y)**2)**0.5
            if (i==x and j==y) or dist>CIRCULAR_RADIUS:
                pixelOut[i,j] = pixelIn[i,j]
                continue
            a = 1 + ((VIEW_DIST/dist)**2)
            b = (dist - (VIEW_DIST/dist)*((RADIUS_OF_CURVATURE**2 - CIRCULAR_RADIUS**2)**0.5))
            c = dist**2 - CIRCULAR_RADIUS**2
            s = (b+(b**2 - a*c)**0.5)/a
            # s = abs(s)

            theta = math.atan2(j - y, i - x)
            X = i - s * math.cos(theta)
            Y = j - s * math.sin(theta)

            pixelOut[i,j] = pixelIn[int(X),int(Y)]

    Output.save("Output\\New.jpg")

def halfFishEye(x,y,relativeRadius = 0.8,rIndex = 0.85):
    #relativeRadius that many times the lower value (rad of circle fish eye makes)
    # rIndex is ratio of rad/roc(radius of curvature of fish eye) rIndex = -> semicircle
    
    Ixput = Image.open("grid.jpg")
    width,height = Ixput.size
    print(width,height)
    Output = Image.new("RGB",(width,height))
    pixelIn = Ixput.load()
    pixelOut = Output.load()

    VIEW_DIST = 650 # distance viewer is from the image
    CIRCULAR_RADIUS = relativeRadius*(min(width,height)/2) #radius of fisheye on screen
    RADIUS_OF_CURVATURE = CIRCULAR_RADIUS/rIndex

    for i in range(width):
        for j in range(height):
            dist = ((i-x)**2 + (j-y)**2)**0.5
            if (i==x and j==y) or dist>CIRCULAR_RADIUS or i>x:
                pixelOut[i,j] = pixelIn[i,j]
                continue
            a = 1 + ((VIEW_DIST/dist)**2)
            b = (dist - (VIEW_DIST/dist)*((RADIUS_OF_CURVATURE**2 - CIRCULAR_RADIUS**2)**0.5))
            c = dist**2 - CIRCULAR_RADIUS**2
            s = (b+(b**2 - a*c)**0.5)/a
            # s = abs(s)

            theta = math.atan2(j - y, i - x)
            X = i - s * math.cos(theta)
            Y = j - s * math.sin(theta)

            pixelOut[i,j] = pixelIn[int(X),int(Y)]

    Output.save("Output\\New.jpg")
