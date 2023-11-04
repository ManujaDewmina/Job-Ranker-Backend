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
    csv_file_path = './csv_files/all_reviews.csv'
    data = pd.read_csv(csv_file_path)

    # Insert data into the MySQL table
    for index, row in data.iterrows():
        sql = "INSERT INTO reviews (firm, job_title, work_life_balance, culture_values, diversity_inclusion, career_opp, comp_benefits, senior_mgmt, recommend, ceo_approv, outlook, headline, pros, cons, year) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
        values = (row['firm'], row['job_title'], row['work_life_balance'], row['culture_values'], row['diversity_inclusion'], row['career_opp'], row['comp_benefits'], row['senior_mgmt'], row['recommend'], row['ceo_approv'], row['outlook'],
                None if pd.isna(row['headline']) else row['headline'],
                None if pd.isna(row['pros']) else row['pros'],
                None if pd.isna(row['cons']) else row['cons'],
                row['year'])
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
