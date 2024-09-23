#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Importing packages
import requests
import json


# In[2]:


host = "http://sit.woodpecker.com"
username ="akash"
password ="akash@2024"


# In[3]:


#Defining url
url = f"http://sit.woodpecker.com/SASLogon/oauth/token" 

authBody = 'grant_type=password&username=%s&password=%s' %(username, password)

headersAuth={'Accept': 'application/json', 'Content-Type': 'application/x-www-form-urlencoded'}

r =  requests.request('POST', url, data= authBody, headers=headersAuth, auth=('sas.ec', ''))

#access_token from postman
token = 'eyJhbGciOiJSUzI1NiIsImprdSI6Imh0dHBzOi8vbG9jYWxob3N0L1NBU0xvZ29uL3Rva2VuX2tleXMiLCJraWQiOiJsZWdhY3ktdG9rZW4ta2V5IiwidHlwIjoiSldUIn0.eyJqdGkiOiJiM2FhZjdlMDI5YzA0MGY0Yjk1ZTUxMjdjMWRkOGUxYiIsImF1dGhvcml0aWVzIjpbIkRhdGFBZ2VudFBvd2VyVXNlcnMiLCJEYXRhQnVpbGRlcnMiLCJFc3JpVXNlcnMiLCJTQVNBZG1pbmlzdHJhdG9ycyIsIkRhdGFBZ2VudEFkbWluaXN0cmF0b3JzIl0sImV4dF9pZCI6InVpZD1ha2FzaCxvdT1XUCxkYz12aXlhLGRjPWNvbSIsInN1YiI6ImQxOWI4M2I5LWUyNWEtNDYwOS1iYzFlLWJlYmE0OTVlNDQzZiIsInNjb3BlIjpbImNsaWVudHMucmVhZCIsIm9wZW5pZCIsInVhYS5hZG1pbiIsIlNBU0FkbWluaXN0cmF0b3JzIiwiY2xpZW50cy53cml0ZSJdLCJjbGllbnRfaWQiOiJhcHBfOTkxIiwiY2lkIjoiYXBwXzk5MSIsImF6cCI6ImFwcF85OTEiLCJncmFudF90eXBlIjoicGFzc3dvcmQiLCJ1c2VyX2lkIjoiZDE5YjgzYjktZTI1YS00NjA5LWJjMWUtYmViYTQ5NWU0NDNmIiwib3JpZ2luIjoibGRhcCIsInVzZXJfbmFtZSI6ImFrYXNoIiwiZW1haWwiOiJha2FzaEB2aXlhLmNvbSIsImF1dGhfdGltZSI6MTcyNzA3MTU0MCwicmV2X3NpZyI6ImZjYjI3ZDJlIiwiaWF0IjoxNzI3MDcxNTQwLCJleHAiOjE3MjcxMTQ3MzksImlzcyI6Imh0dHA6Ly9sb2NhbGhvc3QvU0FTTG9nb24vb2F1dGgvdG9rZW4iLCJ6aWQiOiJ1YWEiLCJhdWQiOlsiYXBwXzk5MSIsImNsaWVudHMiLCJ1YWEiLCJvcGVuaWQiXX0.g_KBFpBvAMR01O3VIiDTvF-4D1PR3yedwc0VP8RW-XlziMoiJ6EOJzjenGp3luwg2tRYKl_ZTWAfWflsXauqjCySwHRq7uEA2MNGopveQtPFmijDlc2uIWvV0F8FID9zXQSz4lRfnqBzsw_HAE6iyv1ddngKRR81XA6sIGj4KX2ayhXBCGWW6pC93k0_SFzrxNR9iRmDf6StC2HqvG7Hy9C6Il9anotmJWlUUZIbad0llFHv_YqyEeKUfdPv5B5-e64MDTrynvZ1uhtKjZMRtvobYMro4lvReC5vpBgMXbdX0fdXqgnrqr-DEt9Xd86QdA5YrAK-ET2Csp0CusNcCw'


# In[4]:


#Getting publish model information
headers = {'Authorization': 'Bearer ' + token}

url =f"http://sit.woodpecker.com/microanalyticScore/modules/" 

r = requests.request('GET', url, headers = headers, verify=False)

for key in r.json()['items']:
    print(key['name'].lower())


# In[7]:


#JSON file for selected model
headers = {'Authorization': 'Bearer ' + token}

