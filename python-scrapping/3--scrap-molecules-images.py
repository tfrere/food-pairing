import json
import os
import re 
from bs4 import BeautifulSoup
from slugify import slugify

outputFolderUrl = '../data/molecules-images/'
moleculeFile = '../data/molecules.json'
    
def downloadImage(id):
    command = ("curl https://cosylab.iiitd.edu.in/flavordb2/static/molecules_images/" + str(id) + ".png > " + outputFolderUrl + str(id) + ".png").replace("\n", " ")
    os.popen(command).read()

with open(moleculeFile, "r") as file:
    molecules = json.load(file)
    for molecule in molecules:
        downloadImage(molecule)

