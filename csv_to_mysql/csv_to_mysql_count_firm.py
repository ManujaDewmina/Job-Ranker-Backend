import pandas as pd
import mysql.connector

# MySQL database configuration
db_config = {
    'host': '127.0.0.1',
    'database': 'dm_project',
    'user': 'root',
    'password': 'root'
}

# Establish a connection to the MySQL database
try:
    conn = mysql.connector.connect(**db_config)
    cursor = conn.cursor()

    # Read data from CSV file using pandas
    csv_file_path = './csv_files/count_per_firm.csv'
    data = pd.read_csv(csv_file_path)

    # Insert data into the MySQL table
    for index, row in data.iterrows():
        sql = "INSERT INTO firm_count (firm, fcount) VALUES ( %s, %s)"
        values = (row['firm'], row['count'])
        cursor.execute(sql, values)

    # Commit the changes and close the connection
    conn.commit()
    print("Data inserted successfully!")

except mysql.connector.Error as error:
    print("Error: {}".format(error))

finally:
    # Close the cursor and connection
    if cursor:
        cursor.close()
    if conn:
        conn.close()
