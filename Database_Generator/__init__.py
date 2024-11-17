
from flask import Flask, render_template, request,  send_file
import mysql.connector
from .utils.generate_schema import generate_schema_sql
from .utils.insert_query import generate_insert_query
from .utils.create_tables import create_table
# from .utils.insert_query import generate_insert_query
# from .utils import generate_insert_query
import requests
import tempfile  # For creating temporary files
import os
# from .utils import api
from config import get_db_config


app = Flask(__name__)


@app.route('/')
def index():
    # api_code = api.api_calling()
    # return render_template('index.html', api_code=api_code)
    return render_template('index.html')


# this function will be triggered by index.html
@app.route('/create_tables/', methods=['POST'])
def create_tables():
    global db_name, db_host, db_user, db_password 
    db_name  = request.form['dbName']
    num_tables = int(request.form['numTables'])
    
    db_host = request.form['hName']
    db_user = request.form['user']
    db_password = request.form['pass']
    return render_template('table.html', db_name=db_name, num_tables=num_tables,db_host=db_host, db_user=db_user, db_password=db_password)


@app.route('/submit_table_details/<db_name>/<int:num_tables>/', methods=['POST'])
def table_details(db_name, num_tables):
    
    table_name_list = request.form.getlist('tableName')
    column_details_list = request.form.getlist('columnDetails')

    messages = []

    # connection = mysql.connector.connect(**db_config)
    # cursor = connection.cursor()
    
    db_config = get_db_config(db_host, db_user, db_password)
    connection = mysql.connector.connect(**db_config)
    cursor = connection.cursor()


    # Create database if not exists
    cursor.execute(f"CREATE DATABASE IF NOT EXISTS {db_name}")
    cursor.execute(f"USE {db_name}")


    # Iterate through the provided table names and column details
    num = 1
    for table_name, column_details in zip(table_name_list, column_details_list):
        create_query = create_table(column_details, table_name)
        
        try:

            cursor.execute(f"SHOW TABLES LIKE '{table_name}' ")
            existing_table = cursor.fetchone()

            if existing_table:
                existing_table = existing_table[0]
                messages.append( (f'Table {num}', table_name, 'Table already exists.') )
                num += 1

            else:
                
                # Execute the create table query
                cursor.execute(create_query)
                connection.commit()
                messages.append( (f'Table {num}', table_name, 'Table created successfully') )
                num += 1

                try:
                    for entry in range(1):
                        insert_query = generate_insert_query(table_name, column_details)
                        print(insert_query)
                        cursor.execute(insert_query)
                        connection.commit()

                except mysql.connector.Error as err:
                    messages.append( (f'Table Name : ', f'{table_name} insertion error', err) )


        except mysql.connector.Error as err:
            cursor.execute(f"DROP TABLE IF EXISTS {table_name};")
            messages.append( (f'Table {num}', f'{table_name} creation error', err) )
            num += 1
    cursor.fetchall()
    cursor.close()
    connection.close()

    total = 0
    for message in messages:
        if message[2]=='Table created successfully' or message[2]=='Table already exists.':
            total += 1

    return render_template('output.html', messages=messages, total= total, num_tables=num_tables, db_name=db_name )



#  to download the schema file
@app.route("/download_schema/<db_name>", methods=['GET','POST'])
def download_schema(db_name):

    if request.method == 'POST':

        schema_sql = generate_schema_sql(db_name,db_host,db_user,db_password)

        # Save the SQL to a file
        # file_path = f"/home/priyanshi/deployment/Prayatn_Hackathon/Database_Generator{db_name}_schema.sql"
        if os.name == 'posix':  # For Linux/macOS
            download_folder = os.path.expanduser("~/Downloads")
        elif os.name == 'nt':  # For Windows
            download_folder = os.path.join(os.environ['USERPROFILE'], 'Downloads')
        else:
            # Fallback for other OSes
            download_folder = '/tmp'  # default to a temp folder if unknown

        # Define the full path for the SQL file
        file_path = os.path.join(download_folder, f"{db_name}_schema.sql")

        with open(file_path, 'w') as file:
            file.write(schema_sql)

        # Provide the file for download
        return send_file(file_path, as_attachment=True) # If set to True, the file will be sent as an attachment


if __name__ == '__main__':
    app.run(debug=True)
