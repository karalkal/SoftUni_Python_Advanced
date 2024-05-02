import json

with open('some_json.json') as message_json:
  message = json.load(message_json)

  print(message['text'])
  print(message)