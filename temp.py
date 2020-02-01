#how many coin need to fullfil the need by coin of 5 and 1.
five=int(input())
one=int(input())
amount=int(input())
temp=amount//5
temp2=amount-5*temp
if(amount==((5*temp)+temp2)):   
    print("no. of 5s:",temp,"no. of 1s",temp2)
else:  
    print("-1")
    
    
    
    
    
