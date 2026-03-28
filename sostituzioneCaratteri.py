def sostituzioni(s): 
#@param s: string 
#@return string 
 for i in range(0,len(s)): 
   if s[i]!=' ': 
    for x in range(i+1,len(s)): 
     if s[x]==s[i]: 
      s=s[0:x]+'*'+s[x+1:] 
 return s 
