# -*- coding: utf-8 -*-
"""
Created on Tue May 22 15:31:46 2018

@author: ZLiu
"""

import math 
import numpy as np 
import matplotlib.pyplot as plt 

def factor_matrix(N):
    factor = -2 * np.eye(N) + np.eye(N,k=1) + np.eye(N,k=-1)
    factor[0][0] = -1    
    factor[N-1][N-1] = -1
    factor[N-1][N-2] = 1
    return factor

import pandas as pd 
#def motion_monitor(N,time):
    #initialize parameter
N = 38
mass = 0.048  #kg 
n_spring = N      # number of springs
n_ball = n_spring +1# divided into n ball 
g = 9.8     # m/s/s
k = 0.22       #hook factor   
springl = []
position = []

x=np.zeros(N+1)
factor = factor_matrix(N+1)       # factor matrix 
# spring extension length 
for i in range(N):
    springl.append((n_spring-i)*mass*g/k/(n_spring*n_ball))
# calculate ball position 
for i in range(N+1):
    position.append(sum(springl[:i]))
print ("original length of spring %f"%position[N])
    
time = 0.5  # second
deltaT = 0.00001
topballposition = []
bottomballposition = []
acceleratelist = []
timelist = [] 
v_after_list = []
distance_list = []
position_list = []
velocity_before = np.zeros(N+1)
time_four = np.zeros(5)
for i in range(30000):
    # accelerate
    accelerate =  (N+1)*N*k/mass*np.dot(factor,position) + g 
    acceleratetemp = [accelerate[0], accelerate[int(N/4)],accelerate[int(N/2)],accelerate[int(N*3/4)],accelerate[N]]
    acceleratetemp = [accelerate[0],accelerate[1]]
    acceleratelist.append(acceleratetemp)
    # velocity  
    velocity_after = velocity_before + deltaT * accelerate  
    v_aftertemp = [velocity_after[0],velocity_after[int(N/4)], velocity_after[int(N/2)], velocity_after[int(N*3/4)], velocity_after[N]]
    v_aftertemp = [velocity_after[0],velocity_after[1]]
    v_after_list.append(v_aftertemp)
    # distance 
    distance = velocity_before*deltaT + 0.5* accelerate*deltaT*deltaT
    acceleratetemp = [distance[0],distance[int(N/4)],distance[int(N/2)],distance[int(3/4*N)],distance[int(N)]]
    distance_list.append(acceleratetemp)
    #position 
    position = position + distance    
    positiontemp = [position[int(0)],position[int(N/4)],position[int(N/2)],position[int(N*3/4)],position[int(N)]]
    positiontemp = [position[int(0)],position[1]]
    position_list.append(positiontemp)
    velocity_before = velocity_after

    x = x + 0.01
    
#    print ("i=%d,distance=%f"%(i,accelerate[-1]))
    timelist.append(deltaT*(i+1))
#    plt.pause(0.01)
accelerate_pd = pd.DataFrame(position_list,index = timelist)

accelerate_pd.plot()
#accelerate_pd.to_csv('./velocity')


plt.ylabel('N=%d'%N)
plt.grid(True)

