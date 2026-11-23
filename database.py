import mysql.connector
import os
from dotenv import load_dotenv

load_dotenv()

# Database connection
def get_connection():
    return mysql.connector.Connect(
        host =os.getenv("DB_HOST"),
        user =os.getenv("DB_USER"),
        password =os.getenv("DB_PASSWORD"),
        database =os.getenv("DB_NAME")

    )
    return connection
# Check database connection
def test_connection():
    try:
        connection =get_connection()

        if connection.is_connected():
            print("Mysql database successfully connected!")

        connection.close()

    except mysql.connector.Error as err:
        print("Database connection:",err)

# create table
def setup_database():
    try:

        connection = get_connection()
        cursor =connection.cursor()


        query ="""
        CREATE TABLE IF NOT EXISTS job_applications(
            application_id INT AUTO_INCREMENT PRIMARY KEY,
            company_name VARCHAR(100) NOT NULL,
            job_role VARCHAR(100) NOT NULL,
            location VARCHAR(100),
            applied_date DATE,
            status VARCHAR(30) DEFAULT 'Applied'
        )"""
        cursor.execute(query)
        connection.commit()

        print("Database table ready!")
        cursor.close()
        connection.close()

    except mysql.connector.Error as err:
        print("Database setup error:",err)


