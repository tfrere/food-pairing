import json
import glob
import os
import shutil
from slugify import slugify

inputFolderUrl = '../data/ingredients/'
outputFolderUrl = '../../hugo/content/pairings/'

debug = True
recipes = [] 

if(debug):
    recipes = glob.glob(
        inputFolderUrl + "backery-products.json")
else:
    recipes = glob.glob(inputFolderUrl + "*.json")

mdRecipes = glob.glob(outputFolderUrl + "*")
for mdRecipe in mdRecipes:
    shutil.rmtree(mdRecipe)

for recipeFile in recipes:
    with open(recipeFile, 'r') as fp:
        recipeJson = json.loads(fp.read())

        os.mkdir(outputFolderUrl + recipeJson["slug"])

        dstUrl = outputFolderUrl + recipeJson["slug"] + "/"

        recipeMd = f'---\n'
        recipeMd += f'  name : ' + f'"{recipeJson["name"]}"\n'
        recipeMd += f'  slug : ' + f'{recipeJson["slug"]}\n'
        # recipeMd += f'  image : ' + f'{recipeJson["image_file_name"]}\n'
        # recipeMd += f'  keywords : ' + f'{recipeJson["tags"]}\n'
        recipeMd += f'  date : 2019-03-26T08:47:11+01:00\n'

        # recipeMd += f'  about : ' + f'"{recipeJson["about"]}"\n'
        # recipeMd += f'  author : ' + f'"{recipeJson["author"]}"\n'
        # recipeMd += f'  book : ' + f'"{recipeJson["book"]}"\n'
        # recipeMd += f'  notes : ' + f'"{recipeJson["notes"]}"\n'
        # recipeMd += f'  size : ' + f'"{recipeJson["size"]}"\n'
        # recipeMd += f'  draft : false\n'

        # recipeMd += f'  number_of_ingredients : {len(recipeJson["ingredients"])}\n'

        # recipeMd += f'  ingredients : \n'

        # # for ingredient in recipeJson["ingredients"]:
        # #     recipeMd += f'  - {ingredient["value"]}\n'

        # for ingredient in recipeJson["ingredients"]:
        #     recipeMd += f'    - "{ingredient["value"].replace(":", "") or ""}"\n'

        # recipeMd += f'  number_of_steps : {len(recipeJson["steps"])}\n'
        # recipeMd += f'  steps : \n'
        # for step in recipeJson["steps"]:
        #     recipeMd += f'    - "{step.replace(":", "")}"\n'
        recipeMd += f'---\n\n\n'

        # ---------

        with open(dstUrl + 'index.md', 'w') as fp:
            fp.write(recipeMd)

print("Json to md done !")