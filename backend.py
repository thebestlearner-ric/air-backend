from flask import Flask, jsonify
from flask_cors import CORS
import requests

app = Flask(__name__)

# Define the base URL and API key for the Open ATMS API
BASE_URL = "https://open-atms.airlab.aero/api/v1"
API_KEY = "NfDGWCgOJdNQrBlDFmz0IYGarZGsbeCQuY3fTUvZRLxtcNwizO5NY2IRmD3db5vS"

@app.route('/sids/airport/<icao_code>', methods=['GET'])
def get_sids_airport_info(icao_code):
    """
    Query Open ATMS API to get information about a specific airport.
    """
    url = f"{BASE_URL}/airac/sids/airport/{icao_code}"
    headers = {'api-key': API_KEY}
    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        return jsonify(response.json())
    else:
        return jsonify({"error": "Error retrieving airport information."}), 500

@app.route('/stars/airport/<icao_code>', methods=['GET'])
def get_stars_airport_info(icao_code):
    """
    Query Open ATMS API to get information about a specific airport.
    """
    url = f"{BASE_URL}/airac/stars/airport/{icao_code}"
    headers = {'api-key': API_KEY}
    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        return jsonify(response.json())
    else:
        return jsonify({"error": "Error retrieving airport information."}), 500


@app.route('/all_airports', methods=['GET'])
def get_all_airport_info():
    """
    Query Open ATMS API to get information about a specific airport.
    """
    url = f"{BASE_URL}/airac/airports/"
    headers = {'api-key': API_KEY}
    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        return jsonify(response.json())
    else:
        return jsonify({"error": "Error retrieving airport information."}), 500

if __name__ == "__main__":
    cors = CORS(app)
    app.run(debug=True, host='0.0.0.0')