url =f"http://sit.woodpecker.com/microanalyticScore/modules/decisiontreeclassifier/steps" 

r = requests.request('GET', url, headers = headers, verify=False) 

r.json()


# In[8]:


#Creating sample data for scoring
import requests 
import json # Define all required variables for the scoring 
LOAN = 10000 # Example value
CLAGE = 24 # Example value 
CLNO = 5 # Example value 
YOJ = 10 # Example value (Years on Job)
DELINQ = 0 # Example value
DEBTINC = 30 # Example value 
DEROG = 0 # Example value 
MORTDUE = 150000 # Example value 
VALUE = 200000 # Example value
NINQ = 2 # Example value
# Create the payload with all required fields
payload_dict = { "inputs": [ {"name": "LOAN", "value": LOAN}, 
                            {"name": "CLAGE", "value": CLAGE},
                            {"name": "CLNO", "value": CLNO}, 
                            {"name": "YOJ", "value": YOJ}, 
                            {"name": "DELINQ", "value": DELINQ}, 
                            {"name": "DEBTINC", "value": DEBTINC}, 
                            {"name": "DEROG", "value": DEROG}, 
                            {"name": "MORTDUE", "value": MORTDUE},
                            {"name": "VALUE", "value": VALUE}, 
                            {"name": "NINQ", "value": NINQ} ] } 
# Convert the Python dictionary to a JSON string
payload = json.dumps(payload_dict)
# Define the headers with content type and authorization token 
headers = { 'Content-Type': 'application/vnd.sas.microanalytic.module.step.input+json', 'Authorization': 'Bearer ' + token } 
# Define the URL for the microanalyticScore module
url = f"http://sit.woodpecker.com/microanalyticScore/modules/decisiontreeclassifier/steps/score" 
# Make the POST request with the payload 
try: 
    r = requests.post(url, data=payload, headers=headers, verify=False)
    # Check if the request was successful
    if r.status_code == 200 or r.status_code ==201:
        response = r.json() 
        print("Scoring response:", response)             
    else: 
        print(f"Error: {r.status_code}, Response: {r.text}") 
except requests.exceptions.RequestException as e: print(f"Request failed: {e}")




# In[9]:


#test

import pandas as pd

df = pd.read_csv('hmeq_s.csv')


# In[12]:


df


# In[14]:


#Using data set for model scoring
import pandas as pd
import requests
import json

# Assuming 'hmeq' is your original dataset loaded as a DataFrame
# Sample 100 rows from the original dataset
sampled_hmeq = df.sample(n=100, random_state=42)

# Remove the 'BAD' column
sampled_hmeq = sampled_hmeq.drop(columns=['BAD']).dropna()

# Define the headers for the scoring API
headers = {
    'Content-Type': 'application/vnd.sas.microanalytic.module.step.input+json',
    'Authorization': 'Bearer ' + token  # Ensure 'token' is defined
}

# Define the URL for the microanalyticScore module
url = f"https://sit.woodpecker.com/microanalyticScore/modules/decisiontreeclassifier/steps/score"

# Iterate over each row in the sampled DataFrame to make scoring requests
for index, row in sampled_hmeq.iterrows():
    # Create the payload for the current row
    payload_dict = {
        "inputs": [
            {"name": "LOAN", "value": row['LOAN']},
            {"name": "CLAGE", "value": row['CLAGE']},
            {"name": "CLNO", "value": row['CLNO']},
            {"name": "YOJ", "value": row['YOJ']},
            {"name": "DELINQ", "value": row['DELINQ']},
            {"name": "DEBTINC", "value": row['DEBTINC']},
            {"name": "DEROG", "value": row['DEROG']},
            {"name": "MORTDUE", "value": row['MORTDUE']},
            {"name": "VALUE", "value": row['VALUE']},
            {"name": "NINQ", "value": row['NINQ']}
        ]
    }

    # Convert the Python dictionary to a JSON string
    payload = json.dumps(payload_dict)

    # Make the POST request
    try:
        r = requests.post(url, data=payload, headers=headers, verify=False)

        # Check if the request was successful
        if r.status_code == 200 or r.status_code == 201:
            response = r.json()
            print(f"Scoring response for row {index}:", response)
        else:
            print(f"Error for row {index}: {r.status_code}, Response: {r.text}")

    except requests.exceptions.RequestException as e:
        print(f"Request failed for row {index}: {e}")
 



# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




