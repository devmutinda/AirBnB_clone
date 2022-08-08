# AirBnB_clone
## About
This is a Airbnb clone projects that will be build with the aim to learn and apply concepts of high level programming and software engineering in general

## Getting started
These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

### Installation
Download this repo on your computer.

### Usage
You can run the shell (in an interactive or non-interactive mode) to manipulate your models. You can start it from running the console.py file:\
```
./console.py
```

The following commands are supported in the console:
#### create
Creates a new instance of BaseModel, saves it (to the JSON file) and prints the id. Ex:\
`create BaseModel`
#### show
Prints the string representation of an instance based on the class name and id. Ex:\
`show BaseModel 1234-1234-1234.`
#### destroy
Deletes an instance based on the class name and id (save the change into the JSON file). Ex:\
`destroy BaseModel 1234-1234-1234.`
#### all
Prints all string representation of all instances based or not on the class name. Example to show all instances:\
`all`\
Example to show all instances of BaseModel only\
`all BaseModel`
#### update
Updates an instance based on the class name and id by adding or updating attribute (save the change into the JSON file). Ex:\
`update BaseModel 1234-1234-1234 email "aibnb@holbertonschool.com"`
#### quit
Quits the shell. Ex:\
`quit`

