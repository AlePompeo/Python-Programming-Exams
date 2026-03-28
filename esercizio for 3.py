def colorePix(myPict):
    print "in alto a sinistra:", getColor(getPixel(myPict,0,0)), "in basso a destra:", getColor(getPixel(myPict,getWidth(myPict)-1,getHeight(myPict)-1))

colorePix(makePicture(pickAFile()))