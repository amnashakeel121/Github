#Task no.1
#print numbers from 1 to 10 using for loop
for x in range (1,11):
                  print(x)
#Task.no 2  
#print numbers from 1 to 5 using while loop 
x= 1
while x<=5:
   print(x)
   x+=1
 #Task no.3
y=int(input("set the count:"))
while y>=0:
  print(y) 
  y-=1
     #Task no.4
  # nested loop
for i in range (1, 4):
 for j in range (1, 4):
           print (i,"*", j,"=", i*j)
 else: 
     print("") 
 #Task no 5
 #print the 0,10 using break
for x in range(10):
 if x==6:
  break  
  print(x)
 #Task.no 6    
for x in range(5):
 if x==3:
  continue
  print(x) 
 #Bonus Task
 name=" Atta ur Rehman"
for z in name:
   if z == " ":
       print()
   else: 
      print(z, end="")   
        
    
      
  
       