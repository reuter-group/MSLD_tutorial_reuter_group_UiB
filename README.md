# Multisite &lambda; Dynamics
1. **Hardware requirements**  
   Linux system with NVIDIA GPU
   !! **no** root or superuser privileges required !!  
   
3. **Software requirements**  
   CHARMM program (download here: https://charmm.chemistry.harvard.edu/request_license.php?version=free)  
   miniconda (https://docs.anaconda.com/free/miniconda/miniconda-install/)  
   PyMOL
    
 ## Compiling CHARMM ##
   1. Install Conda and create a new environment  
   ```conda create --name charmm```  
   ```conda activate charmm```  
   ```conda install conda-forge::mamba```  
   ```nvidia-smi ```  
   ```mamba install -y -c "nvidia/label/cuda-x.y.y" cuda```  
   ```mamba install -y -c conda-forge make cmake binutils fftw openmpi openmm sysroot_linux-64==2.17 readline==8.2 rdkit openbabel pymol-open-source```  
   ```mamba install -y -c conda-forge gcc==X.X gxx==X.X gfortran==X.X ```    
   3. **Compile CHARMM**
