import requests
import json

switchuser = "admin"
switchpassword = "Admin_1234!"

url = "https://sbx-nxos-mgmt.cisco.com/ins"
myheaders={'content-type':'application/json'}
payload = {
  "ins_api": {
    "version": "1.0",
    "type": "cli_show",
    "chunk": "0",
    "sid": "sid",
    "input": "show cdp nei",
    "output_format": "json"
  }
}

response = requests.post(url, data=json.dumps(
    payload), headers=myheaders, auth=(switchuser, switchpassword), verify=False).json()

# print(json.dumps(response, indent=2, sort_keys=True))

auth_url = "https://sbx-nxos-mgmt.cisco.com/api/mo/aaaLogin.json"
auth_body = {"aaaUser": {"attributes": {
      "name": switchuser, "pwd": switchpassword}}}
auth_response =  requests.post(
    auth_url,json=auth_body,timeout=5,verify=False).json()
token = auth_response['imdata'][0]['aaaLogin']['attributes']['token']
print(token)

cookies = {}
cookies = ['APIC-Cookie'] = token
headers = {"content-type": "application/json"}

counter = 0

