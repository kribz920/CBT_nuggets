import requests
import json


########### LOGIN ############
url =  "https://sandboxapicdc.cisco.com/api/aaaLogin.json"

payload = {
    "aaaUser": {
        "attributes": {
            "name": "admin",
            "pwd": "!v3G@!4@Y"
        }
    }
}
headers = {
    'Content-Type': "application/json"
}

response = requests.post(url, data=json.dumps(
    payload), headers=headers, verify=False).json()

# print(json.dumps(response, indent=2, sort_keys=True))

########### Parse Token ############

token = response['imdata'][0]['aaaLogin']['attributes']['token']
cookie = {}
cookie['APIC-COOKIE'] = token

########### Get APN ############
# Get Application profile

url = "https://sandboxapicdc.cisco.com/api/node/mo/uni/tn-Heroes/ap-Power_Up.json"

headers = {
    'cache-control': "no-cache"
}

get_response = requests.get(
    url, headers=headers, cookies=cookie, verify=False).json()

# print(json.dumps(get_response, indent=2, sort_keys=True))


########### Change APN description ############
# set desc

post_payload = {
    "fvAp": {
        "attributes": {
            "descr": "",
            "dn": "uni/tn-Heroes/ap-Power_Up"
        }
    }
}


post_response = requests.post(
    url, headers=headers, cookies=cookie, verify=False, data=json.dumps(post_payload)).json()

# print(json.dumps(post_response, indent=2, sort_keys=True))

print(json.dumps(get_response, indent=2, sort_keys=True))