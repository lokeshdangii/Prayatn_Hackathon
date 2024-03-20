# AI-Based Data Genesis System

This project is a data generation and database management system that leverages the Eden AI API to create realistic data and manage databases seamlessly.

## Features

- Generate realistic data using the Eden AI API.
- Create database schema based on user input (database name, number of tables, table columns).
- Populate the database with realistic data entries.
- Download the database schema in an SQL file format.
- User-friendly web interface for easy interaction.

## Tech Stack

- Frontend: HTML, CSS, JavaScript
- Backend: Flask (Python)
- Database: MySQL

## Directory Hierarchy

```
.
├── config.py
└── Database_Generator
    ├── __init__.py
    ├── static
    │   ├── index_style.css
    │   ├── outer_style.css
    │   ├── script.js
    │   ├── style.css
    │   └── table_style.css
    ├── templates
    │   ├── index.html
    │   ├── output.html
    │   └── table.html
    └── utils
        ├── api.py
        ├── create_tables.py
        ├── generate_schema.py
        └── insert_query.py
```

## Getting Started

1. Clone this repository to your local machine:
   ```
   git clone https://github.com/lokeshdangii/Prayatn_Hackathon
   ```

2. Navigate to the project directory:
   ```
   cd Prayatn_Hackathon
   ```

3. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```

4. Set up your API key for the Eden AI API in `config.py`.

5. Run the application using Flask:
   ```
   python Database_Generator/__init__.py
   ```

6. Access the web interface in your browser at [http://localhost:5000](http://localhost:5000).

## Usage

1. Open the web interface and provide the database name and number of tables.
2. For each table, specify column details (name and data type separated by a colon).
3. Submit the form to create the database schema and populate it with realistic data.
4. Download the generated database schema in an SQL file format for further use.

## Contributors

- [Lokesh Dangi](https://github.com/lokeshdangii)
- [Paritosh Verma](https://github.com/Rockposedon)
- [Anil-Gehlot](https://github.com/anil-gehlot)
- [Priyanshi Verma](https://github.com/ps1231)