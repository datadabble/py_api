#JSON with python

#Import modules

import requests
from tkinter import *
from PIL import Image, ImageTk #loading image files
from characters import Character

#create method
def load_data():

    #make http request to URL
    url = 'https://rickandmortyapi.com/api/character/?page=1'
    response = requests.get(url)
    json_res = response.json()
    json_res_results = json_res['results']

    #index json objects like you would a python dic
    characters = []

    for obj in json_res_results:
        name = obj['name']
        gender = obj['gender']
        species = obj['species']
        origin = obj['origin']['name']
        status = obj['status']
        image = obj['image']
        number_of_episodes = len(obj['episode'])

        character = Character(name, gender, species, origin,  status, image, number_of_episodes)

        character.show_character()
        characters.append(character)
        
    return characters


characters = load_data()

 