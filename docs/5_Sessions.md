# 5. Runing jobs in the IBME cluster


## Batch Sessions 

In batch computing environments, jobs are submitted to compute nodes through the SLURM scheduler. SLURM ensures that the resources (GPU, CPU and Memory) are efficiently utilised across the cluster. It evaluates each job based on factors including requested runtime, required resources, and current cluster availability, then assigns priorities to determine job scheduling order.

## Submitting jobs using SLURM

To submit the job to the compute node with the SLURM scheduler the code to be run should be included in a shell script `(.sh)`. We have created a example shell script to work through the process and requirements of submitting the job to the compute note. Once connected to the IBME cluster, from the login node:

-   Create and activate a Mamba environment (you can also create python virtual environment). This is to ensure we are in an isolated environment and the pckages we install do not interfare with our other work in the cluster. 

    !!! terminal "code"
        ```bash
        $ mamba create --name ImageAnalysis
        $ mamba activate ImageAnalysis
        $ mamba install -c conda-forge matplotlib; mamba install -c conda-forge numpy
        ```

-   make a directory, `cd` into the directory. Output of the jobs submitted through SLURM are saved in the directory where the jobs is submitted from. Therefore, it is recommended to create a directory per project and sub-directories to store the job output everytime a job is submitted. 

    !!! terminal "code"
        ```bash
        $ mkdir Example_job
        $ cd Example_job
        ```

-   download a shell and python script file using command

    !!! terminal "code"
        ```bash
        $ wget https://raw.githubusercontent.com/Institute-of-Biomedical-Engineering/IBME_Cluster/master/Example_script.sh
        $ wget https://raw.githubusercontent.com/Institute-of-Biomedical-Engineering/IBME_Cluster/master/Example_python.py
        ```

    The `Example_script.sh` contains the following code:

    !!! terminal "code"
        ```bash
        ##!/bin/bash
    
        echo "This job is running on:"
        hostname

        python3 Example_python.py
        ```

    The shell scrtpt can be thought of as a manual for the compute node. The compute node reads the shell script runs the command line by line sequencially.The first line of the script `#!/bin/bash` instruct the system to run the script as a `bash` shell. The secound line of the script prints a message and the third line prints the hostname. The final line of the script runs the Python script `Example_python.py`. The Python script generates some random numbers, generate the plot and saves it as a `plot.png` file. 

-   The python script requires some packages to successfully run, they are `matplotlib` and `numpy`. Intall them using command: 

    !!! terminal "code"
        ```bash
        $ mamba install -c conda-forge matplotlib; 
        $ mamba install -c conda-forge numpy
        ```
 
-   One the steps above have been followed, the job can be subbmitted using command: 

    !!! terminal "code"
        ```bash
        $ sbatch ./Example_script.sh
        ```

## The job Output

The job output is not printed in the terminal, instead it is saved in a file called `slurm-JOBID.out` in a directory where we submitted the job from. The `JOBID` in the file name is an unique ID assigned by SLURM to every job. The ouput of the can be investigated using command `less` or `cat`. In the example below, we have used the `less` commnd which opens the page in a interactive mode on the screen. If you have followed the example above you should see:

!!! terminal "code"
    ```bash
    $ less slurm-JOBID.out 
    ```

    ```bash
    This job is running on:
    node04
    ```
    it can be node05 depending on the availability of the node. 

The job also outputs a plot called `plot.png` file, this is also stored in the directory where the job is submitted from. The HPC systems are remote machines which don't have a graphical user interface. It is recomemded to transfer this file to the local computer using FileZZile or rsync command, see [chapter 2](http://127.0.0.1:8000/IBME_Cluster2_Transferring_files_to_remote_machine/) for more details.

## The job Option configaration

SLURM jobs can be configured to run with several specific options. These options can be specified at the top of the shell script with `#SBATCH` keyword followed by the option name and its value. The option names can either be as a short or long format. The table below highlights some of the common options:

| **Short**                                         | **Long** | **Description** |
|:---------------------------------------------------|:-------------| :-------------|
|-D |  --chdir | Working directory |
|-o |  --output| Output file |
|-A | --account| Billing account |
|-p | --partition| partition |
|-c | --cpus-per-task| CPUs per task |
|-t | --time| Runtime limit |
|-J | --job-name`| Job name |


