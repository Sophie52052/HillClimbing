# -*- coding: utf-8 -*-
"""
Created on Wed Oct  2 20:44:56 2019

@author: Sophie
"""

import sys
from functions import func

#catch filename
filename_in=sys.argv[1]
filename_out=sys.argv[2]

#file read 
file_in = open(filename_in, "r")
#file_in = open("input.txt", "r")
line=file_in.readlines()

#file write
file_out = sys.stdout                 
sys.stdout = open(filename_out, 'w')

x_left=int(line[0].split(",")[0])
x_right=int(line[0].split(",")[1])

y_left=int(line[1].split(",")[0])
y_right=int(line[1].split(",")[1])

num=int(line[2])


#Brute
res=[]
for x in range(x_left, x_right+1):
    for y in range(y_left, y_right+1):
        z = func(x,y)
        #print(z)
        res.append(z)
#print(res)
result='%.3f' % min(res)
print(result)     #-30.010
#print(len(res))   #12221
#res.index(min(res)) #min index


step_size=1

for i in range(3,num+3):
    x=int(line[i].split(",")[0])
    y=int(line[i].split(",")[1])
    #print (x)
    #print (y)
    count=0
    A=0
    B=0
    res1=[]
    z=func(x,y) #call 1
    while True:
        func_list=[func(x+step_size,y), func(x-step_size,y), func(x,y+step_size),func(x,y-step_size)]
        #left right front back -4(each)
        
        index=func_list.index(min(func_list)) 
        count+=1
        #print(x,y)
        if z>min(func_list):
            if index==0:
                x=x+step_size
            elif index==1:
                x=x-step_size
            elif index==2:
                y=y+step_size
            elif index==3:
                y=y-step_size
            z=min(func_list)
        else:
            result='%.3f' % func(x,y)
            
            #print((count-1)*4+1)
            print(result)
            break
        
        xy=[]
        xy.append(x)
        xy.append(y)
        res1.append(xy)
        if len(res1) >2:
            if xy == res1[len(res1)-3]:
                result='%.3f' % func(x,y)
                #print((count-1)*4+1)
                print(result)
                break
        else:
            continue
        
        
file_in.close()
sys.stdout.close()   
sys.stdout = file_out
