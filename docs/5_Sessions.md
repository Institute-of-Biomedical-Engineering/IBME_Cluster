# 3. Creating, viewing and editing files


## Creating files

In an HPC system, configuration files often need to be created in the form of text-based files such as YAML. There are several ways to create files from the command line. One common method is the `touch` command, which creates a file if it does not already exist. Although `touch` is typically used to update a file’s timestamp without modifying its contents, it will create a new file when used with a filename that does not exist.

!!! terminal "code"
    ```bash
    $ touch FileExp.fastq
    ```
    use command `ls` to confirm that the `FileExp.fastq` exists
    ```bash
    $ ls
    FileExp.fastq
    ```
## Editing files

Terminal-based text editors like `vim` and `nano` are mainly used to edit files but can also create them if they do not exist. They not only create files but also open them in editor mode. These text editors come preinstalled with many Linux distributions. To start a text editor like `vim`, you can use the `vim` command followed by the filename.

!!! terminal "code"
    ```bash
    $ vim FileExpT1.fastq
    ```

The `vim` command opens a file (or creates and opens it) in *command mode*. Command mode is useful for text manipulation tasks such as cutting and pasting, but it does not allow text to be typed. Typing text can be done by switching from *command mode* to *insert mode* by pressing the **i** key. Once the text has been entered in *insert mode*, you must exit it and return to *command mode*. This is done by pressing the **Esc** key. Once in *command mode*, there are several options:


- `:w` — saves the file and remains in the command mode
- `:wq` — saves the file and exit to the terminal
- `:q!` — doesn't save the file and exit to the terminal

The *visual mode* is another way to manipulate text. This mode can be entered from the *command mode* by pressing:

- `v` — character manupulation
- `V` — line manupulation


## Viewing files

The quickest way to view a file is by using `less` command. 

!!! terminal "code"
    ```bash
    $ less FileExpT1.fastq
    ```

It lets the user view the file in an interactive format by allowing scrolling, searching, and navigation. Some useful keys for the `less` command are:

- `j / k` — for scrolling up/down
- `space` — next page
- `b` — previous page
- `/[search key work]` — search word
- `q` — quite page

If the file to be viewed is small in size, the command `cat` can be used. This command doesn't start an interactive session. It just prints the content of the file in the terminal.

!!! terminal "code"
    ```bash
    $ cat FileExpT1.fastq
    ```