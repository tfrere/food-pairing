import json
import glob
import os
import shutil
from slugify import slugify
import pprint

inputFolderUrl = '../data/ingredients/'
inputMoleculeFolderUrl = '../data/molecules/'
inputImageFolderUrl = '../data/ingredients-images/'
outputFolderUrl = '../hugo/content/ingredients/'
indexOutputFolderUrl = '../hugo/assets/data/'

filteredCategories = json.load(open('../data/filtered-categories.json'))

filteredIngredientKeywordsList = json.load(open('../data/filtered-ingredient-keywords.json'))
filteredIngredientKeywords = ''.join(filteredIngredientKeywordsList)


debug = False
recipes = [] 
involvedIngredients = []
involvedIngredientsList = []

if(debug):
    recipes = glob.glob(
        inputFolderUrl + "bakery-products.json")
else:
    recipes = glob.glob(inputFolderUrl + "*.json")

mdRecipes = glob.glob(outputFolderUrl + "*")
for mdRecipe in mdRecipes:
    shutil.rmtree(mdRecipe)

def getImageUrl(url):
    result  = os.popen("curl "+ url).read()
    return json.loads(json.loads(result)).thumbnail.source

def copyIngredient(recipeJson):
    os.mkdir(outputFolderUrl + recipeJson["slug"])
    dstUrl = outputFolderUrl + recipeJson["slug"]

    imgDstUrl = outputFolderUrl + recipeJson["slug"] + "/images/"
    os.mkdir(imgDstUrl)
    shutil.copy(inputImageFolderUrl +
                str(recipeJson["id"]) + ".jpg", imgDstUrl + "preview.jpg")

    with open(dstUrl + '/index.json', 'w') as fp:
        fp.write(json.dumps(recipeJson))

def consolidateMolecule(id):
    with open(inputMoleculeFolderUrl + str(id) +'.json', 'r') as fp:
        data = json.loads(fp.read())
        return data

hasToListIngredient = True

def iterate():

    count = 0
    for recipeFile in recipes:
        with open(recipeFile, 'r') as fp:
            recipeJson = json.loads(fp.read())

            try:
                # si c'est dans les catégories filtrées
                # OK 
                if recipeJson["category"] in filteredCategories:

                    # si c'est pas  dans les mots clés filtrés
                    # OK
                    isInKeywords = any(x in recipeJson["name"] for x in filteredIngredientKeywordsList)
                    if not isInKeywords:

                        # on prends les 8 premiers
                        # OK
                        recipeJson["ingredients_sharing_molecules"] = recipeJson["ingredients_sharing_molecules"][0:16]

                        # chaque match doit avoir plus de X
                        # SEEMS OK
                        expectedResult = [item for item in recipeJson["ingredients_sharing_molecules"] if len(item['common_molecules']) > 8]

                        # si les ingredients sont dans la liste 
                        # OK
                        if(not hasToListIngredient):
                            expectedResult = [item for item in recipeJson["ingredients_sharing_molecules"] if any(x in item['name'] for x in involvedIngredientsList)]

                        # après ça on recheck si il y à tjrs des match
                        if len(expectedResult) > 0:
                            count += 1

                            if(not hasToListIngredient):
                                newRecipe = recipeJson
                                newRecipe["ingredients_sharing_molecules"] = expectedResult
                                
                                # if(count == 1):
                                #     print(newRecipe)
           
                                # for ingredient in recipeJson["ingredients_sharing_molecules"]:
                                #     newMolecules = []
                                #     for molecule in ingredient["common_molecules"]:
                                #         newMolecules.append(consolidateMolecule(molecule))
                                #     ingredient["common_molecules"] = newMolecules
                                
                                # if(count == 1):
                                #     print(newMolecules)

                                copyIngredient(newRecipe)
                            else: 
                                involvedIngredients.append({"name":recipeJson["name"], "slug":recipeJson["slug"]})
                                involvedIngredientsList.append(recipeJson["name"])

            except:
                print("toto")

    print(count)
    if(hasToListIngredient):
        with open(indexOutputFolderUrl + "ingredient-index.json", 'w') as fp:
            fp.write(json.dumps(involvedIngredients))

iterate()
hasToListIngredient = False
iterate()

print("Json to md done !")
