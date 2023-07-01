# DocHub

DocHub is a solution to save you time and headaches. Remember when you had to access a website and you had to provide it with lots of documents? Or worse: you didn't even have those documents at hand and had to rush to search for them?

Considering all this, DocHub is a Hub of Documents. it stores all documents you want and you can use them anytime! Stop losing huge amounts of time searching for those documents and filling out forms! Make your life easier with DocHub!

<h4 align="left"> 
	Authors :pencil2:
</h4>

<p align="left">
 <a href="https://github.com/maycolteles">Maycol Teles Costa Dionisio Pereira</a> 
</p>
<p align="left">
 <a href="https://github.com/RaphaelRFreitas">Raphael Rangel Freitas</a> 
</p>

*********************

## Summary :clipboard:

* [Requirements](#requirements)
* [Setup and Installation](#setup-installation)
* [How to Use](#how-to-use)
* [Technical Information](#technical-information)
* [Final Considerations](#final-considerations)

*********************
##  Requirements :pencil: <a name="requirements"></a>

* [Python 3.10+](https://www.python.org/)
* Pip 23.0+ (comes with Python 3)

*********************
##  Setup and Installation :white_check_mark: <a name="setup-installation"></a>

### Cloning the repo :file_folder:
First off, in order to get a copy of the project to run/test it, clone the repository into a folder on your machine:

```
git clone git@github.com:MaycolTeles/projeto_c214.git
```

### Creating and Activating the Virtual Environment :open_file_folder:
It is recommended to install the dependencies inside a [virtualenv](https://docs.python.org/3/tutorial/venv.html). So, inside the folder where you cloned the repository, create a new virtualenv:

```
python3 -m virtualenv venv
```

If you don't have the virtualenv package installed, you can install it with pip:

```
pip install virtualenv
```
    
Now, activate the virtualenv (for Linux/MacOS):

```
source venv/bin/activate
```

or (for Windows):

```
.\venv\Scripts\activate
```

### Installing Dependencies :wrench:
To install all the necessary project dependencies, run the following command in the terminal (make sure you're running it from whithin your virtualenv):

```
pip install -r requirements.txt
```

### Docker :whale2: 
To run the application inside a docker container, you can run using docker-compose by running:

```
docker-compose up
```

This should start the application and the database.


*********************

## How To Use :man_technologist: <a name="how-to-use"></a>

### Executing the Project :arrow_forward:
To run the application, you can use the Makefile to run it by running:

```
make run
```

or you can use the Python interpreter directly by running:

```
python -m app.run
```

### Changing the UI/Database
To change the application's UI or Database, you need to open the `dependencies.py` module located inside `dependencies` package. When you open it, you must change the variables `USER_INTERFACE_INJECTION` and `REPOSITORY_INJECTION` to the ones you want. For example, in case you want to use Flask and MySQL, you must have something like so:

```python
USER_INTERFACE_INJECTION = FlaskUserInterface()
REPOSITORY_INJECTION = MySQLRepository()
```

But if you want to use a Desktop UI (using Tkinter) and a repository in memo, you must do like so:

```python
USER_INTERFACE_INJECTION = TkinterUserInterface()
REPOSITORY_INJECTION = InMemoRepository()
```

and so on.

*********************

##  Technical Information :pencil: <a name="technical-information"></a>

### Concepts

The application is written in Python, using concepts of:
* Clean Architecture
* Clean Code
* SOLID
* TDD

### Technologies
Some of the technologies are listed below:

#### UI
* Django
* Flask
* Tkinter

#### Repository
* In Memory
* MongoDB
* MySQL
* SQLite

To check the technical information in detail you can check [this docs](docs/technical_information.md).

*********************
## Final Considerations :pushpin: <a name="final-considerations"></a>

### TODO: May be add a EntityDTO to send the DTO directly to database?