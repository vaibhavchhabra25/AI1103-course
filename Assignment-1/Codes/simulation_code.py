import numpy as np
from scipy.stats import bernoulli


dataset_size = 1000000

prob_B = 0.5 
prob_AB = 0.32

B_dataset = bernoulli.rvs(size = dataset_size , p = prob_B)
AB_dataset = bernoulli.rvs(size = dataset_size , p = prob_AB)

for i in range(dataset_size):
  if B_dataset[k] == 0 :
        AB_dataset[k] == 0

num_of_B = 0
num_of_AB = 0

# counting number of B and AB in the datasets
for k in range(dataset_size):
  if B_dataset[k] == 1 :
    num_of_B += 1
  if AB_dataset[k] == 1 :
    num_of_AB += 1


prob_B_calc = num_of_B/dataset_size
prob_AB_calc = num_of_AB/dataset_size

print("Calculated P(B) = ", prob_B_calc , ", Calculated P(AB) = " , prob_AB_calc)

# Since P(A|B)=P(AB)/P(B)...

print("Theoritical value of P(A|B) = ", prob_AB/prob_B)
print("Calculated value of P(A|B) = ", prob_AB_calc/prob_B_calc)
