import sys
import math
import matplotlib.pyplot as plt

def calculate_reliability(seq_sys,prob) :
    res = 1
    for n in seq_sys :
        res *= (1 - math.pow(1-prob,n))
    return res

if len(sys.argv) != 5 :
    sys.exit(0)
    
args = sys.argv[1:]
print args
num,prob,cost,total = map(float,args)
num,cost,total = int(num),int(cost),int(total)

seq_sys = [1]*num
reliability_data = [calculate_reliability(seq_sys,prob)]
cur_cost, cur_ind = cost,0
while cur_cost <= total :
    seq_sys[cur_ind] += 1
    cur_ind = (cur_ind + 1) % num
    cur_cost += cost
    reliability_data.append(calculate_reliability(seq_sys,prob))

plt.plot(list(range(len(reliability_data))),reliability_data,'ro-')

plt.xlabel('number of additional elements')
plt.ylabel('reliability')
plt.title('Reliability Plot')
plt.show()
