from scipy.stats import bernoulli as ber

import matplotlib.pyplot as plot

theor_prob = 0.042      # theoritical probability

dataset_size = 50000    # total number of trials
num_of_tosses = 20

right_toss_set = 0      # count of toss set with required condition

prob_H = 0.5

for i in range(dataset_size):

    head_count=0        # count of heads in first 10 tosses
    tail_count=0        # count of tails in next 10 tosses

    toss = ber.rvs(size = num_of_tosses , p = prob_H)       # tossing coin 20 times
    # In the toss set, 1 represents 'head' and 0 represents 'tail'

    for k in range(int(num_of_tosses/2)):       # loop for first 10 tosses
        if toss[k] == 1:
            head_count+=1

    for k in range(int(num_of_tosses/2) , num_of_tosses):       # loop for next 10 tosses
        if toss[k] == 0:
            tail_count+=1
    
    if head_count == 4 and tail_count == 4:
        right_toss_set+=1

sim_prob = right_toss_set/dataset_size      # simulated probability

print("Simulated probability :", sim_prob)
print("Theoritical probability :", theor_prob)

plot.bar(0.00, theor_prob, color = 'red', width = 0.2, label = 'Theoretical')
plot.bar(1, sim_prob, color = 'blue', width = 0.2, label = 'Simulated')
plot.xlabel('Cases')
plot.ylabel('Probabilities')

plot.legend()
plot.show()
