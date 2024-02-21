import requests

class DragonBallAPI:
    def __init__(self):
        self.url = 'https://dragonball-api.com/api'

    def get_characters_names(self):
        url = f'{self.url}/characters?limit=58'
        response = requests.get(url)
        if response.ok:
            data = response.json()
            return [character['name'] for character in data['items']]
        
    def get_characters_by_gender(self, gender):
        url = f'{self.url}/characters?limit=58'
        response = requests.get(url)
        if response.ok:
            data = response.json()
            return [character['name'] for character in data['items'] if character['gender'] == gender]
        
    def get_characters_by_race(self, race):
        url = f'{self.url}/characters?limit=58'
        response = requests.get(url)
        if response.ok:
            data = response.json()
            return [character['name'] for character in data['items'] if character['race'] == race]
        
        
    def get_weakest(self):
        url = f'{self.url}/characters?limit=58'
        response = requests.get(url)
        if response.ok:
            data = response.json()
            return [character['name'] for character in data['items'] if character['maxKi'] == '0']
        
    def get_strongest(self):
        url = f'{self.url}/characters?limit=58'
        response = requests.get(url)
        if response.ok:
            data = response.json()
            return [character['name'] for character in data['items'] if 'Googolplex' in character['maxKi']]
            
    
class Character:
    def __init__(self, name):
        self.name = name
        self.url = 'https://dragonball-api.com/api/characters/' + str(self.get_id_by_name(name))
    
    def get_id_by_name(self, name):
        url = f'https://dragonball-api.com/api/characters?limit=58'
        response = requests.get(url)
        if response.ok:
            data = response.json()
            return [character['id'] for character in data['items'] if character['name'] == name][0]
    
    def __str__(self):
        return self.name
    
    def __add__(self, other):
        return self.name[:4] + other.name[-4:]
    
    def get_transformations(self):
        response = requests.get(self.url)
        if response.ok:
            data = response.json()
            return [transformation['name'] for transformation in data['transformations']]
        
class Planet:
    def __init__(self, name):
        self.name = name
        self.url = 'https://dragonball-api.com/api/planets/' + str(self.get_id_by_name(name))
    
    def __str__(self):
        return self.name
    
    def get_id_by_name(self, name):
        url = 'https://dragonball-api.com/api/planets?limit=25'
        response = requests.get(url)
        if response.ok:
            data = response.json()
            return [planet['id'] for planet in data['items'] if planet['name'] == name][0]
    
    def get_planets(self):
        url = 'https://dragonball-api.com/api/planets?limit=25'
        response = requests.get(url)
        if response.ok:
            data = response.json()
            return [planet['name'] for planet in data['items']]
    
    def get_destroyed_planets(self):
        url = 'https://dragonball-api.com/api/planets?limit=25'
        response = requests.get(url)
        if response.ok:
            data = response.json()
            return [planet['name'] for planet in data['items'] if planet['isDestroyed'] == True]
        
    def get_character_planet(self, id):
        url = f'https://dragonball-api.com/api/characters/{id}'
        response = requests.get(url)
        if response.ok:
            data = response.json()
            return data['originPlanet']['name']
    
    def get_characters(self):
        url = 'https://dragonball-api.com/api/characters?limit=58'
        response = requests.get(url)
        if response.ok:
            data = response.json()
            return [character['name'] for character in data['items'] if self.get_character_planet(character['id']) == self.name]
    
char1 = Character('Gohan')
char2 = Character('Piccolo')
name = char1 + char2
print(name)

