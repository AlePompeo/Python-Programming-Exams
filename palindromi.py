def palindromo(str): 
  if reverse(str) == str: 
    return True 
  else: 
    return False 

def reverse(str): 
  reversed = "" 
  for i in range(len(str)-1, -1, -1): 
   reversed += str[i]  
  return reversed 