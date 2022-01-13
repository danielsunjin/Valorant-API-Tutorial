# Valorant-API-Tutoria
[Valorant](https://playvalorant.com/en-us/) is a popular FPS tactical shooter game developed by RIOT Games. In this game, players can choose to play different characters, called *agents*, with unique abilities. Information about these agents can be retrieved from the Valorant API in [JSON](https://en.wikipedia.org/wiki/JSON) (JavaScript Object Notation) format. This repository uses the Valorant API to give the reader an introductory tutorial to retrieving JSON data from APIs using Python. This tutorial assumes the reader has basic knowledge of Python, including data types and indexing.

### Retrieving Data From the Valorant API Using a GET Request

Web APIs, such as the Valorant API, contain useful information that programmers like you and I can work with. We can access this data using GET requests. As the name states, [GET requests](https://www.w3schools.com/tags/ref_httpmethods.asp) are used to get infromation from a web API. A GET request in Python is done using the get() function of the requests library like so:

```python
import requests

#retrieve the agent data from the Valorant API via a get request and the API url
response = requests.get('https://valorant-api.com/v1/agents')
```

### Converting the Retrieved JSON Data to a Python Dictionary

The data retrieved will be a JSON object for the Valorant API. JSON objects are largely analogous in structure to dictionary objects in Python, which are much easier to work with when trying to get entries of specific categories of data. We can convert JSON objects to Python dictionaries using the json() function of the json library like so:

```python
import json

#convert the JSON data to a Python dictionary
data = response.json()
```

### Navigating the Dictionary

Python dictionaries are organized into keys and values, with the key being the "name" that refers to a specific data object (the value) in the dictionary. Python dictionaries are bounded by curly braces, keys and values are separated by colons, and key-value pairs are separated by commas. The values in a dictionary can be any Python object, even other dictionaries. The key must be an immutable object, most commonly a string. Take this dictionary for example that contains information about a car:

```python
car = {'color': 'blue', 'year': 2021, 'previous owners': ['Bob', 'Joe'], 'dimensions': {'height': 5, 'width': 7}}
```

To get the value of a key in a dictionary, put the key within brackets following the dictionary name in your code. If the value happens to be a sequence data type like a list or another dictionary, you can get an element within the key's value by adding on another set of brackets with an index or key of your desire. Some examples:

```python
car['color'] #-> returns 'blue'
car['previous owners'] #-> returns ['Bob', 'Joe']
car['previous owners'][0] #-> returns 'Bob'
car['dimensions']['height'] #-> returns 5
```

Going back to the Valorant API, the Agent data dictionary loaded from the Valorant API contains keys for dictionaries of information about each agent. Each of these sub-dictionaries contains data such as agent name, agent description, agent abilities, etc. The keys for each agent's data in the dictionary is a number. For example, the key for the agent Breach is 0, and the key for the agent Skye is 4. Here are the keys for each agent's information:

| Key | Agent |
|---|---|
| 0 | Breach |
| 1 | Raze |
| 2 | Chamber |
| 3 | KAY/O |
| 4 | Skye |
| 5 | Cypher |
| 6 | Sova |
| 7 | Sova |
| 8 | Killjoy |
| 9 | Viper |
| 10 | Phoenix |
| 11 | Astra |
| 12 | Brimstone |
| 13 | Neon |
| 14 | Yoru |
| 15 | Sage |
| 16 | Reyna |
| 17 | Omen |
| 18 | Jett |

To get the dictionary information for Jett, for example, you would use the following code:888

```python
data[18]
```

To get things like Jett's name or character description, you would do the following:

```python
data[18]['displayName'] #-> returns Jett's name (a string)
data[18]['description'] #-> returns Jett's description (a string)
```

Some key values contain other dictionaries, such as the abilities key. The abilities of an agent have keys ranging from 0 to 3 for each of the agent's 4 abilities. The values for these keys are dictionaries containing further infromation, scuh as the ability's name or description. Some examples:

```python
data[18]['abilities'] #-> returns a dictionary of Jett's abilities
data[18]['abilities'][0]['name'] #-> returns a string for the name of Jett's first ability
```

Sometimes the string values for a key can be more meaningful than usual. For example, the value of the "bustPortrait" key for an agent is a url link to a png image of that agent. The following code will load the image of Jett from the url given by the "bustPortrait" key:

```python
import urllib.request
from PIL import Image

agent_image = agent_data['bustPortrait']
urllib.request.urlretrieve(agent_image, 'agent_image.png')
img = Image.open("agent_image.png")
img.show()
```

The resulting image:

![Jett Agent Image]()

Note: PIL refers to [Pillow](https://pillow.readthedocs.io/en/stable/), a Python imaging library that is not built into the language and will need to be installed. 

An thorough overview of the keys and data in the agent data from the Valorant API can be found on the Valorant API website [here](https://dash.valorant-api.com/endpoints/agents). 

### Example Application of the Valorant API

An example of how one might use the Valorant API is the Valorant.py program that I coded in this repository. This program asks a user to input the name of a Valorant agent and presents the user with the agent's name and description. If the user wishes to see the agent's role, abilities, or image, the program outputs that image to the screen as well. Here is an example output of the program:

```

Input the name of an agent here: Jett

Jett

Representing her home country of South Korea, Jett's agile and evasive fighting style lets her take risks no one else can. She runs circles around every skirmish, cutting enemies up before they even know what hit them.

See jett's role? (y/n): y

jett is a Duelist. Duelists are self-sufficient fraggers who their team expects, through abilities and skills, to get high frags and seek out engagements first.

See jett's abilites? (y/n): y

Updraft: INSTANTLY propel Jett high into the air.

Tailwind: INSTANTLY propel Jett in the direction she is moving. If Jett is standing still, she will propel forward.

Cloudburst: INSTANTLY throw a projectile that expands into a brief vision-blocking cloud on impact with a surface. HOLD the ability key to curve the smoke in the direction of your crosshair.

Blade Storm: EQUIP a set of highly accurate throwing knives. FIRE to throw a single knife and recharge knives on a kill. ALTERNATE FIRE to throw all remaining daggers but does not recharge on a kill.

Drift: Holding the jump button while falling allows you to glide through the air.

See jett's portrait? (y/n): y

```
![Jett Portrait]()
