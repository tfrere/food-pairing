import json
import os
import re 
from bs4 import BeautifulSoup
from slugify import slugify
from pprint import pprint

baseUrl = "https://cosylab.iiitd.edu.in/flavordb2"
outputFolderUrl = '../data/'

def getIngredientData(url):
    result  = os.popen("curl "+ url).read()
    return json.loads(json.loads(result))

def getIngredientName(url):
    result  = os.popen("curl "+ url).read()
    soup = BeautifulSoup(result)

    return soup.select('h1')[0].text.strip()

def writeIngredientFile(i):
    ingredientName = getIngredientName(baseUrl+"/food_pairing?id=" + str(i))
    print(str(i) + " - " + ingredientName)
    if(ingredientName == "Page not found (404)" or ingredientName == "Not Found"):
        return False
    else:
            

        ingredientData = getIngredientData(baseUrl+"/food_pairing_analysis?id=" + str(i))
        sortedData = sorted(ingredientData.items(), key=lambda item: len(item[1]["common_molecules"]),reverse=True)

        data = []
        for item in sortedData:
            newItem = {"name": item[1]["entity_details"]["name"], "wiki": item[1]["entity_details"]["wiki"].replace("https://en.wikipedia.org/wiki/", ""), "id": item[1]["entity_details"]["id"], "category": item[1]["entity_details"]["category"], "common_molecules": item[1]["common_molecules"]}
            data.append(newItem)

        response = {"id": i, "category": ingredientData["0"]["entity_details"]["category"], "slug": slugify(ingredientName), "name": ingredientName, "ingredients_sharing_molecules": data}
        with open(outputFolderUrl + "/ingredients/" + slugify(ingredientName) + ".json", 'w') as fp:
            fp.write("%s\n" % json.dumps(response))
        return True


min = 321
max = 322
step = 1

for i in range(min, max, step):
    writeIngredientFile(i)
    


