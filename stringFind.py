def listGenerator(str):
    space = " "
    newStr = ""
    arr = []
    for i in range(0, len(str)):
        if str[i]!= space:
            newStr += str[i]
        elif str[i] == space:
            arr.append(newStr)
            newStr = ""
    arr.append(newStr)
    return arr

"""
def counter(str, toFind):
    newArr = listGenerator(str)
    for i in range(0 , len(newArr)):
        if newArr[i] == toFind:
            for j in range(0, len(str)):
"""
                
def find(s,ch): 

 #@param s: String 

 #@param ch: String 

 #return int 

   L=len(ch) 

   for i in range(0,len(s)-L+1): 

      if s[i:i+L]==ch: 

          return i 

   return -1 
   
   
ciao = "welcome to favelas"
o = "to"
print(find(ciao, o))
        

