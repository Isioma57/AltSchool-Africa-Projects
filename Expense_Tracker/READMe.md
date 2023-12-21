# Expense Tracking System

<p align="center">
  <img alt="Expense" width="400" src="https://cdn.business2community.com/wp-content/uploads/2016/12/financials-600x400.jpg">
</p>

## 📕 Table Of Contents
* [Project Overview](#project-overview)
    * [Class Summary](#class-summary)
    * [Instructions](#instructions)
    * [Execution](#execution)
* [Cloning Instructions](#cloning-instructions)
* [Running the code](#running-the-code)


# Project Overview
Expense Tracker is a Python application designed to help users or establishments in monitoring their day-to-day spendings. It offers a straightforward and user-friendly interface for recording and managing expenses.

This project involves the implementation of two classes, Expense and ExpenseDatabase.It entails defining classes with relevant attributes and methods to represent real-world expense data, implementing data handling and manipulation techniques and working with time-related functionalities. Below is a preview of the class attributes and methods.

## Class Summary
### Expense Class:

Represents an individual financial expense.

**Attributes:**
1. **```id```**: A unique identifier generated as a UUID string.
2. **```title```**: A string representing the title of the expense.
3. **```amount```**: A float representing the amount of the expense.
4. **```created_at```**: A timestamp indicating when the expense was created (UTC).
5. **```updated_at```**: A timestamp indicating the last time the expense was updated (UTC).

**Methods:**
1. **```__init__```**: Initializes the attributes.
2. **```update```**: Allows updating the title and/or amount, updating the updated_at timestamp.
3. **```to_dict```**: Returns a dictionary representation of the expense.


   
### ExpenseDB class

Manages a collection of Expense objects.

**Attributes:**
1. **```expenses```**: A list storing Expense instances.
   
**Methods:**
1. **```__init__```**: Initializes the list.
2. **```add_expense```**: Adds an expense.
3. **```remove_expense```**: Removes an expense.
4. **```get_expense_by_id```**: Retrieves an expense by ID.
5. **```get_expense_by_title```**: Retrieves expenses by title.

## Instructions

### Expense class

1. Implement an __init__ method to initialize the attributes.
2. Implement an update method that allows updating the title and/or amount of the
expense. The updated_at attribute should be automatically set to the current UTC
timestamp whenever an update occurs.
3. Implement a to_dict method that returns a dictionary representation of the expense.

### ExpenseDB class

1. Implement an __init__ method to initialize the expenses list.
2. Implement methods to:
   * Add an expense to the database.
   * Remove an expense from the database.
   * Get an expense by ID.
   * Get expenses by title (returning a list).
3. Create a to_dict method that returns a list of dictionaries representing each expense in
the database.

## Execution

### Expense class

#### **1. Implement an __init__ method to initialize the attributes.**
```python
import uuid 
from datetime import datetime, timezone

class Expense:
    def __init__(self, title, amount):
        self.id = str(uuid.uuid4())
        self.title = title
        self.amount = amount
        self.created_at = datetime.utcnow()
        self.updated_at = self.created_at
```
This code sets up a basic expense tracking system with unique IDs, titles, amounts, and timestamps for creation and last update.

The uuid is set to uuid4 because this version generates a random UUID, which has a very low chance of collision with other UUIDs. The ```self.updated_at``` matches the ```self.created_at``` because when an Expense object is first created, it has not been updated yet, so the ```updated_at timestamp``` is set to be the same as the ```created_at``` timestamp.

#### **2. Implement an update method that allows updating the title and/or amount of the expense.** 
```python    
    def update(self, title = None, amount = None):
        if title is not None:
            self.title = title
        if amount is not None:
            self.amount = amount
        self.updated_at = datetime.utcnow()
```
 This update method allows you to modify the title and/or amount of an existing expense and updates the timestamp for the last update. If no new title or amount is provided, the method does not make any changes to the respective attributes, but it still updates the ```updated_at``` timestamp.

#### **3. Implement a to_dict method that returns a dictionary representation of the expense.**
```python
    def to_dict(self):
        return {
        "id": self.id,
        "title": self.title,
        "amount": self.amount,
        "created_at": self.created_at.isoformat(),
        "updated_at": self.updated_at.isoformat()
        }
```
This method creates a dictionary with the key-value pairs. When you call the to_dict method on an instance of the Expense class, it will return a dictionary containing the details of that expense. 

The creation and updated timestamp of the expense is in ISO 8601 format. ```The isoformat()``` method is used to convert the datetime object to a string in ISO format. This format provides a standardized and unambiguous way to represent dates and times.

### ExpenseDataBase class

#### **1. Implement an __init__ method to initialize the expenses list.**
```python      
class ExpenseDatabase:
    def __init__(self):
        self.expenses = []
```
The ExpenseDatabase class is created to represent an expense database. An empty list called ```expenses``` is initialized to provide a foundation for storing and managing instances of the Expense class.

#### **2. Implement methods to:**
   * Add an expense to the database.
```python
    def add_expense(self, expense):
        self.expenses.append(expense)
```
This method adds an expense object to the database.
   
   * Remove an expense from the database.
```python
    def remove_expense(self, expense_id):
        self.expenses = [exp for exp in self.expenses if exp.id != expense_id]
```
The remove_expense method removes a specific expense from this database based on its unique ID.  The process involves checking each expense in the database; an expense is included in the newly created list only if its ID does not match the expense_id.
   
   * Get an expense by ID.
```python
    def get_expense_by_id(self, expense_id):
        for exp in self.expenses:
            if exp.id == expense_id:
                return exp
        return None
```
This method retrieves an expense by it's ID. If the id of the current expense matches expense_id, the found expense is returned. If no expense with the matching ID is found, 'None' is returned.
                  
   * Get expenses by title (returning a list).
```python
    def get_expense_by_title(self, title):
        return [expense for expense in self.expenses if expense.title == title]
```
This method retrieves a list of expenses by their title. 

#### **3. Create a to_dict method that returns a list of dictionaries representing each expense in the database.**
```python
    def to_dict(self):
        return [expense.to_dict() for expense in self.expenses]
```
The to_dict method creates a list of dictionaries where each dictionary represents the attributes of an expense in the database.

# Cloning Instructions
Below is a step by step guide on how to clone this project to your local computer:

* Open a terminal window.This can be Command Prompt on Windows, Terminal on Mac/Linux or Git Bash Terminal.
* For git bash terminal, ensure that you are on your home directory by running ```cd``` without any arguments.
* Create a directory where you'd like to store the repo. You can do so by typing the following command
```bash
mkdir <directory>
```
* In the terminal, navigate to the location in which you would like to store the repo
```bash
cd <directory>
```
* Copy the repository URL
* Use the git clone command to clone the repo:
```bash
git clone <repo-url>
```
In this case:
```bash
git clone https://github.com/Isioma57/AltSchool-Africa-Projects.git
```
* Give the process a few moments to complete. 
* Check to make sure that the repository is on your local computer. To do so, navigate to the directory in which it was stored.

# Languages or Frameworks Used

This application requires Python to run. No external libraries are used, making it easy to set up and run on any system with Python installed.

# Running the code

To execute the code using Git Bash or any terminal, follow these steps:

* Ensure you have Python installed on your system.

* Navigate to the project directory where expense_tracker.py is saved.

* Run the Script:
```
python expense_tracker.py
```
#### Note:

* Ensure that you are in the correct directory containing the script.

* If the terminal displays no error messages, the code has successfully executed. 





