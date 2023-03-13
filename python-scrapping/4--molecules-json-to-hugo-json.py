import json
import glob
import os
import shutil
from slugify import slugify

inputFolderUrl = '../data/molecules/'
outputFolderUrl = '../hugo/content/molecules/'
inputImageFolderUrl = '../data/molecules-images/'

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
        dstUrl = outputFolderUrl + str(recipeJson["id"])
        os.mkdir(dstUrl)

        imgDstUrl = dstUrl + "/images/"
        os.mkdir(imgDstUrl)
        shutil.copy(inputImageFolderUrl +
                    str(recipeJson["id"]) + ".png", imgDstUrl + "preview.png")


        with open(dstUrl + '/index.json', 'w') as fp:
            fp.write(json.dumps(recipeJson))

print("Json to md done !")
