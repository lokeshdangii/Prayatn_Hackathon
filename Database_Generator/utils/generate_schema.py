from flask import Flask, render_template, request, redirect, url_for, send_file
import mysql.connector
from faker import Faker
import random


# Initialize the Faker instance
fake = Faker()

# Define your MySQL database configuration
db_config = {
    'host': 'localhost',
    'user': 'root',
    'password': '9644'
}

#  function to generate schema and for download that
def generate_schema_sql(db_name):
    try:
        connection = mysql.connector.connect(**db_config)
        cursor = connection.cursor()

        # Select the database
        cursor.execute(f"USE {db_name}")

        # Get the list of tables in the database
        cursor.execute("SHOW TABLES")
        tables = [table_details[0] for table_details in cursor.fetchall()]

        schema_sql = ''' '''
        for table_name in tables:

            cursor.execute(f"SHOW CREATE TABLE {table_name}")
            create_query = cursor.fetchone()[1]

            schema_sql += f"\n\n-- Table: {table_name}\n"
            schema_sql += f"{create_query}\n;"

    except mysql.connector.Error as err:
        return f"Error: {err}"

    finally:
        cursor.close()
        connection.close()

    return schema_sql

#----------------------------------------------------------------------------------------------------------
