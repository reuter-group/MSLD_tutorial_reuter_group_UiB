import math
import sys
import numpy as np

fp1=open("Result.txt","w")
water = sys.argv[2]

nsubs=sys.argv[1]
combs = [(2,2), (1, 1), (1, 3), (1, 4), (1, 5), (1, 6), (1, 7), (1, 8), (1, 9), (3, 9)]

# Make a plot for each ligand
for i in range(len(combs)):
    sub1 = combs[i][0]
    sub2 = combs[i][1]

    prot_data = np.genfromtxt(f'protein/s1s{sub1}.s2s{sub2}_mbar.dat' , dtype=str, skip_footer=1)
    prot_V = np.array(prot_data[9], dtype=float)
    prot_E = np.array(prot_data[11], dtype=float)
  
    water_data = np.genfromtxt(f'{sys.argv[2]}/water/s1s{sub1}.s2s{sub2}_mbar.dat' , dtype=str, skip_footer=1)
    water_V = np.array(water_data[9], dtype=float)
    water_E = np.array(water_data[11], dtype=float)
    
    V = prot_V - water_V
    E  = math.sqrt((prot_E)**2 + (water_E)**2)
    fp1.write("%8.3f +/- %5.3f\n" % (V,E))
#    print("%8.3f +/- %5.3f\n" % (V,E))
#    print("%8.3f +/- %5.3f" % (V,E))

fp1.close()

data = np.genfromtxt('Result.txt', dtype=str)
data_V = np.array(data[:, 0], dtype=float)
data_E = np.array(data[:, 2], dtype=float)

ref_V = np.array(data[1,0], dtype=float)
ref_E = np.array(data[1,2], dtype=float)

for i in range(len(data_V)):
    V = ref_V - data_V[i]
#    print(V)
    E = math.sqrt((data_E[i])**2 + (ref_E)**2)
    print("%8.3f +/- %5.3f" % (V,E))



