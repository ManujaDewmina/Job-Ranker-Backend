from flask import Flask, jsonify, request
import mysql.connector
import datetime
import requests

app = Flask(__name__)

# MySQL database connection configuration
db_config = {
    'host': '127.0.0.1',
    'database': 'dm_project',
    'user': 'root',
    'password': 'root'
}

# Endpoint to add new users to user table
@app.route('/add_user', methods=['POST'])
def add_user():
    try:
        connection = mysql.connector.connect(**db_config)
        cursor = connection.cursor()

        data = request.get_json()
        userid = data.get('userid')
        username = data.get('username')
        useremail = data.get('useremail')

        query = "INSERT INTO user (userid, useremail, username) VALUES (%s, %s, %s)"
        cursor.execute(query, (userid, useremail, username))
        connection.commit()

        return jsonify(message='User added successfully')
    except Exception as e:
        return jsonify(error=str(e))
    finally:
        cursor.close()
        connection.close()

# Endpoint to add new favourites to favourite table
@app.route('/add_favourite', methods=['POST'])
def add_favourite():
    try:
        connection = mysql.connector.connect(**db_config)
        cursor = connection.cursor()

        data = request.get_json()
        userid = data.get('userid')
        firm = data.get('firm')

        query = "INSERT INTO favourite (userid, firm) VALUES (%s, %s)"
        cursor.execute(query, (userid, firm))
        connection.commit()

        return jsonify(message='favourite added successfully')
    except Exception as e:
        return jsonify(error=str(e))
    finally:
        cursor.close()
        connection.close()

# Endpoint to retrieve favourites data from favourites table
@app.route('/get_favourites', methods=['GET'])
def get_favourites():
    userid = request.args.get('userid')
    if userid is None:
        return jsonify(error="Userid parameter is required.")
    try:
        connection = mysql.connector.connect(**db_config)
        cursor = connection.cursor(dictionary=True)
        query = "SELECT * FROM favourite WHERE userid = %s"
        cursor.execute(query, (userid,))
        favouritedata = cursor.fetchall()
        return jsonify(favouritedata)
    except Exception as e:
        return jsonify(error=str(e))
    finally:
        cursor.close()
        connection.close()

# Endpoint to retrieve user data from user table
@app.route('/get_user', methods=['GET'])
def get_user():
    userid = request.args.get('userid')
    if userid is None:
        return jsonify(error="Userid parameter is required.")
    try:
        connection = mysql.connector.connect(**db_config)
        cursor = connection.cursor(dictionary=True)
        query = "SELECT * FROM user WHERE userid = %s"
        cursor.execute(query, (userid,))
        userdata = cursor.fetchall()
        return jsonify(userdata)
    except Exception as e:
        return jsonify(error=str(e))
    finally:
        cursor.close()
        connection.close()

# Endpoint to retrieve all available firm names from firm_sentiment_details table
@app.route('/firm_names', methods=['GET'])
def get_firm_names():
    try:
        connection = mysql.connector.connect(**db_config)
        cursor = connection.cursor()
        query = "SELECT DISTINCT firm FROM firm_sentiment_details"
        cursor.execute(query)
        firm_names = [row[0] for row in cursor.fetchall()]
        return jsonify(firm_names)
    except Exception as e:
        return jsonify(error=str(e))
    finally:
        cursor.close()
        connection.close()

# Endpoint to retrieve firm details based on firm name
@app.route('/firm_details', methods=['GET'])
def get_firm_details():
    firm_name = request.args.get('firm_name')
    if firm_name is None:
        return jsonify(error="Firm name parameter is required.")
    try:
        connection = mysql.connector.connect(**db_config)
        cursor = connection.cursor(dictionary=True)
        query = "SELECT * FROM firm_details WHERE firm_name = %s"
        cursor.execute(query, (firm_name,))
        firms = cursor.fetchall()
        return jsonify(firms)
    except Exception as e:
        return jsonify(error=str(e))
    finally:
        cursor.close()
        connection.close()

