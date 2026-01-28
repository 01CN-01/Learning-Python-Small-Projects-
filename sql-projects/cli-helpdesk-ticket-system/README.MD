🛠️ CLI Help Desk Ticket System
Python | SQLite | SQL | Logging | Error Handling
A command-line Help Desk Ticket System built with Python and SQLite, demonstrating strong backend fundamentals including SQL CRUD operations, role-based access control, logging, and robust error handling.
Designed to showcase skills relevant to junior software developer roles.

🔍 Project Overview
This application allows users to register, log in, and manage support tickets.
The system enforces ownership rules and permissions at the database level, ensuring users can only modify their own data while staff users have elevated access.

✅ Key Features
User Authentication & Roles
User registration and login

Role-based access:
User – manage own tickets
Staff/Admin – manage all tickets
Ticket Management (CRUD)
Create support tickets
View tickets (own or all, depending on role)
Edit tickets with ownership validation
Delete tickets safely using row-count verification
Automatic ticket timestamps via SQLite
Database & SQL
SQLite database with persistent storage
Parameterised SQL queries to prevent SQL injection
Secure UPDATE and DELETE operations using:
WHERE constraints
cursor.rowcount validation
Logging & Error Handling
Application logging for key actions (logins, ticket operations)
Centralised input validation:
Integers
Email format
Password strength

Graceful handling of:
Invalid input
Non-existent records
Permission violations
Prevents application crashes through defensive programming

🧱 Tech Stack
Python 3
SQLite
SQL
Command Line Interface (CLI)

🗄️ Database Schema
-- Users --
Column	Description
studentid	Primary key
firstname	User first name
lastname	User last name
email	Login email
password	User password
role	User / Staff

-- Tickets --
Column	Description
ticketid	Primary key
created_by	User ID (foreign key)
subject	Ticket title
description	Ticket details
created_at	Auto timestamp

🔐 Security & Access Control
Users can only update/delete tickets they own
Staff/Admin users can manage all tickets
SQL-level validation prevents unauthorised data access
All queries use placeholders (?) for safety

▶️ Running the Project
python main.py


ℹ️ During development, deleting users.db will reset the database schema.

🎯 What This Demonstrates to Employers
Strong understanding of SQL fundamentals
Practical use of database persistence
Clean separation of concerns
Defensive programming with logging and validation
Real-world access control logic
Ability to design a complete backend workflow independently

🚀 Possible Enhancements
Password hashing (bcrypt)
Ticket status tracking
Search & filtering
Unit tests
Refactoring into service/repository layers

👤 Author
Built as a practical backend learning project to prepare for junior software developer roles