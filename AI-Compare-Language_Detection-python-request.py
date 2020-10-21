import requests

# You can find the documentation here : https://www.ai-compare.com/v1/redoc/#operation/Detect%20Language

#Enter your API Token
headers = {'Authorization': 'Bearer your API Key'} #You can get your free API token here https://www.ai-compare.com/accounts/login/?next=/my_apis

# Select API
url = 'https://www.ai-compare.com/v1/pretrained/text/language_detection

# Select providers, and text to analyze
payload = {'providers': '[\'google_cloud\', \'cognitives_service\', \'aws\', \'ibm\']','text':'I am angry today', 'language_to_find': 'en'}

# Request to AI COMPARE
response = requests.request("POST", url, headers=headers, data = payload)

# Print result
print(response.text.encode('utf8'))