# Endpoint to retrieve firm sentiment details based on firm name
@app.route('/firm_sentiment_details', methods=['GET'])
def get_firm_sentiment_details():
    firm_name = request.args.get('firm_name')
    if firm_name is None:
        return jsonify(error="Firm name parameter is required.")
    try:
        connection = mysql.connector.connect(**db_config)
        cursor = connection.cursor(dictionary=True)
        query = "SELECT * FROM firm_sentiment_details WHERE firm = %s"
        cursor.execute(query, (firm_name,))
        firms_sentiment = cursor.fetchall()
        return jsonify(firms_sentiment)
    except Exception as e:
        return jsonify(error=str(e))
    finally:
        cursor.close()
        connection.close()

# Endpoint to retrieve year count based on firm name
@app.route('/year_count', methods=['GET'])
def get_year_count():
    firm_name = request.args.get('firm_name')
    if firm_name is None:
        return jsonify(error="Firm name parameter is required.")
    try:
        connection = mysql.connector.connect(**db_config)
        cursor = connection.cursor(dictionary=True)
        query = "SELECT * FROM year_count WHERE firm = %s"
        cursor.execute(query, (firm_name,))
        year_counts = cursor.fetchall()
        return jsonify(year_counts)
    except Exception as e:
        return jsonify(error=str(e))
    finally:
        cursor.close()
        connection.close()

# Endpoint to retrieve title count based on firm name
@app.route('/title_count', methods=['GET'])
def get_title_count():
    firm_name = request.args.get('firm_name')
    if firm_name is None:
        return jsonify(error="Firm name parameter is required.")
    try:
        connection = mysql.connector.connect(**db_config)
        cursor = connection.cursor(dictionary=True)
        query = "SELECT * FROM title_count WHERE firm = %s"
        cursor.execute(query, (firm_name,))
        title_counts = cursor.fetchall()
        return jsonify(title_counts)
    except Exception as e:
        return jsonify(error=str(e))
    finally:
        cursor.close()
        connection.close()

# Endpoint to retrieve average values for firm details and sentiment, sorted by selected average values in descending order
@app.route('/sorted_firm_averages', methods=['GET'])
def get_sorted_firm_averages():
    try:
        connection = mysql.connector.connect(**db_config)
        cursor = connection.cursor(dictionary=True)

        data = request.get_json()
        include_work_life_balance = data.get('work_life_balance')
        include_culture_values = data.get('culture_values')
        include_diversity_inclusion = data.get('diversity_inclusion')
        include_career_opp = data.get('career_opp')
        include_comp_benefits = data.get('comp_benefits')
        include_senior_mgmt = data.get('senior_mgmt')
        include_recommend = data.get('recommend')
        include_ceo_approv = data.get('ceo_approv')
        include_predicted_sentiments = data.get('predicted_sentiments')
        
        select_fields = []
        if include_work_life_balance:
            select_fields.append('work_life_balance')
        if include_culture_values:
            select_fields.append('culture_values')
        if include_diversity_inclusion:
            select_fields.append('diversity_inclusion')
        if include_career_opp:
            select_fields.append('career_opp')
        if include_comp_benefits:
            select_fields.append('comp_benefits')
        if include_senior_mgmt:
            select_fields.append('senior_mgmt')
        if include_recommend:
            select_fields.append('recommend')
        if include_ceo_approv:
            select_fields.append('ceo_approv')

        if include_predicted_sentiments:
            query_1 = "SELECT firm, Predicted_sentiments FROM firm_sentiment_details"
            cursor.execute(query_1)
            firm_sentiment_details = cursor.fetchall()

        if len(select_fields) != 0:
            if len(select_fields) == 1:
                select_statement = select_fields[0]
                query_2 = f"SELECT firm_name, {select_statement} FROM firm_details"
            else:
                select_statement = ", ".join(select_fields)
                query_2 = f"SELECT firm_name, {select_statement} FROM firm_details"
            cursor.execute(query_2)
            firm_details = cursor.fetchall()

        firm_data = {}

        if len(select_fields) == 0:
            if include_predicted_sentiments:
                for firm_sentiment in firm_sentiment_details:
                    firm_name = firm_sentiment['firm']
                    firm_data[firm_name] = {}
                    firm_data[firm_name]['predicted_sentiments'] = firm_sentiment['Predicted_sentiments']/2
        else:
            for firm in firm_details:
                firm_name = firm['firm_name']
                firm_data[firm_name] = {}
                for field in select_fields:
                    firm_data[firm_name][field] = firm[field]
                
                if include_predicted_sentiments:
                    for firm_sentiment in firm_sentiment_details:
                        if firm_sentiment['firm'] == firm_name:
                            firm_data[firm_name]['predicted_sentiments'] = firm_sentiment['Predicted_sentiments']/2
                            
        firm_averages = {}
        for firm in firm_data:
            firm_averages[firm] = {}
            average = 0
            for field in firm_data[firm]:
                average = average + firm_data[firm][field]
            average = average / len(firm_data[firm])
            firm_averages[firm] = average


        sorted_firm_averages = sorted(firm_averages.items(), key=lambda x: x[1], reverse=True)
        return jsonify(sorted_firm_averages)
    except Exception as e:
        return jsonify(error=str(e))
    finally:
        cursor.close()
        connection.close()

