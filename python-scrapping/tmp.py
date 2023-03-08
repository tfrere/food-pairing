import json
import glob
import os
import shutil
from slugify import slugify

inputFolderUrl = '../data/ingredients/'
outputFolderUrl = '../data/ingredients/'

debug = False
recipes = [] 

if(debug):
    recipes = glob.glob(inputFolderUrl + "bakery-products.json")
else:
    recipes = glob.glob(inputFolderUrl + "*.json")

for recipeFile in recipes:
    with open(recipeFile, 'r') as fp:
        text = fp.read().replace("'", "\"")
        recipeJson = json.loads(text)

        recipeJson["slug"] = slugify(recipeJson["name"])

        with open(recipeFile, 'w') as fp:
            fp.write(json.dumps(recipeJson))

print("Json to md done !")
