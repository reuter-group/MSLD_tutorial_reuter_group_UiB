import sys
import numpy as np
import math
import matplotlib.pyplot as plt
from itertools import combinations

nsubs = 10
print('Q-RMSD cutoff (JCIM article): 0.001 e-')
print(u'log\u2081\u2080''(Q-RMSD) cutoff > -3.0')
print('==========================================')

combs = [(2,2), (1, 1), (1, 3), (1, 4), (1, 5), (1, 6), (1, 7), (1, 8), (1, 9), (3, 9)]

for i in range(len(combs)):
    sub1 = combs[i][0] 
    sub2 = combs[i][1]
    ff_str = np.genfromtxt(f's1s{sub1}.s2s{sub2}_crn2ff_qpert.str' , dtype=str, skip_header=3, skip_footer=2)
    ff = np.array(ff_str[:, 3], dtype=float)
    crn_str = np.genfromtxt(f's1s{sub1}.s2s{sub2}_ff2crn_qpert.str', dtype=str, skip_header=3, skip_footer=2)
    crn =  np.array(crn_str[:, 3], dtype=float)
    # Paste the two columns side by side
    ff_crn = np.column_stack((ff, crn))
  
    # Calculate the RMSD
    rmsd = np.sqrt(np.mean((crn - ff) ** 2))
    log10 = math.log10(rmsd)

    # Calculate the deviation from ff based on rmsd cutoff (0.001 e-)
    N = np.shape(ff)[0]
    #print(N)
    deviation = float(0.001) * np.sqrt(N) + ff
    #print(deviation)
   
    # Calculate the average of each row
    #mean = np.mean(ff_crn, axis=1)
    #print(mean)
    
    # Calculate the geometric mean of each row
    #geometric_means = np.sqrt(np.prod(ff_crn, axis=1))
   
    # Calculate the standard deviation
    sd = np.std(ff_crn, axis=1)
  
    # Combine row averages and row geometric means side by side
    np.set_printoptions(suppress=True)
    print(f'site1sub{sub1}-site2sub{sub2}')
    #result = np.column_stack((ff, crn, mean, sd, deviation))
    #print("     ff        crn         mean           sd         cutoff_deviation")
    #result = np.column_stack((ff, crn, sd))
    #print("     ff        crn   standard_deviation")
    #print(result)
    
    #print('site1sub' + str(sub))
    print("Q rmsd:", "%.4f" % rmsd)
    print(u'log\u2081\u2080'"(Q rmsd (ff-crn)):", "%.4f" % log10)
    #print(u'log\u2081\u2080'"(Q rmsd (ff-mean)):", "%.4f" % math.log10(np.sqrt(np.mean(mean - ff) ** 2)))
    #print(u'log\u2081\u2080'"(Q rmsd (crn-mean)):", "%.4f" % math.log10(np.sqrt(np.mean(mean - crn) ** 2)))
 
print('===============================')  
quit()

#-------------------------------------

#ff = np.genfromtxt(sys.argv[1]) #, skip_header=3, skip_footer=2, dtype=str, usecols=3)
#crn = np.genfromtxt(sys.argv[2]) #, skip_header=3, skip_footer=2, dtype=str, usecols=3)

#print(ff)
#quit()

# Calculate the RMSD
#rmsd = np.sqrt(np.mean((crn - ff) ** 2))

# Calculate the standard deviation
#std_dev = np.std(crn - ff)

#print("Q rmsd:", "%.4f" % rmsd)
#print("Q Standard Deviation:", std_dev)

#print(ff, crn)
quit()

# Create figure and 3 subplots
fig, ax = plt.subplots()

nsubs = 10

for mols in range(nsubs):
    sub = mols + 1
    ff = np.genfromtxt('ff_' + str(sub) + '.dat')
    crn = np.genfromtxt('crn_' + str(sub) + '.dat')
    # Calculate the RMSD
    rmsd = np.sqrt(np.mean((crn - ff) ** 2))
    print("Q rmsd:", "%.4f" % rmsd)    
    ax.plot(rmsd, label='sub' + str(sub))
    ax.legend(frameon=False)

# Set overall title and tight layout
fig.suptitle("Q rmsd")
fig.tight_layout()

# Show the plot
plt.show()

quit()



