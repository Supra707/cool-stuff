import random
l=[]
while(True):
    i=input()
    if(i=='###'):
        break
    l.append(i)
randchoice=random.randint(0,len(l)-1)
compuchoice=l[randchoice]
print(compuchoice)
n=int(input("Enter the number of users guesses: "))
k=1

l1=[]
while(k<=n):
    count=0
    user=input("User,enter your guess: ")
    for j in compuchoice:
        if(j in user):
            l1.append(j)
            count=count+1
    if(count==0):
        print("."*len(user))

    elif(count<len(compuchoice) or count>len(compuchoice)):
        print("The matching letters are: ")
        print(l1)
        for j in range(0,len(l)):
            count1=0 
            for i in range(0,len(l1)):
                
                if(l1[i] in l[j]):
                    count1=count1+1
            if(count1==len(l1)):
                print(l[j])
        l1.clear()
    elif(compuchoice==user):
        print("Guessed it right")
        l1.clear()
    
    k=k+1






