import requests

# Replace with your actual EC2 instance IP and port if not using the default port 5000
BASE_URL = "http://54.68.238.162:5000"

def check_app_status():
    try:
        response = requests.get(BASE_URL)
        if response.status_code == 200:
            print("The Flask app is running successfully!")
        else:
            print(f"Failed to reach the app. Status code: {response.status_code}")
    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    check_app_status()
