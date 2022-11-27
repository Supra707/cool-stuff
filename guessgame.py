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
i=1
count=0
l1=[]
while(i!=n):
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
            for i in range(0,len(l1)):
                count=0 
                if(l1[i] in l[j]):
                    count=count+1
                if(count==len(l1)):
                    print(l[j])
        l1.clear()
    elif(count==len(compuchoice)):
        print("Guessed it right")
    
i=i+1







