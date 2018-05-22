# -*- coding: utf-8 -*-
"""
Created on Tue May 22 15:31:46 2018

@author: ZLiu
"""

import math 

def time_calculation(n_point):   
    # initialize parameter
    mass = 0.1          #kg 
    n_spring = n_point              # number of springs
    n_ball = n_spring +1        # divided into n ball 
    g = 9.8             # m/s/s
    k = 1               #hook factor    
    t_l = []
    v_start = 0.0
    for i in range(n_spring): 
        n = i+1
        delta_l = (n_spring-i)*mass*g/k/(n_spring*n_ball)
        # gravity energy 
        E_g = (n/(n_ball)*mass*g*delta_l)
        # spring energy 
        E_s = (0.5*k*delta_l*delta_l)
        # energy increament
        delta_E = (E_g + E_s) 
        # velocity of ball before hitting the next ball 
        v_hit = (math.sqrt( v_start*v_start + 2*delta_E/(n/n_ball*mass)))  
        t_l.append(delta_l/v_hit*2)
        v_after = (1.00* n/(n+1)*v_hit)
        v_start = v_after
#        print (delta_l)

    return (sum(t_l))

result_i = []
result_t = []
for i in range(50): 
    n = (i+1)*2000
    result_i.append(n)
    result_t.append(time_calculation(n))
    print ("i = %d, time = %.5f"%(n,time_calculation(n)))
