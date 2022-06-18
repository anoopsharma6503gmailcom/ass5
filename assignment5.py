#Ques 1
string=input("Enter the the string :")
print(string[::-1])
#solution 1
"""
Enter the the string :wycuydbcygqu
uqgycbdyucyw
"""

#Ques 2
x,y=(input("Enter the range of numbers: ").split())
num=int(input("Enter the number for divisibility: "))
x=int(x)
y=int(y)
for no in range(x,y+1):
    if no%num==0 :
        print(no)  
#solution
"""
Enter the range of numbers: 1 55
Enter the number for divisibility: 2
2
4
6
8
10
12
14
16
18
20
22
24
26
28
30
32
34
36
38
40
42
44
46
48
50
52
54
"""
#Ques 3
a=float(input("Enter the length of side:"))
b=float(input("Enter the length of side:"))
c=float(input("Enter the length of side:"))
if a+b>c and a+c>b and b+c>a :
    s=(a+b+c)/2
    ar_tri=(s*(s-a)*(s-b)*(s-c))**(0.5)
    print(ar_tri)
else :
    print("Error")
#solution 3
"""
Enter the length of side:10
Enter the length of side:12
Enter the length of side:14
58.787753826796276
"""
#ques 4
n=int(input("Enter the no. of rows :"))
t=(n//2)+1
l=n//2
for i in range(1,t+1):
    for j in range(1,i+1):
        print("*",end="")
    print()
for q in range(l,0,-1):
    for r in range(q,0,-1):
        print("*",end="")
    print()
#solution
"""
Enter the no. of rows :10
*
**
***
****
*****
******
*****
****
***
**
*
"""
#ques5
n=int(input("Enter number of rows: "))
p=ord("A")
for rows in range(1,n+1):
    for col in range(1,rows+1):
        print(chr(p),end="")
        p+=1
    print()
#solution 
"""
Enter number of rows: 5
A
BC
DEF
GHIJ
KLMNO
"""
#ques 6
high=int(input("Enter the maximum number of range: "))
low=int(input("Enter the minimum number of range: "))
for no in range(low,high+1):
    for i in range(2,no):
        if no%i==0:
            break
    else :
        print(no)
#solution
"""
Enter the maximum number of range: 98
Enter the minimum number of range: 1
1
2
3
5
7
11
13
17
19
23
29
31
37
41
43
47
53
59
61
67
71
73
79
83
89
97
"""
#ques 7
accum=[]
for i in range(1,500):
    if i%7==0 and i%11==0 :
        accum.append(i)
print("The numbers divisible by 11 and are multiple of 7 are :",accum)
"""
solution
The numbers divisible by 11 and are multiple of 7 are : [77, 154, 231, 308, 385, 462]
"""
#ques 8
pos=[]
neg=[]
odd=[]
even=[]
times={}
li=[]
for i in range(10):
    num=int(input("Enter the number "))
    li.append(num)
    if num>0:
        pos.append(num)
    elif num<0 :
        neg.append(num)
    if num%2==0 :
        even.append(num)
    else :
        odd.append(num)
    if num not in times :
            times[num]=1
    else:
        times[num]+=1
print("Positive numbers are: ",pos)
print("Negative numbers are: ",neg)
print("Even numbers are: ",even)
print("Odd numbers are: ",odd)
print("Number of times each number occurs in the List",times)
"""
solution
Enter the number 9
Enter the number 91
Enter the number 7
Enter the number 7
Enter the number -16
Enter the number -15
Enter the number -41
Enter the number 489
Enter the number 789
Enter the number -16
[9, 91, 7, 7, 489, 789]
[-16, -15, -41, -16]
[-16, -16]
[9, 91, 7, 7, -15, -41, 489, 789]
{9: 1, 91: 1, 7: 2, -16: 2, -15: 1, -41: 1, 489: 1, 789: 1}
"""
#ques 9
n=int(input("Number of words: "))
li=[]
for i in range(n):
    word=input("Enter the word: ")
    li.append(word)
times={}
for i in li :
    if i not in times :
        times[i]=1
    else :
        times[i]+=1
print("Number of occurences: ",times)
#solution
"""
Number of words: 8
Enter the word: My
Enter the word: Name
Enter the word: is
Enter the word: Ketan
Enter the word: PEC
Enter the word: ITC \
Enter the word: is
Enter the word: ITC
The list of words is:  ['My', 'Name', 'is', 'Anoop', 'PEC', 'ITC \\', 'is', 'ITC']
Number of occurences:  {'My': 1, 'Name': 1, 'is': 2, 'Anoop': 1, 'PEC': 1, 'ITC \\': 1, 'ITC': 1}
"""
