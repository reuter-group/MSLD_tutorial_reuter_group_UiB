import sys
import numpy as np
import matplotlib.pyplot as plt

# 1 = original FF rtf, 2 = crn rtf
verbose = False
plot = True

#--------------------------------------------
#--------------------------------------------

ff = {}
ff['an'] = []
ff['at'] = []
ff['q'] = []
ff['bond'] = []
for lines in open(sys.argv[1], 'r').readlines():
    line = lines.split()
    try:
        if line[0] == 'ATOM':
            ff['an'].append(line[1])
            ff['at'].append(line[2])
            ff['q'].append(line[-1])
        if line[0] == 'BOND':
            ff['bond'].append(tuple((line[1], line[2])))
    except IndexError:
        None


crn = {}
crn['an'] = []
crn['at'] = []
crn['q'] = []
crn['bond'] = []
junk = {'|', '0',}
for lines in open(sys.argv[2], 'r').readlines():
    line = lines.split()
    try:
        if line[0] == 'ATOM' and line[1] == 'NAME':
            for atom in range(2, len(line)):
                crn['an'].append(line[atom])
        if line[0] == 'ATOM' and line[1] == 'TYPE':
            if line[2] != 'CODES':
                for atom in range(2, len(line)):
                    crn['at'].append(line[atom])
        if line[0] == 'CHARGE':
            for charge in range(1, len(line)):
                crn['q'].append(line[charge])
        if line[1] == 'BONDS:':
            for b in range(3, len(line)):
                if line[b] not in junk and line[b+1] not in junk:
                    #print (line[b], line[b+1]) 
                    crn['bond'].append(tuple((line[b], line[b+1])))
    except IndexError:
        None

ff1 = []
crn1 = []

for i in range(len(ff['an'])):
    #print(ff['an'][i], ff['at'][i], ff['q'][i], crn['an'][i], crn['at'][i], crn['q'][i],)
    ff_name = ff['an'][i]
    ff_at   = ff['at'][i]
    ff_q    = ff['q'][i]
    dq = []
    index = []
    index_names = []
    for p in range(len(crn['at'])):
        if crn['at'][p] == ff_at:
            #j = crn['at'].index(crn['at'][p])
            #index.append(j)
            index.append(p)
            dq.append(abs(abs(float(ff_q)) - abs(float(crn['q'][p]))))
            index_names.append(crn['an'][p])
    if verbose == True:
        print(dq)
        print(index_names)
    
    k = index[dq.index(min(dq))]
    if abs( float(ff_q) - float(crn['q'][k]) ) > 0.05:
        print(f"check these atom names: {ff_name}, {crn['an'][k]}")

    #print(ff_name, ff_q, crn['an'][k], crn['q'][k])

    ff1.append(float(ff_q))
    crn1.append(float(crn['q'][k]))

if plot == True:
    ff_crn = np.column_stack((ff1, crn1))
    rmsd = np.sqrt(np.mean((np.array(crn1) - np.array(ff1)) ** 2))
    plt.scatter(ff1,crn1,marker='o',linewidth=0.5, label=f'QRMSD={rmsd:.4f}')
    plt.axline((0, 0), slope=1)
    plt.xlabel('FF charges')
    plt.ylabel('CRN charges')
    plt.legend()
    plt.show()

quit()

#============================================================================
#============================================================================
#            j = crn['at'].index(atype)
#            if abs(abs(float(ff_q)) - abs(float(crn['q'][j]))) < 0.01:
#                print(ff_name, ff_q, crn['an'][j], crn['q'][j])
#                break

#    least = []
#    if ff_at in crn['at']:
#        j = crn['at'].index(ff_at)
#        diff = abs(abs(float(ff_q)) - abs(float(crn['q'][j])))
#        if least = '':
#            least.append(diff)
        
#        if abs(abs(float(ff_q)) - abs(float(crn['q'][j]))) < 0.005:
#            print(ff_name, ff_q, crn['an'][j], crn['q'][j])
#            out['pair'].append(tuple((ff_name, crn['an'][j])))

