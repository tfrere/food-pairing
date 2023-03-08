import json
import glob
import os
import shutil
from slugify import slugify

inputFolderUrl = '../data/molecules/'
outputFolderUrl = '../hugo/content/molecules/'

debug = False
recipes = [] 

if(debug):
    recipes = glob.glob(
        inputFolderUrl + "49.json")
else:
    recipes = glob.glob(inputFolderUrl + "*.json")

mdRecipes = glob.glob(outputFolderUrl + "*")
for mdRecipe in mdRecipes:
    shutil.rmtree(mdRecipe)

for recipeFile in recipes:
    with open(recipeFile, 'r') as fp:
        recipeJson = json.loads(fp.read())

        print(recipeJson)

        dstUrl = outputFolderUrl + str(recipeJson["id"])

        os.mkdir(dstUrl)

        recipeMd = f'---\n'
        recipeMd += f'  id : ' + f'{recipeJson["id"]}\n'
        recipeMd += f'  name : ' + f'"{recipeJson["name"]}"\n'
        recipeMd += f'  slug : ' + f'{recipeJson["id"]}\n'
        
        recipeMd += f'  taste : ' + f'{recipeJson["data"]["taste"]}\n'
        recipeMd += f'  bitter : ' + f'{recipeJson["data"]["bitter"]}\n'
        recipeMd += f'  odor : ' + f'{recipeJson["data"]["odor"]}\n'
        recipeMd += f'  natural : ' + f'{recipeJson["data"]["natural"]}\n'
        recipeMd += f'  flavor_profile : ' + f'{recipeJson["data"]["flavor_profile"]}\n'
        recipeMd += f'  fema_flavor_profile : ' + f'{recipeJson["data"]["fema_flavor_profile"]}\n'

        recipeMd += f'  date : 2019-03-26T08:47:11+01:00\n'
        recipeMd += f'---\n\n\n'

        # ---------

        with open(dstUrl + '/index.md', 'w') as fp:
            fp.write(recipeMd)

print("Json to md done !")
