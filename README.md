# AirBnB_clone
## 🧐 About
This is a Airbnb clone project that is built with the aim of learning and applying concepts of high level programming.

## 🏁 Getting started
These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.\
First, download this repo on your computer.

## 🔧 Testing
This project uses the python unittest model for automated tests.\
You can run the tests as shown below:
```
python3 -m unittest discover tests
```
## 🎈 Usage
You can run the shell (in an interactive or non-interactive mode) to manipulate your models. You can start it from running the console.py file on your linux terminal:
```
./console.py
```
The prompt `(hbnb) ` will appear on your terminal to show that the console is now active, and that you can enter a series of commands to interact with the data models(classes)\

To check which commands are supported by the console, type `help` and click enter.\
The following commands are supported in the console:
### create
Creates a new instance of BaseModel, saves it (to the JSON file) and prints the id. Ex:
```
create BaseModel
```
### show
Prints the string representation of an instance based on the class name and id. Ex:
```
show BaseModel 1234-1234-1234.
```
### destroy
Deletes an instance based on the class name and id (save the change into the JSON file). Ex:
```
destroy BaseModel 1234-1234-1234.
```
### all
Prints all string representation of all instances based or not on the class name. Example to show all instances:
```
all
```
Example to show all instances of BaseModel only
```
all BaseModel
```
### update
Updates an instance based on the class name and id by adding or updating attribute (save the change into the JSON file). Ex:
```
update BaseModel 1234-1234-1234 email "aibnb@holbertonschool.com"
```
### quit
Quits the shell. Ex:
```
quit
```
## ✍️Authors
* [@devmutinda](https://github.com/devmutinda)
* [@Dayvies](https://github.com/Dayvies)

