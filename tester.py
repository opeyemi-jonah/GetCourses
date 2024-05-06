import requests

def Test():
    # Define the URL of the Flask app
    url = "http://localhost:5000/extract-text"

    # Define the data to send in the POST request
    data = {
        "text": "Schedule For: 010145005 SOTELO, LUZ Term: SUMMER 2023 SUBJ CRSE COURSE TITLE ENGL 1110 COMPOSITION I CREDS G 3 T Course Credits: 3"
    }

    # Send the POST request with JSON data
    response = requests.post(url, json=data)

    # Check the response
    if response.status_code == 200:
        print("Success:", response.json())
    else:
        print("Error:", response.status_code, response.text)

Test()