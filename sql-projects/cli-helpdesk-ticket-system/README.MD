🛠️ CLI Help Desk Ticket System
Python | SQLite | SQL | Logging | Error Handling

A command-line Help Desk Ticket System built with Python and SQLite.
The application focuses on backend fundamentals such as SQL CRUD operations, role-based access control, input validation, and defensive error handling.

Designed to showcase skills relevant to junior software developer roles, with an emphasis on clean logic and real-world constraints.

🔍 Project Overview
This application allows users to register, log in, and manage support tickets via a CLI interface.
The system enforces ownership rules and role-based permissions, ensuring:
Standard users can only manage their own tickets
Staff/Admin users have elevated access to manage all tickets
Data integrity and access control are enforced at both the application and database level.

✅ Key Features
User Authentication & Roles
User registration and login
Role-based access control:
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
cursor.rowcount validation to confirm successful operations
Logging & Error Handling
Application logging for key actions:
Logins
Ticket creation, updates, and deletions
Centralised input validation for:
Integers
Email format
Password strength

Graceful handling of:
Invalid input
Non-existent records
Permission violations
The application uses defensive programming techniques to prevent crashes and inconsistent state.

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
Users can only update or delete tickets they own
Staff/Admin users can manage all tickets
SQL-level validation prevents unauthorised data access
All database queries use placeholders (?) for safety

▶️ Running the Project
python main.py


ℹ️ Deleting users.db will reset the database schema during development.

🎯 What This Demonstrates to Employers
Strong understanding of SQL fundamentals and relational data
Practical use of database persistence
Real-world access control and permission logic
Defensive programming with logging and validation
Ability to design and implement a complete backend workflow independently

🚀 Possible Enhancements
Password hashing (bcrypt)
Ticket status tracking
Search and filtering
Expanded automated testing
Refactoring into service / repository layers

👤 Author
Built as a practical backend project to prepare for junior software developer roles.