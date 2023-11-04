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
    csv_file_path = './csv_files/average_all_scores.csv'
    df = pd.read_csv(csv_file_path)

    # Iterate through rows of the DataFrame and insert into MySQL database
    for index, row in df.iterrows():
        query = "INSERT INTO firm_details (firm_name, work_life_balance, culture_values, diversity_inclusion, career_opp, comp_benefits, senior_mgmt, recommend, ceo_approv) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)"
        values = (
            row['firm'],
            None if pd.isna(row['work_life_balance']) else row['work_life_balance'],
            None if pd.isna(row['culture_values']) else row['culture_values'],
            None if pd.isna(row['diversity_inclusion']) else row['diversity_inclusion'],
            None if pd.isna(row['career_opp']) else row['career_opp'],
            None if pd.isna(row['comp_benefits']) else row['comp_benefits'],
            None if pd.isna(row['senior_mgmt']) else row['senior_mgmt'],
            None if pd.isna(row['recommend']) else row['recommend'],
            None if pd.isna(row['ceo_approv']) else row['ceo_approv']
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
