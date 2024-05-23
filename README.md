# Multisite &lambda; Dynamics
1. **Hardware requirements**  
   Linux system with NVIDIA GPU  
   **!! root or superuser privileges are NOT required !!**  
   
2. **Software requirements**  
   [CHARMM program](https://charmm.chemistry.harvard.edu/request_license.php?version=free)  
   [miniconda](https://docs.anaconda.com/free/miniconda/miniconda-install/)  
   PyMOL

3. **References literature**
   - [&lambda;D original paper](https://doi.org/10.1063/1.472109)
   - [MS&lambda;D paper](https://doi.org/10.1021/ct200444f)
   - [Adaptive Landscape Flattening (ALF)](https://doi.org/10.1021/acs.jpcb.6b09656)
   - [Protein Mutations - I](https://doi.org/10.1002/pro.3500)
   - [Protein Mutations - II](https://doi.org/10.1002/jcc.26525)
   - [Biasing potential replica exchange (BPREX)](https://doi.org/10.1021/ct500894k)
   - [msld_py_prep and charge corrections](https://doi.org/10.1021/acs.jcim.2c00047)
   - [MS&lambda;D benchmark paper](https://doi.org/10.1021/acs.jctc.0c00830)
   - [AMBER & OPLS in MS&lambda;D](https://doi.org/10.1021/acs.jcim.3c01949)

4. **Github Resources - Charlie's group**
   - [ALF](https://github.com/RyanLeeHayes/ALF)
   - [pyCHARMM workshop](https://github.com/BrooksResearchGroup-UM/pyCHARMM-Workshop/tree/main)
   - [MS&lambda;D workshop](https://github.com/BrooksResearchGroup-UM/MSLD-Workshop)

   
 ## Compiling CHARMM ##
** You can follow the steps from the [pyCHARMM](https://github.com/BrooksResearchGroup-UM/pyCHARMM-Workshop/tree/main/0Install_Tools/Linux) workshop as well, below is just a part of the things that are on the pyCHARMM workshop page
**

   1. Install Conda and create a new environment  
   ```conda create --name charmm```  
   ```conda activate charmm```  
   - install mamba within the conda environment to make the next steps fast   
   ```conda install conda-forge::mamba```
   - check the version of NVIDIA drivers  
   ```nvidia-smi ```
   - install cuda version that is compatible with your NVIDIA drivers  
   ```mamba install -y -c "nvidia/label/cuda-x.y.y" cuda```  
   ```mamba install -y -c conda-forge make cmake binutils fftw openmpi openmm sysroot_linux-64==2.17 readline==8.2 rdkit openbabel pymol-open-source```  
   ```mamba install -y -c conda-forge gcc==X.X gxx==X.X gfortran==X.X ```    
   3. **Compile CHARMM**
