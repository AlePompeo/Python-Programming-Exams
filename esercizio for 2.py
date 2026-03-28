def schiarisciDueVolte(pict): 
# @param pict: Picture 
    for p in getPixels(pict): 
        col = getColor(p) 
        lightCol = makeLighter(col)  
        lighterCol = makeLighter(lightCol) 
        setColor(p, lighterCol) 


myPict = makePicture(pickAFile())
schiarisciDueVolte(myPict) 