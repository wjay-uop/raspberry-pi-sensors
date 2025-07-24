# The Linux Command Line #

This is the scary black box that you type text into to interact with your computer.

You can run the command line on Raspbury Pi by opening "Terminal". There's an icon in the top left of the desktop or in the start menu under "Accessories".

You can use the terminal to do anything on your computer. Run software, open files, write documents, get system information etc. In this project we will be using the command line to install and run code.

The instructions in this repository contain commands to copy and paste into the command line. You just need to know how to locate or navigate to where the code we need to run is.


## Copy and Paste ##

You can't use the usual keyboard shortcuts in the command line.

To copy:    `ctrl+shift+C`
To paste:   `ctrl+shift+V`


## Help ##

You can display the manual page for most commands by using the `man` command followed by the name of the command.

This shows you all the possible options and example usage of each command.


## Basic Commands ##

### `pwd` ###

`pwd` is "Print Working Directory". This tells you what directory you are currently in.

When you start the terminal, you will start in your home directory (this is named as your username in the `/home/` directory).

Example:

```bash
pwd
```

Standard output (as user wjay, in the home directory):
```
/home/wjay
```

### `ls` ###

`ls` is "List Directory". This prints out the contents of a directory.

Example:
```bash
ls
```
Standard output in `/home/wjay/`:
```
Bookshelf  data     Documents  file1.txt  file3.txt  Pictures  Public     Videos
code       Desktop  Downloads  file2.txt  Music      Pimoroni  Templates
```

Commands have arguments that can be used. `ls` has many options, `-l` uses a "long listing format" with more information about files, `-t` sorts files by time.

Example:
```bash
ls -l
```
Standard output:
```
drwxr-xr-x 2 wjay wjay 4096 Jul  4  2024 Bookshelf
drwxr-xr-x 6 wjay wjay 4096 Jul 23 13:40 code
drwxr-xr-x 3 wjay wjay 4096 Jul 18 09:54 data
drwxr-xr-x 2 wjay wjay 4096 Jul 16 12:02 Desktop
drwxr-xr-x 2 wjay wjay 4096 Jul 22 15:56 Documents
drwxr-xr-x 2 wjay wjay 4096 Jul 16 12:02 Downloads
-rw-r--r-- 1 wjay wjay    0 Jul 24 13:33 file1.txt
-rw-r--r-- 1 wjay wjay    0 Jul 24 13:33 file2.txt
-rw-r--r-- 1 wjay wjay    0 Jul 24 13:33 file3.txt
drwxr-xr-x 2 wjay wjay 4096 Jul 16 12:02 Music
drwxr-xr-x 2 wjay wjay 4096 Jul 24 09:45 Pictures
drwxr-xr-x 4 wjay wjay 4096 Jul 23 13:41 Pimoroni
drwxr-xr-x 2 wjay wjay 4096 Jul 16 12:02 Public
drwxr-xr-x 2 wjay wjay 4096 Jul 16 12:02 Templates
drwxr-xr-x 2 wjay wjay 4096 Jul 16 12:02 Videos
```

Now the output displays the permissions, owner, group, size and data modified for each item in the directory.

Another argument is that you can specify the directory you want to list. This is by adding the full path, or the path relative to the current directory, after `ls`

Examples:
```bash
ls /home/wjay/
```
```bash
ls /home/wjay/Documents
```


### `cd` ###

`cd` is change directory.

This changes the current working directory to a given path. This can be a full path (i.e `/home/wjay/Documents/`) or 
`./Documents` if you are already in the home directory.

Some important relative path features:
 * `~` represents the home directory. E.g `ls ~/Documents` would like the home Documents directory regardless of your current working directory
 * `./` represents the current directory.
 * `../` represents the parent directory. For example, if the current working directory is `/home/wjay/Documents/`, we can list `/home/wjay/Pictures` with `ls ../Pictures`


## Other Common Commands ##

The above commands should be all you need to know to get things running in this repository. Below are a list of other common commands to be aware of.

* `cp`: Copy file
* `mv`: Move / rename file
* `rm`: Remove file (careful)
* `rmdir`: Remove directory
* `cat`: Displays text in a file
* `nano`: A simple command line text editor

