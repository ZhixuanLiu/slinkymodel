# slinkymodel
to solve two problems: 1). the length deformation of a hanging slinky under gravity 2). time needed for slinky to restore to normal when a hanging slinky free falls 

first assumptions: 
a slinky can be considered as a brunch of balls connected by ideal springs(no mass) in series like: 

(ball) -- (spring) -- (ball) -- (spring) -- (ball) -........- (spring) --(ball) -- (spring) --(ball)  -----> ( gravity direction)

assume that 
there are n+1 balls and n springs in series under gravity
original hook factor of slinky is k 
mass of slinky is m 

The springs in the model are in series connected. according to equation: 
1/k_all = 1/k1 + 1/k2 + 1/k3 ...... 
in the (ball-spring) model, the equivalent hooks factors of springs is ke: 
1/k (slinky) = 1/k(spring) + 1/k(spring) + ...... (number of springs : n) 
k(spring) = n * k(slinky) 

deformation: 
top 1st spring: 
Tension = n/(n+1)*m*g , Tension = k(spring) * DeltaL1 , DeltaL1 = m*g/k*(1/(n+1)) 
top 2nd spring: 
Tension = (n-1)/(n+1)*m*g , Tension = k(spring) * DeltaL1 , DeltaL2 = m*g/k*(1/(n+1)) * (n-1)/n 
top 3rd spring: 
Tension = (n-2)/(n+1)*m*g , Tension = k(spring) * DeltaL1 , DeltaL3 = m*g/k*(1/(n+1)) * (n-2)/n
...
top i th spring: 
Tension = (n-(i-1))/(n+1)*m*g , Tension = k(spring) * DeltaL1 , DeltaLi = m*g/k*(1/(n+1)) * (n-(i-1))/n 

Sumoflength = DeltaL1 + DeltaL2 ....  = 1/2 * m*g/k


