
#series(0,0,7,6,14,12,21,28....)
term = int(input("enter the term"))
if term %2==0:
    term=term//2
    print(6*(term-1))
else:
     term=term//2+1
     print(7*(term-1))


#armstrong number 3-digit     
num = int(input("enter the 3 digit number"))
sum = 0
i = num
while i > 0:

    n = i % 10
    sum += n*n*n
    i = i//10

if (num == sum):
    print('it is a armstrong number')
else:
    print('it is not a armstrong number')



#armstrong number 4-digit

num = int(input("enter the number"))
sum = 0
i = num
while i > 0:
    n = i % 10
    sum += n**4
    i = i//10

if(num==sum):
    print('it is a armstrong number')
else:
    print('it is not a armstrong number')


#armstrong number 4-digit

num = int(input("enter the number"))
number=len(str(num))
sum = 0
i = num
while i > 0:
    n = i % 10
    sum += n**(number)
    i = i//10

if(num==sum):
    print('it is a armstrong number')
else:
    print('it is not a armstrong number')


#geometric series(1,1,2,3,4,9,8,27,16,81...find 13th &16th term)

term=int(input("enter the term:"))
if term%2 ==0:
     term=term//2
     print(3**(term-1))
else:
    term=term//2+1
    print(2**(term-1))
         
    
