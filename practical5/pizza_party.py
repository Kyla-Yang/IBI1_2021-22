n=0
#The cutting number, n, is from 1 to infinity so in the while-loop, the 
#first n printed out is 1, which causes n is 0 at the beginning.
p=0
#The slice number, p, is introduced into this one as a variable by the 
#codes "p=0".
while p<64:
    n=n+1
    p=(n ** 2+n+2)/2
#The equation tells the relatinoship between n and p.
    print("The cutting number is",n,"and the slice number is",p)
