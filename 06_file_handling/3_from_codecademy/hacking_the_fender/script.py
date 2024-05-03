import csv
import json

# objective is to copy compromised users' usernames to new file 
# and add to passwords.csv the string from signature.txt

compromised_users = []

# get compromised accounts
with open ("passwords.csv") as password_file:    
    password_csv = csv.DictReader(password_file, delimiter=",")
    # print(list(password_csv))
    for password_row in password_csv:
        compromised_users.append(password_row['Username'])
    # print(compromised_users)
    
# write them in separate file
with open ("compromised_users.txt", "w") as compromised_user_file:
    for cu in compromised_users:
        compromised_user_file.write(cu)
        compromised_user_file.write("\n")  
        
# write json message
message_to_write = {"recipient": "The Boss", "message": "Mission Success"}
with open('boss_message.json', 'w') as boss_message_file:
  json.dump(message_to_write, boss_message_file)


# get the signature here, add it to passwords.csv with it later, not as per step-by-step guide
slash_null_sig = ""
with open ("signature.txt") as signature:
    slash_null_sig = signature.read()
# print(slash_null_sig)

   
# overwrite passwords.csv
with open ("passwords.csv", "a") as password_file:
    password_file.write(slash_null_sig)

  


