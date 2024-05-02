import json

data_payload = [
  {'interesting message': 'What is JSON? A web application\'s little pile of secrets.',
   'follow up': 'But enough talk!'}
]


with open('newly_created_json.json', 'w') as data_json:
  json.dump(data_payload, data_json)
