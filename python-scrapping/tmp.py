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
    try:
        with open(recipeFile, "r") as file:
            recipeJson = json.load(file)

            for ingredient in recipeJson["ingredients_sharing_molecules"]:
                
                try:
                    if(ingredient["common_molecules"][0][0]):
                        newArray = []
                    
                        for item in ingredient["common_molecules"]:
                            newArray.append(item[0])
                        
                        ingredient["common_molecules"] = newArray
                except:
                    print("toto")
            
            with open(recipeFile, 'w') as fp:
                fp.write(json.dumps(recipeJson))

    except json.decoder.JSONDecodeError as e:
        print("error")

print("Json to md done !")
