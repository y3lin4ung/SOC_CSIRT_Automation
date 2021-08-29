import requests, os

###Put your AbuseIPDB Key
abuseip_key=""

# Defining the api-endpoint
url = 'https://api.abuseipdb.com/api/v2/blacklist'

querystring = {
    'limit':'10000'
}

headers = {
    'Accept': 'text/plain',
    'Key': abuseip_key
}

response = requests.request(method='GET', url=url, headers=headers, params=querystring)

# Formatted output
dir_path = os.path.dirname(os.path.realpath(__file__))
print(dir_path)
abusefilelocation = dir_path + "\\AbuseIP_Top10000.txt"
file1 = open(abusefilelocation,"w")
file1.writelines(response.text)
print("Generating AbuseIPDB TOP 10,000 IOCs is finished")
