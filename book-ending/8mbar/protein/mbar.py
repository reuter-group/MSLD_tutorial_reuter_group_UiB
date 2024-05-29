import sys
import numpy as np
import pymbar
from pymbar import *
import seaborn as sns

temp = 298.15
beta = 1/(0.001987204259*temp)

ligPath = sys.argv[1]
throttle = 0

# Load energies
## Forward direction
ffE1 = np.loadtxt(f'{ligPath}crn2ffprot/ff.ener',dtype=float, skiprows=1, usecols=1)
crnE1 = np.loadtxt(f'{ligPath}/crn2ffprot/renormal.ener',dtype=float, skiprows=1, usecols=1)

## Backward direction
crnE2 = np.loadtxt(f'{ligPath}/prot/renormal.ener',dtype=float, skiprows=1, usecols=1)
ffE2 = np.loadtxt(f'{ligPath}/prot/ff.ener',dtype=float, skiprows=1, usecols=1)

# Assemble MBAR matrix
ffE = np.concatenate((ffE1, ffE2))
crnE = np.concatenate((crnE1, crnE2))

u_kn = np.stack((ffE,crnE),axis=0)*beta
N_k = np.array([len(ffE1),len(crnE2)])

# Instantiate MBAR object
mbar = MBAR(u_kn,N_k)

result = mbar.compute_free_energy_differences()

# Get free energy/uncertainty in kcal/mol
fe = result['Delta_f'][0,1]/beta
unc = result['dDelta_f'][0,1]/beta
#print(fe, unc)

# Get overlap
overlap = mbar.compute_overlap()
#print(overlap)
overlap = overlap['matrix'][0,0]


print(f'free energy of perturbing from our force field to renormalized charges for ligand is: {fe:.3f} +/- {unc:.3f}')
print(f'Overlap between forward and reverse distributions is: {overlap*100:.2f}%')

quit()
