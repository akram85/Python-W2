#Import
import math
import random
#import calendar

#Dynamic typing
n=10
n=n/2
print(n)
x,y =1,2
x,y=y,x
print(x,y)
x=10
# remove 
del x
#print(x)

#shorthand
count =0
count+=1
count*=2
print(count)
#in operators
print('a' in 'alpha')

#chaning
x=5
print(5==x>4)
#escape char
print('it\'s a day')
print('hello \t world')
print('hello \n world')
print('this is from "IITM"')
print("this is from 'IITM'")
z= '''first line
second line
third line'''
print(z)
'''multi line
comment'''
print(24%26)
#if else 
#age =int(input("Enter your #age :"))
age=30
if(age<10):
  print('age is less')
elif(age>10 and age<20):
  print('age is good')
else:
  print('age is higher')

#import
print(math.sqrt(16))
print(math.pow(10,3))
print(random.random())
print(random.randrange(1,7))
#print(calendar.calendar(2022))
