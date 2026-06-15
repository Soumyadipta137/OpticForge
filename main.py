# main.py
from filters import *
from transforms import *
from utilities import *
from styles import *
import math

def rectCornerMask(centerTuple):return RectangularMask(centerTuple,(0.44,0.44),Gradient(lambda x:x**2,0.1))

def main():
    Input = Image("Input\\test1.jpg")
    Input2 = Image("Input\\TestZoro.webp")
    ellipseMask1 = EllipseMask((0.5,0.5),(0.15,0.15),Gradient(lambda x:x,0.5),math.pi*11/12,True)
    ellipseMask2 = EllipseMask((0.5,0.5),(0.42,0.42),Gradient(lambda x:x),math.pi/16)
    concentricEllMask = MaskIntersection(ellipseMask1,ellipseMask2)
    borderMask = MaskIntersection(RectangularMask((0.5,0.5),(0.95,0.92)),EllipseMask((0.5,0.5),0.63),inverse=True)

    myStyle1 = Style("4Way")
    myStyle1.addProcess(Style.Process(ComplementaryMean(),rectCornerMask((0.26,0.26)),0.95))
    myStyle1.addProcess(Style.Process(Grayscale(1),rectCornerMask((0.26,0.74))))
    myStyle1.addProcess(Style.Process(Negative(),rectCornerMask((0.74,0.26)),1))
    myStyle1.addProcess(Style.Process(Vignette(0.25,(0.74,0.74),8),rectCornerMask((0.74,0.74))))

    myStyle2 = Style("Focus")
    myStyle2.addProcess(Style.Process(ColourFilter((255,0,0)),CircleMask((0.5,0.5),0.2,Gradient(lambda x:x**2,1))))
    myStyle2.addProcess(Style.Process(ColourFilter((255,50,0)),CircleMask((0.5,0.5),0.15,Gradient(lambda x:x**2,1))))
    myStyle2.addProcess(Style.Process(ColourFilter((255,100,0)),CircleMask((0.5,0.5),0.10,Gradient(lambda x:x**2,1))))
    myStyle2.addProcess(Style.Process(ColourFilter((255,125,0)),CircleMask((0.5,0.5),0.05,Gradient(lambda x:x**2,1))))

    myStyle3 = Style("SunShine")
    myStyle3.addProcess(Style.Process(ColourFilter((255,100,0)),CircleMask((0.9,0.1),0.5,Gradient(lambda x:xp.sin(20*x**(2)*xp.pi/2),1)),0.5))
    myStyle3.addProcess(Style.Process(ColourFilter((255,0,0)),CircleMask((0.9,0.1),0.5,Gradient(lambda x:xp.sin((40*x**(2))*xp.pi/2 ),1)),0.25))
    myStyle3.addProcess(Style.Process(ColourFilter((255,100,0)),CircleMask((0.9,0.1),0.3,Gradient(lambda x:x**2,0.85))))
    myStyle3.addProcess(Style.Process(ColourFilter((255,150,0)),CircleMask((0.9,0.1),0.25,Gradient(lambda x:x**2,0.90))))
    myStyle3.addProcess(Style.Process(ColourFilter((255,200,0)),CircleMask((0.9,0.1),0.20,Gradient(lambda x:x**2,0.95))))
    myStyle3.addProcess(Style.Process(ColourFilter((255,255,0)),CircleMask((0.9,0.1),0.15,Gradient(lambda x:x**2,1))))

    myStyle = Style("MyStyle2")
    myStyle.addProcess(Style.Process(myStyle1,concentricEllMask))
    myStyle.addProcess(Style.Process(myStyle2))
    myStyle.addProcess(Style.Process(myStyle3))
    myStyle.addProcess(Style.Process(ColourFilter((50,125,210)),borderMask))

    myStyle.apply(Input).save("Output\\Luffy1.jpg")
    myStyle.apply(Input2).save("Output\\Zoro1.jpg")

if __name__ == "__main__":main()