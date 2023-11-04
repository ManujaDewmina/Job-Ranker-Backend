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

    # Read CSV file into a pandas DataFrame
    csv_file_path = './csv_files/title_counts.csv'
    df = pd.read_csv(csv_file_path)

    # Iterate through rows of the DataFrame and insert into MySQL database
    for index, row in df.iterrows():
        query = "INSERT INTO title_count (firm, job_title, title_count) VALUES (%s, %s, %s)"
        values = (
            row['firm'],
            None if pd.isna(row['job_title']) else row['job_title'],
            None if pd.isna(row['title_count']) else row['title_count'],
        )
        cursor.execute(query, values)

    # Commit the changes and close the connection
    conn.commit()
    print("Data inserted successfully into MySQL database!")

except mysql.connector.Error as err:
    print("Error: {}".format(err))

finally:
    # Close the cursor and connection
    if cursor:
        cursor.close()
    if conn:
        conn.close()
