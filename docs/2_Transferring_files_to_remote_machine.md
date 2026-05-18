# 5. Transferring files to and from remote machine

## Archiving file

The quickest way to transfer a large number of files is to archive the files into one file before transferring it over the network. This reduces the overhads of transferring individual files. In Linux *Tape Archive* knows as `tar` is used as combine multiple files and folder into a single file. The `tar` is often combined with compression tool such as `gzip`, which has `.gz` file extension. For example, to compress a directory *data* which have multiple subdirectories and files within the subdirectories in to a single file (compressed_data.tar.gz), the following command can be used:

!!! terminal "code"
    ```bash
    $ tar -cvzf compressed_data.tar.gz data
    ```

Compare the reduction in size with the `du` command.

!!! terminal "code"
    ```bash
    $ du -sh data
    146M    data
    ```
    The output shows the data directory have a size of 146M

    ```bash
    $ du -sh compressed_data.tar.gz
    48M    data
    ```
    The compressed file have a size of 48M

## Transferring files

The `rsync` command can be used to transfer files and directory to remote servers. For instance, to transfer the file *compressed_data.tar.gz* to a `user` home directory of a remote machine `linux-machine`, the following command can be used:

!!! terminal "code"
    ```bash
    $ rsync -avP compressed_data.tar.gz user@linux-machine:~/
    ```
    Similar command can also be used to transfer a directory to a remore machine
  
## Transferring files with FileZilla

FileZilla is a file transfer software that is free of charge. It can be used to upload and download data from remote server. To use the software the filezilla client can be downloaded from https://filezilla-project.org and installed on local computer. Once installed the filezilla software can be available form the windows search pane and can be launched. The image below shows the graphical user interface of the sofware.

FileZilla is free file transfer software. It can be used to upload and download data from a remote server. To use the software, the FileZilla Client can be downloaded from <https://filezilla-project.org> and installed on a local computer. Once installed, FileZilla is available from the Windows Search pane and can be launched. The image below shows the graphical user interface of the software.

<p align="center">
    <img src="../images/filezila.png" width="720">
</p>

The software has two file browser windows: one for the local computer on the left and one for the remote server on the right. Initially, the remote server file browser remains empty until a connection to the server is established.

To connect to the remote machine, in this case the IBME cluster. The follwing information should be provided:

- Host: sftp://engs-ibmecluster01.eng.ox.ac.uk
- Username: User name in the host machine
- Password: User passowrd in the host machine
- Post: This can be left black

After entering the connection details, click **Quickconnect**. If the connection is successful, the remote server file browser will appear on the right Navigate to the required location by selecting folders in the file browser or by entering the directory path in the address bar. For the remote server entering the directory path directly is often more convenient.Files can then be transferred by dragging and dropping them between the left and right panels.
