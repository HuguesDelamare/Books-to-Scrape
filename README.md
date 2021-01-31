## Table of contents
* [General info](#general-info)
* [Technologies](#technologies)
* [Installation](#installation)


## General info
<p>This project was made to learn how to scrape datas from a website using HTML & CSS tags.<br>I've been asked to get differents datas from all the books of all the categories available on the website (title,price,description,etc...) and save them in a CSV file.</p>
	


## Technologies

---

Project is created with:
* Python version: 3.9
* Beautifulsoup library version: 4.9.3
* Requests library: 2.25.1

## Installation

---

* Make sure you have Python 3.7+ installed. (I developed it with Python 3.9).
* Installing pip will be needed to install packages. (pip is already installed if you are using Python 2 >=2.7.9 or Python 3 >=3.4 downloaded from python.org)
* Some Python modules are required which are contained in requirements.txt and will be installed below.

<h3>Installing the requirements</h3>

<h4>Python</h4>
To make sure Python is installed on windows :
 
    python --version

On Linux, Python 3.x users may need to use: 
    
    python3 --version

If you get a "Python is not defined" message, you'll need to download it at [The python site](https://www.python.org/downloads/)
<h4>How to install PIP</h4>
on Windows :

1. Download the [get-pip.py installer](https://bootstrap.pypa.io/get-pip.py) Either way, right-click on the link and select Save As... and save it to any safe location, such as your Downloads folder. 

2. Open the Command Prompt and navigate to the get-pip.py file

3. Run the following command: `python get-pip.py`

on Mac :

    sudo easy_install pip

on Linux (Advanced Package Tool (Python 3.x)) :

    sudo apt-get install python3-pip

<h4>Installing Git</h4>
You can go the official [website of Git](https://git-scm.com/downloads) to intall it.
    

<h3>Installing the project</h3>
Open your terminal (CMD).

Choose the destination where you want to put folder that will contain the project:

    > cd YourFolderPath

Once you've picked a path for your folder we can create that folder:

	> mkdir FolderName

Now, we can clone the project in our folder by using the github https method (don't forget to be in the folder you just created):

	> git clone https://github.com/HuguesDelamare/Books-to-Scrape.git

Enter now in the project we just downloaded 

    > cd Books-to-Scrape

Installing the python environement in this folder:

  	> py -m venv YourEnvironementName

After installing the environement:

	> YourEnvName\Scripts\activate

We can now install all the libraries necessary for the project:

	> py -m pip install -r requirements.txt

The environement is functional we can now start the project:

	> py main.py

The project should start and you'll see infos of the script progression in your terminal.	



