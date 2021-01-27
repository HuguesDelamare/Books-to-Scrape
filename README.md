## Table of contents
* [General info](#general-info)
* [Technologies](#technologies)
* [Setup](#setup)

## General info
<p>This project was made to learn how to scrap datas from a website using HTML & CSS tags.<br>
I've been asked to get datas from all the books from all categories (title,price,description,etc...) and insert/save them in a CSV file.</p>
	
## Technologies
Project is created with:
* Python version: 3.9
* Beautifulsoup library version: 4.9.3
* Requests library: 2.25.1

## Setup
Open your terminal (CMD).

Choose the destination where you want to put folder that will contain the project:

	$ cd YourFolderPath

Once you've picked a path for your folder we can create that folder:

	$ mkdir FolderName

Now, we can clone the project in our folder by using the github https method (don't forget to be in the folder you just created):

	$ git clone https://github.com/HuguesDelamare/Books-to-Scrape.git


Installing the python environement in this folder:

  	$ python -m venv EnvironementName

After installing the environement:

	$ YourEnvName\Scripts\activate

We can now install all the libraries necessary for the project:

	$ pip install -r requirements.txt

The environement is functional we can now start the project:

	$ python main.py
	

The project should start and you'll see infos of the script progression in your terminal.	
