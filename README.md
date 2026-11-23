
# Job Application Tracker

A Python and MySQL based console application to manage and track job applications.

## Project Overview

The Job Application Tracker helps users maintain their job application records in one place. Users can add new applications, view existing records, search applications, update application statuses, delete records, and view application summaries.

## Features

- Add new job applications
- View all job applications
- Search applications
- Update application status
- Delete job application records
- View application summary by status
- Store application data in a MySQL database

## Technologies Used

- Python
- MySQL
- mysql-connector-python
- python-dotenv
- Git
- GitHub

## Project Structure

```text
job_application_tracker/
│
├── main.py
├── database.py
├── README.md
├── .gitignore
└── .env
```

## Setup and Installation

1. Clone the repository:

```bash
git clone https://github.com/pushpamartin7/job-application-tracker.git
```

2. Open the project folder.

3. Install the required packages:

```bash
pip install mysql-connector-python python-dotenv
```

4. Create a MySQL database and configure your database credentials in a `.env` file.

Example `.env` configuration:

```env
DB_HOST=localhost
DB_USER=my_username
DB_PASSWORD=mysql_password
DB_NAME=job_tracker_db
```

5. Run the application:

```bash
python main.py
```

## Learning Outcomes

Through this project, I practised:

- Python functions and exception handling
- CRUD operations
- MySQL queries
- Python and MySQL connectivity
- Environment variables
- Git and GitHub version control

## Author

**Pushpa Martin**

GitHub: https://github.com/pushpamartin7
