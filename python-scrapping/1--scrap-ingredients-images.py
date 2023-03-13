import json
import os
import re 
from bs4 import BeautifulSoup
from slugify import slugify
from pprint import pprint

outputFolderUrl = '../data/ingredients-images/'
    
def downloadImage(id):
    command = ("curl https://cosylab.iiitd.edu.in/flavordb2/static/entities_images/" + str(id) + ".jpg > " + outputFolderUrl + str(id) + ".jpg").replace("\n", " ")
    os.popen(command).read()

min = 0
max = 1000
step = 1

for i in range(min, max, step):
    downloadImage(i)


