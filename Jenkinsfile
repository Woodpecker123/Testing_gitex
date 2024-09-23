pipeline {
  agent any
  stages {
    
    // First stage: Print a message
    stage('Hello') {
      steps {
        echo 'Hi There please work'
      }
    }
     stage('Setup') {
            steps {
                script {
                    // Define variables
                    env.HOST = "http://sit.woodpecker.com"
                    env.USERNAME = "akash"
                    env.PASSWORD = "akash@2024"
                }
            }
        }
    stage('Authenticate') {
            steps {
                script {
                    def authScript = '''
import requests
import json

host = "${HOST}"
username = "${USERNAME}"
password = "${PASSWORD}"

url = f"{host}/SASLogon/oauth/token"
authBody = f'grant_type=password&username={username}&password={password}'
headersAuth = {'Accept': 'application/json', 'Content-Type': 'application/x-www-form-urlencoded'}

r = requests.post(url, data=authBody, headers=headersAuth, auth=('sas.ec', ''))

if r.status_code == 200:
    token = r.json().get('access_token')
    print(token)
else:
    print(f"Error: {r.status_code}, Response: {r.text}")
                    '''

                    writeFile file: 'auth.py', text: authScript
                    def tokenOutput = sh(script: 'source venv/bin/activate && python auth.py', returnStdout: true)
                    env.TOKEN = tokenOutput.trim()
                }
            }
        }

    
  }
}
