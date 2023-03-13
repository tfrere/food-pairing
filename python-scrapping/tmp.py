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

# POUR CHAQUE INGREDIENT
for recipeFile in recipes:
    with open(recipeFile, "r") as file:
        recipeJson = json.load(file)


        #  si pas de molecules en commun du tout
        #  ou si la categorie n'est pas listée dans le fichier catégorie

        # # OUVRE LE FICHIER ET RELISTE CHAQUE INGREDIENT

        # print(recipeJson["name"])

        # try:
        #     recipeJson["category"] = recipeJson["category"]

        # except:    
        #     for recipeFile2 in recipes:
        #         with open(recipeFile2, "r") as file:
        #             recipeJson2 = json.load(file)

        #             print(recipeJson2["name"])

        #             # LISTE LES INGREDIENTS EN COMMUN

        #             for ingredient in recipeJson2["ingredients_sharing_molecules"]:

        #                 # SI LE NOM DU FICHIER D ORIGINE EST EGAL A LINGREDIENT EN COURS

        #                 print(ingredient["name"] +" == "+ recipeJson["name"])

        #                 if(ingredient["id"] == recipeJson["id"]):
        #                     recipeJson["category"] = ingredient["category"]
        #                     with open(recipeFile, 'w') as fp:
        #                         fp.write(json.dumps(recipeJson))
        #                     break
        #                     break
                


print("Json to md done !")
