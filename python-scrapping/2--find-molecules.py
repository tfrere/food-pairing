import json
import glob
import os
import shutil
from slugify import slugify
import numpy as np

inputFolderUrl = '../data/ingredients/'
outputFolderUrl = '../data/'

debug = False
involvedMolecules = np.array([]) 
index = 0

if(debug):
    recipes = glob.glob(inputFolderUrl + "bakery-products.json")
else:
    recipes = glob.glob(inputFolderUrl + "*.json")

for recipeFile in recipes:
    with open(recipeFile, "r") as file:
        index += 1
        print(index)
        recipeJson = json.load(file)

        for ingredient in recipeJson["ingredients_sharing_molecules"]:

            involvedMolecules = np.unique(np.concatenate((involvedMolecules, np.array(ingredient["common_molecules"])), axis=None))

with open(outputFolderUrl + "molecules.json", 'w') as fp:
    fp.write(json.dumps(involvedMolecules.astype(int).tolist()))
