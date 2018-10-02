while True:
 print("Enter 1 for encryption")
 print("Enter 2 for decryption")
 print("Other option to exit")
 ch=int(input("Enter your choice:"))
 if(ch==1):
  print("******************************ENCRYPTION*********************************")
  Matrix = [[0 for x in range(5)] for y in range(5)] 
  key=input("Enter key:");
  key=list(key) #convert key to list
  lstKey= []
  key = [w.replace('i', 'j') for w in key]
  for el in key:            #removing duplicates elements from the list
   if el not in lstKey:
    lstKey.append(el)
  c2='j'
  j=0
  k=0
  for i in lstKey[:]:        #inserting into 5*5 matrix
   Matrix[k][j]=i
   j=j+1
   if(j==5):
    j=0
    k=k+1
  if(c2 in lstKey):
   a=['a','b','c','d','e','f','g','h','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
  else:
   a=['a','b','c','d','e','f','g','h','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
  for m in lstKey[:]: #check for the common elements in the key and list 'a' and remove them
   for n in a[:]:
    if(m==n):
     a.remove(n)
  i=0
  for i in a[:]: #Insert the elements in 'a' into the matrix
   Matrix[k][j]=i
   j=j+1
   if(j==5):
    j=0
    k=k+1
  pt=input("Enter plain text:") #takes plain text as input
  pt=pt.replace(" ", "")
  pt=list(pt) 
  pt = [w.replace('i', 'j') for w in pt]
  for p in range(0,len(pt)+1): #check if plain text contains adjacent duplicates, if so append 'x'
   if(p+1>=len(pt)):
    break;
   elif(pt[p]==pt[p+1]):
    pt.insert(p+1,'x')
  print(pt) 
  sp=[pt[i:i+2] for i in range(0, len(pt), 2)] #split the plain text as bunch of 2 chars
  cipher=[]
  for i in sp[:]:  
   ls=list(i)     #convert each 2 char piece of plain text into a list
   if(len(ls)==1): #if the last element is left, add 'x' to it
    ls.append('x')
   c=0
   w=0
   x=0
   y=0
   z=0
   for t in ls:
    for i in range(0,5):
     for j in range(0,5):
      if(Matrix[i][j]==t):
       if(c==0):
        x = j
        w = i 
        c=c+1
       else:
        z = j 
        y = i    
   if(w==y):
    x = (x + 1) % 5  
    z = (z + 1) % 5 
    cipher.append(Matrix[w][x])
    cipher.append(Matrix[y][z])
   elif(x==z):
    w = (w + 1) % 5 
    y = (y + 1) % 5  
    cipher.append(Matrix[w][x])
    cipher.append(Matrix[y][z])
   else:
    cipher.append(Matrix[w][z])
    cipher.append(Matrix[y][x])
  print("The cipher text for the given Plain text is:")
  cipherText = ''.join(cipher)
  print(cipherText)
 elif(ch==2):
  print("************************************DECRYPTION**************************************")
  Matrix1 = [[0 for x in range(5)] for y in range(5)] 
  lstKey= []
  for el in key:            #removing duplicates elements from the list
   if el not in lstKey:
    lstKey.append(el)
  c2='j'
  j=0
  k=0
  for i in lstKey[:]:        #inserting into 5*5 matrix
   Matrix[k][j]=i
   j=j+1
   if(j==5):
    j=0
    k=k+1
  if(c2 in lstKey):
   a=['a','b','c','d','e','f','g','h','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
  else:
   a=['a','b','c','d','e','f','g','h','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
  for m in lstKey[:]: #check for the common elements in the key and list 'a' and remove them
   for n in a[:]:
    if(m==n):
     a.remove(n)
  i=0
  for i in a[:]: #Insert the elements in 'a' into the matrix
   Matrix[k][j]=i
   j=j+1
   if(j==5):
    j=0
    k=k+1
  pt=cipherText #takes plain text as input
  pt=pt.replace(" ", "")
  pt=list(pt) 
  sp=[pt[i:i+2] for i in range(0, len(pt), 2)] #split the plain text as bunch of 2 chars
  plain=[]
  for i in sp[:]:  
   ls=list(i)     #convert each 2 char piece of plain text into a list
   if(len(ls)==1): #if the last element is left, add 'x' to it
    ls.append('x')
   c=0
   w=0
   x=0
   y=0
   z=0
   for t in ls:
    for i in range(0,5):
     for j in range(0,5):
      if(Matrix[i][j]==t):
       if(c==0):
        x = j
        w = i 
        c=c+1
       else:
        z = j 
        y = i    
   if(w==y):
    x = (x - 1) % 5  
    z = (z - 1) % 5 
    plain.append(Matrix[w][x])
    plain.append(Matrix[y][z])
   elif(x==z):
    w = (w - 1) % 5 
    y = (y - 1) % 5  
    plain.append(Matrix[w][x])
    plain.append(Matrix[y][z])
   else:
    plain.append(Matrix[w][z])
    plain.append(Matrix[y][x])
  print("The plain text for the given cipher text is:")
  plainText = ''.join(plain)
  print(plainText)
 else:
  quit();