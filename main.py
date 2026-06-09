import math
from filters import *
from effects import *
from utilities import Image

def main():
    Input = Image("test1.jpg")
    vinn = Vignette(0,(0.5,0.5),8)
    Filter.applyToCopy(Input,vinn).save("Output\\New8.jpg")
    vinn.config(0,(0.5,0.5),4)
    Filter.applyToCopy(Input,vinn).save("Output\\New4.jpg")
    vinn.config(0,(0.5,0.5),2)
    Filter.applyToCopy(Input,vinn).save("Output\\New2.jpg")
    vinn.config(0,(0.5,0.5),1.5)
    Filter.applyToCopy(Input,vinn).save("Output\\New1_5.jpg")
    vinn.config(0,(0.5,0.5),1)
    Filter.applyToCopy(Input,vinn).save("Output\\New1.jpg")
    vinn.config(0,(0.5,0.5),0.5)
    Filter.applyToCopy(Input,vinn).save("Output\\New0_5.jpg")
    vinn.config(0,(0.5,0.5),0)
    Filter.applyToCopy(Input,vinn).save("Output\\New0.jpg")
    


if __name__ == "__main__":main()
