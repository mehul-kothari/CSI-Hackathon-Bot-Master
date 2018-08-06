import requests
import json

luis_url = ""
while True:
    user_input = input()
    params = {"q" : user_input}
    r = requests.get(luis_url, params = params)
    luis_response = json.load(r.json())
    # Enter your code here and store response in variable called bot_output
    # luis_response is a dictionary containing the response
    print(bot_output)
