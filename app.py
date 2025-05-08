import requests
import json
import os

# Paste your bearer token here
bearer_token = 'eyJ0eXAiOiJKV1'

# Paste the url of the chat in the place of {url}
url = 'https://{url}/api'


# You don't need to update anything below
headers = {
    'Authorization': f'Bearer {bearer_token}'
}

# Send the GET request
response = requests.get(f"{url}/chatHistory", headers=headers)

# Check if the request was successful
if response.status_code == 200:
    # Get all your chatIds 
    data = response.json()
    chatIds = []
    
    for chat in data:   
        chatIds.append(chat["chatId"])
    
    # Download each chat's response into a json file.
    for chatId in chatIds:
        chatHistoryResponse = requests.get(f"{url}/chatHistory/{chatId}", headers=headers)
        
        chatData = chatHistoryResponse.json()
        
        folder_path = 'chats'
        
        file_path = os.path.join(folder_path, f"{chatData["title"]}.json")
        with open(file_path, 'w') as json_file:
            json.dump(chatData, json_file, indent=4)

else:
    print(f'Failed to retrieve data: {response.status_code}')
