# 4. Modules in the cluster

## Pre-installed software

Several software/module packages are pre-installed on the IBME cluster and are available to users. The GPU module stack available on the IBME cluster is listed below:

| **Name**                                         | **Version** | **Description** |
|:---------------------------------------------------|:-------------| :-------------|
|CUDA |  `10.0.130`,    `10.1.243`,    `11.3.0`,    `11.8.0` | NVIDIA CUDA Toolkit |
|cuDNN |  `6.0.20`,    `7.0.1`,    `7.5.0`| CUDA Deep Neural Network Library |
|NCCL | `1.3.5`,    `2.1.2`,    `2.3.7`,    `2.4.2`| NVIDIA Collective Communications Library. |

The remaining software provides the infrastructure and support services required to maintain the cluster environment. Once logged into headnode1, the `module` command can be used to view and interact with these available software packages. For example:

- The `module avail` or `module spider` command shows the available modules in the system.
- The `module load <module_name-version>` command loads a module. (Note: replace `<module_name-version>` with the specific module and version you want to load.)
- The `module unload <module_name-version>` command unloads a module.
- The `module list` command shows the currently loaded modules.

Once a module is loaded, it is automatically added to the PATH environment variable. This can be verified using the `echo $PATH` command.

!!! terminal "code"
    ```bash
    $ module load cuda/10.0.130
    $ echo $PATH
    /usr/local/cuda-10.0/bin
    ```

## The Mamba or Conda package manager

As the number of pre-installed packages is limited, there may be situations where additional software needs to be installed. One way to install additional software is through the Mamba package manager. Mamba is a faster, open-source alternative to Conda, implemented in C++ to provide improved performance and faster dependency resolution. In most cases, Mamba can be used interchangeably with Conda using identical commands.

Mamba allows different versions of the same software to be installed on the HPC system (or other machines) within isolated virtual environments. Software can be installed locally on the HPC without requiring permission from the IBME HPC administrators.

## Installing Mamba on the IBME cluster

Before you can use Mamba on the IBME cluster, it must be installed (note that Mamba is already pre-installed on the BMRC cluster). Follow the steps below to install it:

- Log in to the IBME cluster - `ssh <userid>@engs-ibmecluster01.eng.ox.ac.uk`.

- In the login node make a shell variable `dir="/users/<userid>/miniforge3"`.


- Download the installer using `wget`. More information about the installer is available on the official GitHub [**repository**](https://github.com/conda-forge/miniforge/) repository.

!!! terminal "code"
    ```bash
    $ wget "https://github.com/conda-forge/miniforge/releases/latest/download/Miniforge3-$(uname)-$(uname -m).sh"
    ```
    Once the installer has been downloaded, it will be saved in the current directory as `Miniforge3-Linux-x86_64.sh`

- Run the installer to install the packages into the `miniforge3` directory.

!!! terminal "code"
    ```bash
    $ bash Miniforge3-$(uname)-$(uname -m).sh -b -p $dir
    ```

- Configure the shell environment for Mamba.

!!! terminal "code"
    ```bash
    $ dir/bin/mamba shell init --shell bash
    ```

- Log out of the IBME cluster and log back in to restart the terminal session.

- Run the following commands to add software repositories (known as channels) to Mamba.

!!! terminal "code"
    ```bash
    $ conda config --add channels nodefaults
    $ conda config --add channels bioconda
    $ conda config --add channels conda-forge
    $ conda config --set channel_priority strict
    ```
- Verify that the repositories have been installed.

!!! terminal "code"
    ```bash
    $ mamba config list channels
    channels:
        - conda-forge
        - bioconda
        - nodefaults
    ```

    nodefaults means do not use the official Anaconda defaults channel
    conda-forge is the largest community-maintained channel
    bioconda is a specialised channel for bioinformatics


## Installing software on the IBME cluster

To install software on the IBME cluster using Mamba, first create and activate a software environment (for example, ImageAnalysis) using the following command:

!!! terminal "code"
    Create environment

    ```bash
    $ mamba create --name ImageAnalysis
    ```
    Activate environment

    ```bash
    $ mamba activate ImageAnalysis
    ```


Once the environment is activated, its name will appear in parentheses at the start of your terminal, for example (ImageAnalysis). Next, identify the software to install from a repository, such as the [conda-forge](https://conda-forge.org/packages/?) channel. In the example below, CUDA toolkit is installed from the conda-forge [repository](https://anaconda.org/channels/conda-forge/packages/cuda/overview) into the active software environment.

!!! terminal "code"
    ```bash
    $ mamba install conda-forge::cuda
    ```

We will not specify a fixed version during installation. As a result, Mamba will install the latest available package that is compatible with the IBME cluster environment. In this case, that was `CUDA 12.6.3`. While this is not the most recent CUDA release available, it is significantly newer than the default CUDA version installed on the IBME cluster.

The command above also installs a number of additional CUDA-related packages that are not available in the versions pre-installed on the IBME cluster. These include key development tools such as the `nvcc` and `gcc` compilers

The mamba environment can be deactivated using command:

!!! terminal "code"
    ```bash
    $ mamba deactivate
    ```


!!! info
    Installing software with Mamba also installs a large number of dependencies. Creating multiple environments can quickly consume storage space in your home directory. We therefore recommend archiving or removing environments that are no longer in use. Your Mamba environments are typically located in `/users/<userid>/miniforge3/envs`.



