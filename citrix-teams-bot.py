import requests
import json

def login():
    login_url = ''
    headers = {'Content-Type': 'application/json'}
    data = {'username': 'your_username', 'password': 'your_password'}

    response = requests.post(login_url, headers=headers, data=json.dumps(data))
    if response.status_code == 200:
        return response.json()['access_token']
    else:
        raise Exception('Login failed')

def check_endpoint_status(access_token):
    endpoint_status_url = ''
    headers = {'Authorization': 'Bearer ' + access_token}

    response = requests.get(endpoint_status_url, headers=headers)
    if response.status_code == 200:
        return response.json()['status']
    else:
        raise Exception('Failed to fetch endpoint status')

def reset_endpoint(access_token):
    reset_url = ''
    headers = {'Authorization': 'Bearer ' + access_token}

    response = requests.post(reset_url, headers=headers)
    if response.status_code == 200:
        print('Endpoint reset successfully')
    else:
        raise Exception('Failed to reset endpoint')

def send_diagnostics(access_token):
    diagnostics_url = ''
    headers = {'Authorization': 'Bearer ' + access_token}

    diagnostics_data = {'message': 'Diagnostic information'}

    response = requests.post(diagnostics_url, headers=headers, data=json.dumps(diagnostics_data))
    if response.status_code == 200:
        print('Diagnostics sent successfully')
    else:
        raise Exception('Failed to send diagnostics')

def send_to_teams(message):
    webhook_url = 'YOUR_WEBHOOK_URL'

    headers = {'Content-Type': 'application/json'}
    payload = {'text': message}

    response = requests.post(webhook_url, headers=headers, data=json.dumps(payload))

    if response.status_code == 200:
        print('Message sent to Teams successfully.')
    else:
        print('Failed to send message to Teams.')

def main():
    try:
        access_token = login()
        endpoint_status = check_endpoint_status(access_token)
        
        if endpoint_status == 'connected':
            message = 'Endpoint is connected. Resetting...'
            reset_endpoint(access_token)
            send_diagnostics(access_token)
            send_to_teams(message)
            print('Endpoint reset and diagnostics sent successfully.')
        else:
            message = 'Endpoint is not connected.'
            send_to_teams(message)
            print('Endpoint is not connected.')
    except Exception as e:
        print('An error occurred:', str(e))

if __name__ == "__main__":
    main()
