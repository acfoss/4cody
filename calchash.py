import hashlib 
 
def hash_file(filename): 
   
  """
  Calculates and returns the SHA-1 hash of the file.
  
  Parameters:
    filename (str): The path to the file to hash
    
  Returns:
    str: The hexadecimal string representation of the SHA-1 hash
  """
 
   # make a hash object 
   h = hashlib.sha1() 
 
   # open file for reading in binary mode 
   with open(filename,'rb') as file: 
 
       # loop till the end of the file 
       chunk = 0 
       while chunk != b'': 
           # read only 1024 bytes at a time 
           chunk = file.read(1024) 
           h.update(chunk) 
 
   # return the hex representation of digest 
   return h.hexdigest() 
 
message = hash_file("track1.mp3") 
print(message) 
