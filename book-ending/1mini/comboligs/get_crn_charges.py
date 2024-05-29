import sys
import os

rtf = sys.argv[1]
print(rtf.split("."))

if len(rtf.split(".")) < 3:
    sub1 = rtf.split(".")[0][-1]
else:
    sub1 = rtf.split(".")[0][-1]
    sub2 = rtf.split(".")[1][3:]

print(sub1, sub2)
core = 'LIG' 

names = []
charges = []
with open(rtf, 'r') as f:
    for lines in f.readlines():
        line = lines.split()
        try:
            #print(line)
            if line[0] == 'ATOM' and line[1] == 'NAME':
               for i in range(2, len(line)):
                    names.append(line[i])
            if line[0] == 'CHARGE':
                for j in range(1, len(line)):
                    charges.append(line[j])
        except IndexError:
            None

try:
   os.remove(f's1s{sub1}.s2s{sub2}_ff2crn_qpert.str')
except FileNotFoundError:
    print('File does not exists.')


new_str = open(f's1s{sub1}.s2s{sub2}_ff2crn_qpert.str', 'a')

new_str.write(f'* Change atom charges to crn charges for ligand s1s{sub1}.s2s{sub2} \n')
new_str.write(f'* \n')
new_str.write(f'\n')
for p in range(len(names)):
    new_str.write(f'scalar charge set {charges[p]} sele atom LIG 1 {names[p]} end \n')   

new_str.write(f' \n')
new_str.write('RETURN')

quit()
###############

