import random

Cmptr=0
Usr=0

Option= ["rock" ,"paper","siccors"]


while True : 
   User=input("Type:  Rock / Paper / Scissor   (Q = Quit) : ").lower()
   if User == "q":
      print("You : ",Usr," - ",Cmptr," : Computer")
      break
   elif User not in Option:
     continue
 
   Computer = random.randint(0,2)
 
   if (User=="rock") & (Option[Computer]=="siccors"):
            print("You : ",User," - ",Option[Computer]," : Computer")
            print ("You Won !!!")
            Usr+=1
          
   elif (User=="siccors") & (Option[Computer]=="paper"):
            print("You : ",User," - ",Option[Computer]," : Computer")
            print ("You Won !!!")
            Usr+=1
           
   elif (User=="paper") & (Option[Computer]=="rock"):
            print("You : ",User," - ",Option[Computer]," : Computer")
            print ("You Won !!!")
            Usr+=1
           
   else :
         print("You : ",User," - ",Option[Computer]," : Computer")
         print ("You Lost !!!")
         Cmptr+=1
        
        
         
