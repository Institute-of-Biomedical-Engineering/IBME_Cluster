# 5. Runing jobs in the IBME cluster


## Batch Sessions 

In batch computing environments, jobs are submitted to compute nodes through the SLURM scheduler. SLURM ensures that the resources (GPU, CPU and Memory) are efficiently utilised across the cluster. It evaluates each job based on factors including requested runtime, required resources, and current cluster availability, then assigns priorities to determine job scheduling order.

## Submitting jobs using SLURM

To submit the job to the compute node with the SLURM scheduler the code to be run should be included in a shell script `(.sh)`. We have created a example shell script to work through the process and requirements of submitting the job to the compute note. Once connected to the IBME cluster, from the login node:

- Create and activate a Mamba environment (you can also create python virtual environment). This is to ensure we are in an isolated environment and the pckages we install do not interfare with other work in the cluster. 

- make a directory, 'cd' into the directory. Output of the jobs submitted through SLURM are saved in the directory where the jobs is submitted from. Therefore, it is recommended to create a directory per project and sun directories to store the job output. 

- download a shell and python script file using command

!!! terminal "code"
    ```bash
    $ mamba create --name ImageAnalysis
    $ mamba activate ImageAnalysis
    $ mamba install -c conda-forge matplotlib; mamba install -c conda-forge numpy
    $ mkdir Example_job
    $ cd Example_job
    $ wget https://raw.githubusercontent.com/Institute-of-Biomedical-Engineering/IBME_Cluster/master/Example_script.sh
    $ wget https://raw.githubusercontent.com/Institute-of-Biomedical-Engineering/IBME_Cluster/master/Example_python.py
    ```

The `Example_script.sh` contains the following code:

!!! terminal "code"
    #!/bin/bash
 
    echo "This job is running on:"
    hostname

    python3 Example_python.py

The shell scrtpt can be thought of as an manual for the compute node. The compute node reads the shell script runs the command line by line sequencially.The first line of the script `#!/bin/bash` instruct the system to run the script as a `bash` shell. The secound line of the script prints a message and the third line prints the hostname. The final line of the script runs the Python script `Example_python.py`. The Python script generates some random numbers, generate the plot and saves it as a `plot.png` file. 

The python script requires some packages to successfully run, they are `matplotlib` and `numpy`. Intall them using command: 

!!! terminal "code"
    ```bash
    $ mamba install -c conda-forge matplotlib; 
    $ mamba install -c conda-forge numpy
    ```
 
 Finally the job can be subbmitted using command: 

!!! terminal "code"
    ```bash
    $ sbatch ./Example_script.sh
    ```