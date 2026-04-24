import json
import yaml
 
with open('/home/devasc/labs/devnet-src/parsing/myfile.json') as json_file:
 
    ourjson = json.load(json_file)

print("Token:", ourjson['access_token'])


print("The token expires in {} seconds.".format(ourjson['expires_in']))
