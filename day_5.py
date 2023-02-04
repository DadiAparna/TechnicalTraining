def total(a,b):
    result=(a+b)
    result2=(a-b)
    print("function result is",result)
    print("function result is",result2)
a=int(input("enter the value of a"))
b=int(input("enter the value of b"))
total(a,b)


#--------------simple function-------------------#

def total(a,b):
    result=(a+b)
    print("function result is",result)
def diff(a,b):
    result=(a-b)
    print("function result2 is",result)
a=int(input("enter the value of a"))
b=int(input("enter the value of b"))
total(a,b)
diff(a,b)
   

#-----------------multiple functions-------------#

def total(a,b):
    result=(a+b)
    
    print("function result is",result)
def diff(a,b):
    result2=(a-b)


    print("function result is",result2)

def multi(a,b):
    result3=(a*b)
    
    print("function result is",result3)  

def div(a,b):
    result4=(a//b)
    
    print("function result is",result4)  



a=int(input("enter the value of a"))
b=int(input("enter the value of b"))
total(a,b)
diff(a,b)
multi(a,b)
div(a,b)

# --------------------actual and formal arg-------------#

def total(a,b):
    result=(a+b)
    
    print("function result is",result)
def diff(a,b):
    result2=(a-b)


    print("function result is",result2)


x=int(input("enter the value of a"))
y=int(input("enter the value of b"))
total(x,y)
diff(x,y)


def aparna(money):
    print("give aparna the sum of",money)

aparna(100)  


'''def aparna(money):
    print("give aparna the sum of",money)

aparna(10*4)'''


#------------global & local variable----------------------#


var="aparna"
def show():
    global var1
    var1='short'
    print("in function var is" ,var)
show()
print("ouside function",var1)
print("var is",var)  

#---------------nested function-----------------------#


def outf():
    var=10
    def inf():
        var=20
        print("inner var",var)
    inf()
    print("outer var",var)  
outf()  



#---------------return function-------------#

def cube(x):
    return(x**3)

x=10
result=cube(x)
print("output of the evaluation is",result)


#-------------------summation of numbers------------#

def add(x):
    return((x[0]+x[1]+x[2]+x[3]+x[4]+x[5]))



x=8,6,4,2,10,0
result=add(x)
print("summation of",result)


def display(name,age):
    print("name",name)
    print("age",age)
n="aparna"
y=77
display(name=n,age=y)

#-----------fibonacci series-------------------------#

def fib(n):
    if n<2:
        return 1
    return (fib(n-1) + fib(n-2))
n=int(input(""))
for i in range (n):
    print("fibonacci (" ,i,")" ,fib(i))    



a=[1,2,3]
b=[]
c=[]
a


#-------------------------------execution time-----------------------#

from time import *
t1 = perf_counter()
i=sum=0
while i<1000000:
    sum+=i
    i+=1
sleep(0)
t2 = perf_counter()
print("execution time = %f seconds" %(t2-t1))


#-------------------poles&discs-------------------------#

def hanoi(n,a,b,c):
    if n>0:
        hanoi(n-1,a,c,b)
        if a:
            c.append(a.pop())
        hanoi(n-1,b,a,c)    
a=[1,2,3,4]
b=[]
c=[]
print("before puzzle")
print(a,b,c)
hanoi(len(a),a,b,c)
print("after puzzle")
print(a,b,c)


#-------------------------------- date--------------------------------#


from datetime import *
d = date.today()
print(d)
d=date(2023,2,3)
for x in range(1,10):
    nextdate = d + timedelta(days=x)



#---------------------------------Strong number-------------------------------------#    
  


def factorial(d):
   if(d==1 or d==0):
      return 1
   return d*factorial(d-1)
def isStrong(n):
   num=n
   sum=0
   while(n>0):
      digit=n%10
      sum=sum+factorial(digit)
      n=n//10
   if(sum==num):
      return ("it is a strong number")
   else:
      return ("not a strong number")
print("Enter the number:")
d=int(input())
print(isStrong(d))





 

  










