Inventory System (Python)
Overview

This is a command-line inventory system written in Python.
It allows items to be stored with a quantity and price, calculates totals, and saves data using a CSV file so information persists between runs.

This project was built while self-teaching Python to practice file handling, data validation, and program structure.

---Features---
Load inventory data from a CSV file on startup
Create the CSV file if it does not exist
Add inventory items (quantity, name, price)
Validate user input (integers, floats, empty input)
Calculate item totals and overall inventory value
Display formatted currency output (2 decimal places)

---Technologies Used---
Python
CSV (csv.DictReader / csv.DictWriter)
Object-Oriented Programming (OOP)
Error handling (try / except ValueError)

---How It Works---
The program attempts to read from a CSV file when it starts
CSV data is loaded into a list of dictionaries
All numeric values are converted from strings before calculations
Item totals are calculated using price × quantity
A running total is used to calculate the full inventory value
Data is written back to the CSV file to persist changes

---What I Learned---
CSV files always store data as strings
The difference between DictReader and Reader
Why data must be converted before performing calculations
How to safely handle missing or invalid data
How to structure a small project using multiple files

---Possible Improvements---
Edit inventory items
Sort inventory by price or quantity
Move storage from CSV to a database (SQLite)