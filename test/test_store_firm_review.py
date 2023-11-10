import requests
import json

url = "http://127.0.0.1:8000/store_firm_review"

data = {
    "firm_name": "AFH-Wealth-Management",
    "job_title": " Office Administrator",
    "work_life_balance": 4,
    "culture_values": 5,
    "diversity_inclusion": 4,
    "career_opp": 5,
    "comp_benefits": 5,
    "senior_mgmt": 4,
    "recommend": 2,
    "ceo_approv": 2,
    "outlook": 3,
    "headline": "Great place to work!",
    "pros": "Amazing work environment, supportive colleagues, competitive salary.",
    "cons": "Limited growth opportunities, long working hours.",
}

headers = {
    "Content-Type": "application/json"
}

try:
    response = requests.post(url, data=json.dumps(data), headers=headers)
    response.raise_for_status()  # Raise an exception for bad requests
    print("Data successfully sent to the server.")
except requests.exceptions.HTTPError as errh:
    print(f"HTTP Error: {errh}")
except requests.exceptions.ConnectionError as errc:
    print(f"Error Connecting: {errc}")
except requests.exceptions.Timeout as errt:
    print(f"Timeout Error: {errt}")
except requests.exceptions.RequestException as err:
    print(f"Request Exception: {err}")
