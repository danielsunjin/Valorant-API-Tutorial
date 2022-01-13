import requests
import json
import urllib.request
from PIL import Image

#retrieve the agent data from the Valorant API via a get request
response = requests.get('https://valorant-api.com/v1/agents')
data = response.json() #convert the JSON data from the API to a dictionary

#create a dictionary to store the agent data by agent name
agents = {}

for i in data['data']:
    agents[i['displayName'].lower()] = i

#ask the user to input an agent name until a valid name is entered
#and store the input
print()
agent = input('Input the name of an agent here: ').lower()

while agent not in agents:
    agent = input('Your agent does not exist. Input the name of an agent here: ')

agent_data = agents[agent]

#display the agent name and description
print()
print(agent_data['displayName'])
print()
print(agent_data['description'])

#ask the user whether they want to see the agent's role
print()
see_role = input('See ' + agent + "'s role? (y/n): ")

#if yes, print the agent's role and role description
if see_role.lower() == 'y' or see_role.lower() == 'yes':
    role_data = agent_data['role']

    print()
    print(agent + " is a " + role_data['displayName'] + ". " + role_data['description'])

#ask the user whether they want to see the agent's abilities
print()
see_abilities = input('See ' + agent + "'s abilites? (y/n): ")

#if yes, print the agent's abilities and ability descriptions
if see_abilities.lower() == 'y' or see_abilities.lower() == 'yes':
    abilities_data = agent_data['abilities']
    for j in abilities_data:
        print()
        print(j['displayName'] + ": " + j['description'])

#ask the user whether they want to see the agent's portrait
print()
see_agent = input('See ' + agent + "'s portrait? (y/n): ")

#if yes, load the agent's portrait
if see_agent.lower() == 'y' or see_agent.lower() == 'yes':
    agent_image = agent_data['bustPortrait']
    urllib.request.urlretrieve(agent_image, 'agent_image.png')
    img = Image.open("agent_image.png")
    img.show()

print()
