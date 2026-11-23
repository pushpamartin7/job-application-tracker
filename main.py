from database import get_connection,setup_database 

# add job application

def add_application():
    try:
        print("=========ADD JOB APPLICATION========")

        company =input("Enter company: ")
        role =input("Enter job role: ")
        location =input("Enter job location: ")
        applied_date=input("Enter applied date(yyyy-mm-dd): ")

        if not company or not role:
            print("company name and job role are required!")
            return
        connection =get_connection()
        cursor =connection.cursor()


        query ="""
        INSERT INTO job_applications
        (company_name,job_role,location,applied_date)
        VALUES(%s,%s,%s,%s)
        """

        Values =(company,role,location,applied_date)
        cursor.execute(query,Values)
        connection.commit()

        print("Company and job added successfully!")

        cursor.close()
        connection.close()

    except ValueError:
        print("Invalid input")
    except Exception as err:
        print("Error:",err)

def view_application():
    try:
        connection = get_connection()
        cursor =connection.cursor()
        query ="""SELECT * FROM job_applications 
        ORDER BY application_id DESC
        """

        cursor.execute(query)

        applications =cursor.fetchall()

        print("\n========VIEW ALL JOB APPLICATION======")

        if len(applications) == 0:
            print("No job available")

        else:
            for application in applications:
                print("---------------")
                print("Application ID",application[0])
                print("company name",application[1])
                print("job role",application[2])
                print("Location",application[3])
                print("Applied date",application[4])
                print("status",application[5])

                cursor.close()
                connection.close()

    except Exception as err:
        print("Error",err)


def search_application():
    try:
        search =input("Enter company name and job role to search")
        connection =get_connection()
        cursor =connection.cursor()

        query ="""
        SELECT * FROM job_applications
        WHERE company_name LIKE %s
        OR job_role LIKE %s
        """
        values =("%" + search + "%","%" +search + "%")

        cursor.execute(query,values)
        applications =cursor.fetchall()

        print("============SEARCH APPLICATION==========")

        if len(applications) == 0:
            print("No applications found!")

        for application in applications:
            print("-------------------------")
            print("Application ID:",application[0])
            print("company name:",application[1])
            print("Job role:",application[2])
            print("Location:",application[3])
            print("Applied date:",application[4])
            print("Status:",application[5])

            connection.close()
            cursor.close()

    except Exception as err:
        print("Error",err)


def update_application():
    try:
        print("\n======UPDATE APPLICATION========")

        application_id =int(input("Enter application ID: "))
        print("\nAvailable status")
        print("1.Applied")
        print("2.Interview")
        print("3.Selected")
        print("4.Rejected")

        new_status=input("Enter new status: ").strip().title()
        valid_statuses =["Applied","Interview","Selected","Rejected"]
        if new_status not in valid_statuses:
            print("Invalid status! Please enter valid status")
            return

        connection = get_connection()
        cursor =connection.cursor()

        check_query ="""
        SELECT application_id FROM job_applications
        WHERE application_id =%s
        """

        cursor.execute(check_query,(application_id,))
        application = cursor.fetchone()

        if application is None:
            print("Application not found")

        else:
            query ="""
            UPDATE job_applications
            SET status=%s
            WHERE application_id=%s
            """

        values =(new_status,application_id)
        cursor.execute(query,values)
        connection.commit()

        print("Application status Updated successfully!")
        cursor.close()
        connection.close()

    except ValueError:
        print("Invalid input! Application ID must be a number.")

    except Exception as err:
        print("Error:",err)

def delete_application():
    try:
        print("\n==========DELETE JOB APPLICATION=========")
        application_id = int(input("Enter application ID to delete:"))

        connection = get_connection()
        cursor =connection.cursor()

        check_query = """
        SELECT application_id FROM job_applications
        WHERE application_id = %s
        """

        cursor.execute(check_query,(application_id,))
        application =cursor.fetchone()

        if application is None:
            print("Application not found!")

        else:
            query = """
            DELETE FROM job_applications
            WHERE application_id =%s
            """
            cursor.execute(query,(application_id,))
            connection.commit()

            print("Application deleted successfully.")
        cursor.close()
        connection.close()

    except ValueError:
        print("Invalid input! application ID must be a number.")

    except Exception as err:
        print("Error:",err)


def application_summary():
    try:
        print("==============APPLICATION SUMMARY=============")
        connection =get_connection()
        cursor =connection.cursor()

        query ="""
        SELECT status, COUNT(*)
        FROM job_applications
        GROUP BY status
        """
        cursor.execute(query)
        results = cursor.fetchall()

        total_query = """
        SELECT COUNT(*) FROM job_applications
        """
        cursor.execute(total_query)
        total = cursor.fetchall()[0]

        print("\nTotal applications",total)

        if total == "0":
            print("No applications found")

        else:
            print("\nStatus wise summary..")

            for status, count in results:
                print("Status",":",count)

        cursor.close()
        connection.close()

    except Exception as err:
        print("Error:",err)

def main():
    setup_database()


    while True:
        print("\n==========JOB APPLICATION TRACKER=========")
        print("1.Add job application")
        print("2.View application")
        print("3.Search job application")
        print("4.Update Application status")
        print("5.Delete job application")
        print("6.Application summary")
        print("7.Exit")

        choice =(input("Enter your choice...."))
        if choice == "1":
            add_application()

        elif choice == "2":
            view_application()

        elif choice == "3":
            search_application()

        elif choice == "4":
            update_application()

        elif choice == "5":
            delete_application()

        elif choice == "6":
            application_summary()
                
        elif choice == "7":
            print("Thanks for using Job Application Tracker!")
            break

        else:
            print("Invlid choice")

if __name__ == "__main__":
    main()