@app.route('/store_firm_review', methods=['POST'])
def store_firm_sentiment():
    try:
        connection = mysql.connector.connect(**db_config)
        cursor = connection.cursor()

        data = request.get_json()
        firm_name = data.get('firm_name')
        job_title = data.get('job_title')
        work_life_balance = data.get('work_life_balance')
        culture_values = data.get('culture_values')
        diversity_inclusion = data.get('diversity_inclusion')
        career_opp = data.get('career_opp')
        comp_benefits = data.get('comp_benefits')
        senior_mgmt = data.get('senior_mgmt')
        recommend = data.get('recommend')
        ceo_approv = data.get('ceo_approv')
        outlook = data.get('outlook')
        headline = data.get('headline')
        pros = data.get('pros')
        cons = data.get('cons')
        year = datetime.datetime.now().year

        review = headline + " " + pros + " " + cons
        sentiment_api_url = 'http://localhost:9090/predict_sentiment' 
        sentiment_data = {'review': review}
        sentiment_response = requests.post(sentiment_api_url, json=sentiment_data)
        sentiment_list = sentiment_response.json().get('sentiment')
        predicted_sentiment = sentiment_list[0][0]*10

        query = "INSERT INTO reviews (firm, job_title, work_life_balance, culture_values, diversity_inclusion, career_opp, comp_benefits, senior_mgmt, recommend, ceo_approv, outlook, headline, pros, cons, year) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
        cursor.execute(query, (firm_name, job_title, work_life_balance, culture_values, diversity_inclusion, career_opp, comp_benefits, senior_mgmt, recommend, ceo_approv, outlook, headline, pros, cons, year))
        connection.commit()

        query_1 = "SELECT * FROM firm_count WHERE firm =  %s"
        cursor.execute(query_1, (firm_name,))
        result = cursor.fetchall()
        if result:
            for row in result:
                count = row[2]
                count = count + 1
                query_1 = "UPDATE firm_count SET fcount = %s WHERE firm = %s"
                cursor.execute(query_1, (count, firm_name))
                connection.commit()

                query_5 = "SELECT * FROM firm_sentiment_details WHERE firm = %s"
                cursor.execute(query_5, (firm_name,))
                result_1 = cursor.fetchall()

                if result_1:
                    for row in result_1:
                        sentiment = row[2]
                        sentiment = ((sentiment*(count-1)) + predicted_sentiment)/count
                        query_6 = "UPDATE firm_sentiment_details SET Predicted_sentiments = %s WHERE firm = %s"
                        cursor.execute(query_6, (sentiment, firm_name))
                        connection.commit()
                
                query_7 = "SELECT * FROM firm_details WHERE firm_name = %s"
                cursor.execute(query_7, (firm_name,))
                result_2 = cursor.fetchall()
                if result_2:
                    for row in result_2:
                        work_life_balance_o = row[2]
                        culture_values_o = row[3]
                        diversity_inclusion_o = row[4]
                        career_opp_o = row[5]
                        comp_benefits_o = row[6]
                        senior_mgmt_o = row[7]
                        recommend_o = row[8]
                        ceo_approv_o = row[9]
                        work_life_balance_n = ((work_life_balance_o*(count-1)) + work_life_balance)/count
                        culture_values_n = ((culture_values_o*(count-1)) + culture_values)/count
                        diversity_inclusion_n = ((diversity_inclusion_o*(count-1)) + diversity_inclusion)/count
                        career_opp_n = ((career_opp_o*(count-1)) + career_opp)/count
                        comp_benefits_n = ((comp_benefits_o*(count-1)) + comp_benefits)/count
                        senior_mgmt_n = ((senior_mgmt_o*(count-1)) + senior_mgmt)/count
                        recommend_n = ((recommend_o*(count-1)) + recommend)/count
                        ceo_approv_n = ((ceo_approv_o*(count-1)) + ceo_approv)/count
                        query_8 = "UPDATE firm_details SET work_life_balance = %s, culture_values = %s, diversity_inclusion = %s, career_opp = %s, comp_benefits = %s, senior_mgmt = %s, recommend = %s, ceo_approv = %s WHERE firm_name = %s"
                        cursor.execute(query_8, (work_life_balance_n, culture_values_n, diversity_inclusion_n, career_opp_n, comp_benefits_n, senior_mgmt_n, recommend_n, ceo_approv_n, firm_name))
                        connection.commit()
        else:
            query_4 = "INSERT INTO firm_count (firm, fcount) VALUES (%s, %s)"
            cursor.execute(query_4, (firm_name, 1))
            connection.commit()
            
            query_2 = "INSERT INTO firm_sentiment_details (firm, Predicted_sentiments) VALUES (%s, %s)"
            cursor.execute(query_2, (firm_name, predicted_sentiment))
            connection.commit()

            query_3 = "INSERT INTO firm_details (firm_name, work_life_balance, culture_values, diversity_inclusion, career_opp, comp_benefits, senior_mgmt, recommend, ceo_approv) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)"
            cursor.execute(query_3,(firm_name, work_life_balance, culture_values, diversity_inclusion, career_opp, comp_benefits, senior_mgmt, recommend, ceo_approv))
            connection.commit()

        query_9 = "SELECT * FROM title_count WHERE firm = %s AND job_title = %s"
        cursor.execute(query_9, (firm_name, job_title))
        result_3 = cursor.fetchall()
        if result_3:
            for row in result_3:
                count = row[3]
                count = count + 1
                query_10 = "UPDATE title_count SET title_count = %s WHERE firm = %s AND job_title = %s"
                cursor.execute(query_10, (count, firm_name, job_title))
                connection.commit()
        else:
            query_11 = "INSERT INTO title_count (firm, job_title, title_count) VALUES (%s, %s, %s)"
            cursor.execute(query_11, (firm_name, job_title, 1))
            connection.commit()

        query_12 = "SELECT * FROM year_count WHERE firm = %s AND year = %s"
        cursor.execute(query_12, (firm_name, year))
        result_4 = cursor.fetchall()
        if result_4:
            for row in result_4:
                count = row[3]
                count = count + 1
                query_13 = "UPDATE year_count SET year_count = %s WHERE firm = %s AND year = %s"
                cursor.execute(query_13, (count, firm_name, year))
                connection.commit()
        else:
            query_14 = "INSERT INTO year_count (firm, year, year_count) VALUES (%s, %s, %s)"
            cursor.execute(query_14, (firm_name, year, 1))
            connection.commit()

        return jsonify(message="Data successfully stored in the database.")
    except Exception as e:
        print(e)
        return jsonify(error=str(e))
    finally:
        cursor.close()
        connection.close()


if __name__ == '__main__':
    app.run(port=8000,host='0.0.0.0')
