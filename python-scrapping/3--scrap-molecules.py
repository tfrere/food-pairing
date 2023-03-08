import json
import os
import re 
from bs4 import BeautifulSoup
from slugify import slugify

baseUrl = "https://cosylab.iiitd.edu.in/flavordb2"
moleculeFile = '../data/molecules.json'
outputFolderUrl = '../data/molecules/'


def getMoleculeData(url):
    result  = os.popen("curl "+ url).read()
    print(result)
    return json.loads(result)

with open(moleculeFile, "r") as file:
    molecules = json.load(file)
    for molecule in molecules:
        moleculeData = getMoleculeData(baseUrl+"/molecules_json?id=" + str(molecule))    
        response = {"slug": slugify(moleculeData["common_name"]), "id": molecule, "name": moleculeData["common_name"], "data": moleculeData}
        with open(outputFolderUrl + moleculeData["id"] + ".json", 'w') as fp:
            fp.write("%s\n" % json.dumps(response))
