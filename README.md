# Log Analysis
A reporting tool that explores the basic concepts of python, relational databasees, joins, queries and sub-queries.

## The Database
The database is a fictional PostgreSQL news website database. It contains tables such as Articles, Authors and Log. The articles table contains information such as author, title, slug, lead, time, etc. The Authors table conatins informationm such as name, bio and id while the Log table contains information such as the web server log for the site. The log has a databse row for each time a reader loaded a webpage.

## The Reporting Tool
The script is wriiten in python, connects to the database and uses SQL queries to analyze the log data. it runs from the command line and the output of the queires are printed out in plain text, formatted using string interpolation. It uses information from the database to answer the following questions:
1. What are the most popular 3 articles of all time?
2. Who are the most popular articles author of all time?
3. On what days did more than 1% of requests lead to errors?

This tool provides a way to draw conclusions from data. In this project, the reporting tool and the web server connect to the same databse allowing information to flow from the web server into the report.

## Getting Started
Running this reporting script involves having the following tools installed on your computer:
- python
- virtualBox
- Vagrant
- Virtual Machine(VM).
The Vagrant and VirtualBox are used to install and manage the VM. You also need a terminal. You can use the regular terminal if you are on Mac or Linux. For Windows, you can use Git Bash. it can be downloaded [here](https://git-scm.com/downloads)

### Python Installation
If you are on Linux, you probably already have python installed with your distro. However, to download and install python, follow the instruction [here](https://realpython.com/installing-python/)

### Install VirtualBox
Download VirtualBox from [here](https://www.virtualbox.org/wiki/Download_Old_Builds_5_1). Install the platform package for your operating system. You do not need to open VirtualBox after installation. Vagrant will do that.

### Install Vagrant
Download Vagrant from [here](https://www.vagrantup.com/). Vagrant configures the VM and lets you share files between your host computer and the VM'S filesystem. Install the version for your operating system. After successful installation, run `vagrant --version` in your terminal to see the version number.

### Download the VM Configuration
1. You can download and unzip this file: [FSND-Virtual-Machine.zip](https://s3.amazonaws.com/video.udacity-data.com/topher/2018/April/5acfbfa3_fsnd-virtual-machine/fsnd-virtual-machine.zip) This will give you a directory called FSND-Virtual-Machine.
2. Alternately, you can use Github to fork and clone the repository https://github.com/udacity/fullstack-nanodegree-vm.

Either way, you will end up with a new directory containing the VM files. From your terminal, change to this directory with `cd`. Using `ls` list the content of this directory and you will find another directory called vagrant. Change directory to the vagrant directory.

### Start the Virtual Machine
- While you are inside the vagrant subdirectory, run the command `vagrant up`. Vagrant will download the Linux operating system and install it.
- Once `vagrant up` is done with installation, run `vagrant ssh` to log into the Linux VM

## Preparing the Data
- Download the data [here](https://d17h27t6h515a5.cloudfront.net/topher/2016/August/57b5f748_newsdata/newsdata.zip)
- Unzip this file after downloading it. The file inside is called newsdata.sql
- Change directory to `\vagrant` and put the newsdata.sql file into the directory. This directory is shared with your virtual machine.
- Load the site's data into your local database using `psql -d news -f newsdata.sql`. Here's what the command does:
  - `psql` - the PostgreSQL command line
  - `-d news` - connect to the databse named news
  - `-f newsdata.sql` - runs the SQL statements in the file newsdata.sql

## Running the Reporting Tool
The reporting tool is the `news.py` file. Download this file in the same directory as the database data and from your terminal run `./news.py`. You should get an output that looks like this: 
```
The most popular 3 articles of all time are:
*Candidate is jerk, alleges rival - 338647 views
*Bears love berries, alleges bear - 253801 views
*Bad things gone, say good people - 170098 views

The most popular article authors of all time are:
*Ursula La Multa - 507594 views
*Rudolf von Treppenwitz - 423457 views
*Anonymous Contributor - 170098 views
*Markoff Chaney - 84557 views

The day(s) more than 1 percent of requests led to errors is/are:
*July      17, 2016 - 2.26 percent
```

