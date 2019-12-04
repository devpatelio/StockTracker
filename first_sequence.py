
#Primary variable for data is test[_key and value_]

import requests
import json

parameters = {
    " ":"", '':""
}

stock = input('What stock data would you like to collect:')
primary_request = requests.get("https://www.alphavantage.co/query?function=GLOBAL_QUOTE&symbol=" + stock + "&apikey=E7W0A9REUL6LY9J9", params=parameters)


def stockprint(object):  #turn funciton into class for variable use
    text = json.dumps(object, sort_keys=True, indent=4)
    print(text)

print(primary_request.status_code)

stockprint(primary_request.json())

test = primary_request.json()["Global Quote"]  #test to see if method works
stockprint(test) #printing information


hardcode = json.dumps(test, sort_keys=True, indent=4)

opening = open('reduced.json', 'w+')

with open('reduced.json', 'w') as f:
    f.write(hardcode)


values = list(test.values())

print("Great! You picked to track the stock " + stock +"! The current price of your selection is $" + test['05. price'] + ". Here's the current data for your stock")

