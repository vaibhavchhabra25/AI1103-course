import numpy as np
import random

dataset_size = 1000000

F_x = 0    #CDF for U
G_x = 0    #CDF for 2V

x = random.uniform(-10e15,10e15)    #Assigning a random value to x from -10^15 to 10^15 which is a very big range

for k in range(dataset_size):

  X = random.uniform(-10e15,10e15)  #Assigning a random value to X from -10^15 to 10^15 which is a very big range

  if(X <= x):
    F_x += 1
  if(X <= x/2):
    G_x += 1
  
F_x /= dataset_size     #Value of CDF of U at a particular x
G_x /= dataset_size     #Value of CDF of 2V at a particular x

print("Value of x =", x )
print("Value of F(x)-G(x) =", F_x - G_x)
print("Value of (F(x)-G(x))x =", (F_x - G_x) * x)

print("\nSo, value of (F(x)-G(x))x is positive.")
