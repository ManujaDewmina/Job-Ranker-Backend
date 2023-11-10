import requests
import json

# URL of the Flask endpoint
url = "http://192.168.1.11:8000/sorted_firm_averages"

def test_sorted_firm_averages_endpoint():
    try:
        # Send boolean parameters indicating which fields to include in the calculation
        data = {
            'work_life_balance': False,
            'culture_values': False,
            'diversity_inclusion': False,
            'career_opp': False,
            'comp_benefits': False,
            'senior_mgmt': False,
            'recommend': False,
            'ceo_approv': True,
            'predicted_sentiments': False
        }

        headers = {
            "Content-Type": "application/json"
        }
        response = requests.get(url,data=json.dumps(data), headers=headers)
        if response.status_code == 200:
            print("Sorted firm names:")
            print(response.json())
        else:
            print(f"Error: {response.status_code} - {response.text}")
    except Exception as e:
        print(f"An error occurred: {str(e)}")

if __name__ == "__main__":
    test_sorted_firm_averages_endpoint()
