import numpy as np
import matplotlib.pyplot as plt
from math import factorial as fact

'''
For Multisite site system.
'''
__author__ = "Dandan Xue, Parveen Gartan"
__Date__ = "June 23, 2021 (updated: 13 July 2021)"

x = np.arange(0, 1, 0.0025)

nsubs = np.genfromtxt('../nsubs', dtype=None, delimiter=' ')
#print(nsubs)

nsites = len(nsubs)
nblocks = sum(nsubs)
extra = [0] # this will help in going to the next site after excluding 2D profiles (for 1st site = 0)
current_sum = 0 # 2D profiles that need to be excluded (for site=1 ==> 0)

for isite in range(nsites):
    subs = nsubs[isite]
    start = extra[isite] + 1 # read single pmf files
    stop1 = start + subs     # start of transition files
    fig, ax1 = plt.subplots(1, 1)#, figsize=(15,15))
    for i in range(start, stop1): # for site=i generate PMF vs LAMBDA plots
        filename = f'multisite/G{i}.dat'
        with open(filename) as f:
            v = [float(l.strip())  for l in f.readlines()]
            #print(f)   
            #ax1[start-start, start-start].plot(x, v)
            ax1 = plt.plot(x,v, label='sub' + str(i-start+1))
    plt.title('site'+str(isite+1))        
    plt.xlabel('$\lambda$')
    plt.ylabel('PMF')
    plt.legend()
    #    print(i)
    
    fig, ax2 = plt.subplots(subs, subs, figsize=(8,8))
    m = 0 # To skip transition combinations for substituents  
    for j in range(subs):
        comb = subs - j - 1 # transition combination for sub j
        start2 = stop1 + m
        stop2 = start2 + comb
        m += subs-j-1 # calculate transitions to skip for sub (j+1)
        for k in range(start2, stop2): # for site=i,sub=j generate pairwise transitions
            l = k - start2
            filename = f'multisite/G{k}.dat'
            print(filename)
            with open(filename) as f:
                v = [float(l.strip())  for l in f.readlines()]
                #print(f) # check if reading the correct files or not
                #python first fills 1st row then 2nd row then 3rd row and so on....
                ax2[j, j+l+1].plot(x, v)
                ax2[j, j+l+1].set_title((f'Sub{j+1}-{j+l+2}'))
                
        fig.suptitle('site'+str(isite+1))
    
    for p in range(subs):
        for q in range(p+1):
            ax2[p,q].set_visible(False)

    #print(j)
    #break
    '''
    # the if statements helps in skipping 2D profiles and going over to the next site.
    # add print statements to check which files are being read.
    # To understand which combinations are 2D, read the log file from WHAM analysis.
    # Create all combinations for all sites and assign them the file numbers to help with the necessary 
    # files.
    '''
    if nsubs[isite] > 2:
        next_sum = current_sum + nsubs[isite]
        summation = sum(range(current_sum+1, next_sum+1))
        ex = extra[isite] + subs + int(fact(subs)/(fact(2)*fact(subs-2))) + (subs*nblocks)-summation
        extra.append(ex)
        current_sum += next_sum
    else:
      next_sum = current_sum + nsubs[isite]
      summation = sum(range(current_sum+1, next_sum+1))
      ex = extra[isite] + subs + int(fact(subs)/(fact(2)*fact(subs-2))) + (subs*nblocks)- summation - 1
      extra.append(ex)
      current_sum += next_sum


plt.legend()
plt.show()
#plt.savefig('pmfvL.png', dpi='figure')

