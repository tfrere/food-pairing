import json
import os
import re 
from bs4 import BeautifulSoup
from slugify import slugify

baseUrl = "https://cosylab.iiitd.edu.in/"
outputFolderUrl = '../data/molecules/'

def getMoleculeData(url):
    result  = os.popen("curl "+ url).read()
    print(result)
    return json.loads(result)

for i in range(2):
    moleculeData = getMoleculeData(baseUrl+"flavordb/molecules_json?id=" + str(i))
    if(moleculeData == "Page not found (404)"):
        break
    else:
        response = {"index": i, "name": moleculeData["common_name"], "data": moleculeData.keys()}
        with open(outputFolderUrl + slugify(moleculeData["common_name"]) + ".json", 'w') as fp:
            fp.write("%s\n" % response)