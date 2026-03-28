def existNTimes(s,c,n): 
  #@param s string 
  #@param c string 
  #@param n int 
  #@return bool     
  if n==0: 
    return True     
  if len(s)<=0: 
    return False   
  if s[0]==c: 
    n=n-1 
  return existNTimes(s[1:],c,n) 