import math 
import numpy as np 
import matplotlib.pyplot as plt 

def factor_matrix(N):
    factor = -2 * np.eye(N) + np.eye(N,k=1) + np.eye(N,k=-1)
    factor[0][0] = -1 
    factor[N-1][N-1] = -1
    factor[N-1][N-2] = 1
    return factor

def k_correction(delta_x, l, k_pos, k_neg): 
    force = (delta_x-l)*k_pos if delta_x>=l else (delta_x-l)*k_neg 
    return force

import pandas as pd 

#initialize parameter
l = 0.058       # original length
N = 2  
mass = 0.2155  #kg 
n_spring = N      # number of springs
n_ball = n_spring +1# divided into n ball 
g = 9.8     # m/s/s
k = 0.69       #hook factor   
springl = []
position = []

x=np.zeros(N+1)
factor = factor_matrix(N+1)       # factor matrix 

for i in range(N):
    springl.append((n_spring-i)*mass*g/k/(n_spring*n_ball)+l/N)
for i in range(N+1):
    position.append(sum(springl[:i]))
print ("original length of spring %f"%position[N])

plt.cla()

p_list=[]
v_list=[]
a_list=[] 
t_list=[]
accelerate = np.zeros(N+1)
v_before = np.zeros(N+1)
time = np.ones(3)
deltaT = 0.001
hit = 0
delta_x=np.zeros(N)
T_spring=np.zeros(N)
for i in range(10000): 
    p_list.append((position[0],position[int(N/2)],position[-1]))
    v_list.append((v_before[0],v_before[int(N/2)],v_before[-1]))
    a_list.append((accelerate[0],accelerate[int(N/2)],accelerate[-1]))
    t_list.append(time*i*deltaT)
    # correction needed 
#    for i in range(N):
#        if(position[i+1]-position[i]) < l/N :
#            hit = hit+1
#            position[i] = position[i+1] -l/N 
#            v_before[i] = (i+1)/(i+2)*v_before[i] + 1/(i+2)*v_before[i+1]
#            v_before[i+1] = v_before[i]
    # corrction ended 
    for i in range(N):
        delta_x[i] = position[i+1]-position[i]
        T_spring[i] = k_correction(delta_x[i], l/N,k,1*k)
    for i in range(N-1): 
        accelerate[i+1] = g + (T_spring[i+1]-T_spring[i])/(mass/(N+1)) 
    accelerate[0] = g + (T_spring[0])/(mass/(N+1)) 
    accelerate[N] = g - (T_spring[N-1])/(mass/(N+1))
    v_after = v_before + accelerate*deltaT
    position = position + v_before*deltaT + 0.5* accelerate*deltaT*deltaT
    v_before = v_after   

plt.subplot2grid((3,1),(0,0))
plt.scatter(t_list,a_list,marker ='.',c=('r','g','b') )
plt.ylabel("acceleration")

plt.subplot2grid((3,1),(1,0))
plt.scatter(t_list,v_list,marker ='.',c=('r','g','b') )
plt.ylabel("velocity")  

plt.subplot2grid((3,1),(2,0))
plt.scatter(t_list,p_list,marker ='.',c=('r','g','b') )
plt.ylabel("position")

print(hit)

