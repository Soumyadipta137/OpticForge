from PIL import Image
import math

def vineatte(pos,colour,size,rad = 0):      #rad = 0 means lower dimension edge,rad = 1 larger dim edge
    center = (size[0]//2,size[1]//2)
    p = 2
    a = min(size[0],size[1])//2
    b = max(size[0],size[1])//2
    rad = a +rad*(b-a)
    distance = ((pos[0]-center[0])**2 + (pos[1]-center[1])**2)**0.5
    v = math.exp(-p * (distance/rad)**4)
    newColour = tuple([int(x*v) for x in colour])
    return newColour

def grayscale(colour):
    return (sum(colour)//3,)*3

def negative(colour):
    return tuple([255-x for x in colour])

def edgeGlow(inputFileName):
    Input = Image.open(inputFileName)
    width,height = Input.size
    Output = Image.new("RGB",(width,height))

    pixelIn = Input.load()
    pixelOut = Output.load()

    limit = 70
    for i in range(width):
        for j in range(height):
            colour = pixelIn[i,j]
            if i < limit or i >= width-limit or j < limit or j >= height-limit:pass
            else:
                avg = [0,0,0]
                for x in range(i-1,i+2):
                    for y in range(j-1,j+2):
                        avg[0] += pixelIn[x,y][0]
                        avg[1] += pixelIn[x,y][1]
                        avg[2] += pixelIn[x,y][2]
                avg = [comp//25 for comp in avg]
                colour = [
                    min(255,int(comp + ((comp - avg[z]) ** 2) / 255))
                    if comp - 50 > avg[z]
                    else comp
                    for z, comp in enumerate(colour)
                ]
            pixelOut[i,j] = tuple(colour)

    Output.save("Output\\New.jpg")

def fisheye(x,y,relativeRadius = 0.8,rIndex = 0.85):
    #relativeRadius that many times the lower value (rad of circle fish eye makes)
    # rIndex is ratio of rad/roc(radius of curvature of fish eye) rIndex = -> semicircle
    
    Input = Image.open("grid.jpg")
    width,height = Input.size
    print(width,height)
    Output = Image.new("RGB",(width,height))
    pixelIn = Input.load()
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
    
    Input = Image.open("grid.jpg")
    width,height = Input.size
    print(width,height)
    Output = Image.new("RGB",(width,height))
    pixelIn = Input.load()
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

def main():
    Input = Image.open("luffy.jpg")
    width,height = Input.size
    print(width,height)
    Output = Image.new("RGB",(width,height))

    pixelIn = Input.load()
    pixelOut = Output.load()

    for i in range(width):
        for j in range(height):
            colour = pixelIn[i,j]
            # pixelOut[i,j] = vineatte((i,j),colour,(width,height),1)
            pixelOut[i,j] = grayscale(colour)

    Output.save("Output\\New.jpg")

if __name__ == "__main__":fisheye(311,175)