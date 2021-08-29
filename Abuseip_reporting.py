#!/usr/bin/python
import socket, requests, json, sys

###Put your AbuseIPDB Key
abuseip_key=""

def abuseip_reporting():
    adversary_abuseip = input("""Enter the Adversary IP, Threat Type/s, Comment:
Threat Type
4   - DDOS Attack
7   - Phishing
11  - Email SPAM
14  - Port SPAM
16  - SQL Injection
17  - Spoofing Email
18  - Brute Force
19  - Bad Web bot
20  - Exploited Host
21  - Web App Attack
22  - SSH Attack

Eg: 54.240.11.2, 7, 11, Massive Phishing to our Organization
>>> """)
    adversary_abuseip = adversary_abuseip.split(",")
    adversary_ip = adversary_abuseip[0]
    adversary_input_len = len(adversary_abuseip) - 1
    adversary_threatType = ','.join([str(elem) for elem in adversary_abuseip[1:adversary_input_len]])
    adversary_cmt = adversary_abuseip[adversary_input_len]

    try:
        socket.inet_aton(adversary_ip)
        print(adversary_ip)
        print(adversary_threatType)
        print(adversary_cmt)
    except socket.error:
        print("IP Address was wrong, Try Again!")
        sys.exit(1)


    url = 'https://api.abuseipdb.com/api/v2/report'

    # String holding parameters to pass in json format
    params = {
    'ip':adversary_ip,
    'categories':adversary_threatType,
    'comment':adversary_cmt
    }
    print(params)
    headers = {
        'Accept': 'application/json',
        'Key': abuseip_key
    }

    response = requests.request(method='POST', url=url, headers=headers, params=params)

    # Formatted output
    decodedResponse = json.loads(response.text)
    print(json.dumps(decodedResponse, sort_keys=True, indent=4))

def main():
    abuseip_reporting()

if __name__ == "__main__":
    main()
