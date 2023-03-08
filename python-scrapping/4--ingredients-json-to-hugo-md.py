import json
import glob
import os
import shutil
from slugify import slugify

inputFolderUrl = '../data/ingredients/'
outputFolderUrl = '../hugo/content/ingredients/'

debug = False
recipes = [] 

if(debug):
    recipes = glob.glob(
        inputFolderUrl + "bakery-products.json")
else:
    recipes = glob.glob(inputFolderUrl + "*.json")

mdRecipes = glob.glob(outputFolderUrl + "*")
for mdRecipe in mdRecipes:
    shutil.rmtree(mdRecipe)

for recipeFile in recipes:
    with open(recipeFile, 'r') as fp:
        recipeJson = json.loads(fp.read())

        print(recipeJson)

        os.mkdir(outputFolderUrl + recipeJson["slug"])
        dstUrl = outputFolderUrl + recipeJson["slug"]

        recipeMd = f'---\n'
        recipeMd += f'  id : ' + f'{recipeJson["id"]}\n'
        recipeMd += f'  name : ' + f'"{recipeJson["name"]}"\n'
        recipeMd += f'  ingredients_sharing_molecules : ' + f'"{recipeJson["ingredients_sharing_molecules"][0:5]}"\n'
        recipeMd += f'  slug : ' + f'{recipeJson["slug"]}\n'
        recipeMd += f'  date : 2019-03-26T08:47:11+01:00\n'
        recipeMd += f'---\n\n\n'

        # ---------

        with open(dstUrl + '/index.md', 'w') as fp:
            fp.write(recipeMd)

print("Json to md done !")
