# main.py
from filters import *
from effects import *
from utilities import *
from styles import *
import math

def main():
    Input = Image("test1.jpg")
    Filter.applyToCopy(Input,ColourFilter(),0.7).save("Output\\newImage2.jpg")
    myStyle = Style("MyStyle1")
    myStyle.addProcess(Style.Process(ComplementaryMean(),MaskSet(EllipseMask((0.5,0.5),(0.42,0.42),Gradient(lambda x:x),math.pi/16),RectangularMask((0.26,0.26),(0.44,0.44),Gradient(lambda x:x**2,0.1))),0.95))
    myStyle.addProcess(Style.Process(Grayscale(1),MaskSet(EllipseMask((0.5,0.5),(0.42,0.42),Gradient(lambda x:x),math.pi/16),RectangularMask((0.26,0.74),(0.44,0.44),Gradient(lambda x:x,0.25)))))
    myStyle.addProcess(Style.Process(Negative(),MaskSet(EllipseMask((0.5,0.5),(0.42,0.42),Gradient(lambda x:x),math.pi/16),RectangularMask((0.74,0.26),(0.44,0.44),Gradient(lambda x:3*x**2 + x,0.2))),1))
    myStyle.addProcess(Style.Process(Vignette(0.25,(0.74,0.74),8),MaskSet(EllipseMask((0.5,0.5),(0.42,0.42),Gradient(lambda x:x),math.pi/16),RectangularMask((0.74,0.74),(0.44,0.44),Gradient(lambda x:3*x**2 + x,0.2)))))
    myStyle.addProcess(Style.Process(ColourFilter((50,125,210)),
                                     MaskSet(
                                         RectangularMask((0.5,0.5),(0.95,0.92)),
                                         EllipseMask((0.5,0.5),0.63),
                                         inverse=True
                                     ),
                                     0.0
                                     ))

    myStyle.apply(Input,
                  MaskSet(
                      MaskSet(
                          EllipseMask((0.5,0.5),(0.15,0.15),Gradient(lambda x:x,0.5),math.pi*11/12,True),
                          EllipseMask((0.5,0.5),(0.42,0.42),Gradient(lambda x:x),math.pi/16),
                          inverse=True
                          ),
                      RectangularMask((0.5,0.5),(0.95,0.92)),
                      EllipseMask((0.5,0.5),0.55),
                      inverse=True
                  )).save("Output\\newImage.jpg")


if __name__ == "__main__":main()
